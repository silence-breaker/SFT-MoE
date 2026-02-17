"""
RANSTRUCT FAISS 管理模块

实现向量索引和相似性搜索功能：
- 使用 BGE-Small-EN-1.5 嵌入模型
- 构建 FAISS 索引
- 执行相似性搜索
"""

import os
import pickle
import logging
from pathlib import Path
from typing import List, Dict, Optional, Tuple, Any
import numpy as np

# 设置 HuggingFace 镜像源（解决国内网络问题）
if 'HF_ENDPOINT' not in os.environ:
    os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'

try:
    import faiss
except ImportError:
    faiss = None
    print("警告: faiss 未安装，请运行 pip install faiss-cpu 或 pip install faiss-gpu")

try:
    from sentence_transformers import SentenceTransformer, CrossEncoder
except ImportError:
    SentenceTransformer = None
    CrossEncoder = None
    print("警告: sentence-transformers 未安装，请运行 pip install sentence-transformers")

from .config import Config, FAISSConfig
from .data_processor import Chunk

logger = logging.getLogger(__name__)


class EmbeddingGenerator:
    """嵌入向量生成器"""
    
    # 本地模型路径优先级
    LOCAL_MODEL_PATHS = [
        "/app/models/bge-small-en-v1.5",  # Docker 容器挂载路径
        "models/bge-small-en-v1.5",        # 项目相对路径
    ]
    
    def __init__(self, model_name: str = "BAAI/bge-small-en-v1.5", device: str = "cuda"):
        """
        初始化嵌入生成器
        
        Args:
            model_name: 嵌入模型名称
            device: 计算设备 ("cuda", "cpu", "mps")
        """
        if SentenceTransformer is None:
            raise ImportError("请安装 sentence-transformers: pip install sentence-transformers")
        
        self.model_name = model_name
        self.device = device
        
        # 优先使用本地模型（避免网络下载）
        local_path = None
        for path in self.LOCAL_MODEL_PATHS:
            if os.path.exists(path):
                local_path = path
                break
        
        if local_path:
            logger.info(f"使用本地嵌入模型: {local_path}")
            self.model = SentenceTransformer(local_path, device=device)
        else:
            logger.info(f"正在加载嵌入模型: {model_name}")
            self.model = SentenceTransformer(model_name, device=device)
        
        self.dimension = self.model.get_sentence_embedding_dimension()
        logger.info(f"嵌入维度: {self.dimension}")
    
    def encode(
        self, 
        texts: List[str], 
        batch_size: int = 32,
        show_progress: bool = True,
        normalize: bool = True
    ) -> np.ndarray:
        """
        将文本编码为向量
        
        Args:
            texts: 文本列表
            batch_size: 批处理大小
            show_progress: 是否显示进度条
            normalize: 是否归一化向量
            
        Returns:
            嵌入向量数组 (n_texts, dimension)
        """
        embeddings = self.model.encode(
            texts,
            batch_size=batch_size,
            show_progress_bar=show_progress,
            normalize_embeddings=normalize
        )
        return embeddings
    
    def encode_single(self, text: str, normalize: bool = True) -> np.ndarray:
        """编码单个文本"""
        return self.encode([text], show_progress=False, normalize=normalize)[0]


class FAISSManager:
    """FAISS 索引管理器 (支持 GPU 加速)"""
    
    def __init__(self, config: Config):
        """
        初始化 FAISS 管理器
        
        Args:
            config: RANSTRUCT 配置
        """
        if faiss is None:
            raise ImportError("请安装 faiss: pip install faiss-cpu 或 faiss-gpu")
        
        self.config = config
        self.faiss_config = config.faiss
        self.model_config = config.model
        
        self.index: Optional[faiss.Index] = None
        self.gpu_index: Optional[faiss.Index] = None  # GPU 索引
        self.embedding_generator: Optional[EmbeddingGenerator] = None
        self.chunks: List[Chunk] = []
        self.chunk_id_map: Dict[int, str] = {}  # faiss_id -> chunk_id
        
        self._dimension = self.model_config.embedding_dimension
        self._use_gpu = config.device == "cuda" and self._check_gpu_available()
        self._gpu_resources = None
    
    def _check_gpu_available(self) -> bool:
        """检查 GPU 是否可用于 FAISS"""
        # 检查环境变量，允许强制禁用 GPU
        if os.environ.get('FAISS_NO_GPU', '').lower() in ('1', 'true', 'yes'):
            logger.info("检测到 FAISS_NO_GPU 环境变量，使用 CPU 模式")
            return False
        
        try:
            num_gpus = faiss.get_num_gpus()
            if num_gpus > 0:
                # 检查 CUDA 版本兼容性
                # faiss-gpu PyPI 包通常只支持 CUDA 11.x
                # CUDA 12.x 需要 conda 安装或 faiss-cpu
                import torch
                cuda_version = torch.version.cuda if torch.cuda.is_available() else "0"
                if cuda_version and cuda_version.startswith("12"):
                    logger.warning(f"检测到 CUDA {cuda_version}，faiss-gpu PyPI 包可能不兼容")
                    logger.warning("建议设置 FAISS_NO_GPU=1 使用 CPU 模式，或通过 conda 安装 faiss-gpu")
                    logger.info("自动回退到 CPU 模式以避免卡死")
                    return False
                
                logger.info(f"检测到 {num_gpus} 个 GPU，将使用 GPU 加速 FAISS")
                return True
        except Exception as e:
            logger.warning(f"检查 GPU 时出错: {e}")
        
        logger.info("使用 CPU 模式")
        return False
    
    def _to_gpu(self, index: faiss.Index) -> faiss.Index:
        """将索引转移到 GPU"""
        if not self._use_gpu:
            return index
        
        # 检查环境变量，允许强制禁用 GPU
        if os.environ.get('FAISS_NO_GPU', '').lower() in ('1', 'true', 'yes'):
            logger.info("检测到 FAISS_NO_GPU 环境变量，跳过 GPU 加速")
            return index
        
        try:
            logger.info("正在初始化 GPU 资源...")
            if self._gpu_resources is None:
                self._gpu_resources = faiss.StandardGpuResources()
                # 限制 GPU 内存使用 (为其他任务预留空间)
                self._gpu_resources.setTempMemory(512 * 1024 * 1024)  # 512MB
            
            logger.info("正在执行 index_cpu_to_gpu...")
            gpu_index = faiss.index_cpu_to_gpu(self._gpu_resources, 0, index)
            logger.info("FAISS 索引已转移到 GPU")
            return gpu_index
        except Exception as e:
            logger.warning(f"GPU 转移失败，使用 CPU: {e}")
            return index
    
    def initialize_embedding_generator(self):
        """初始化嵌入生成器"""
        if self.embedding_generator is None:
            model_name = f"BAAI/{self.model_config.embedding_model}"
            self.embedding_generator = EmbeddingGenerator(
                model_name=model_name,
                device=self.config.device
            )
            self._dimension = self.embedding_generator.dimension
    
    def _create_index(self, dimension: int) -> faiss.Index:
        """
        创建 FAISS 索引
        
        Args:
            dimension: 向量维度
            
        Returns:
            FAISS 索引对象
        """
        index_type = self.faiss_config.index_type.lower()
        
        if index_type == "flat":
            # 精确搜索，适合小数据集
            index = faiss.IndexFlatIP(dimension)  # 内积（用于归一化向量等同于余弦相似度）
            
        elif index_type == "ivf":
            # IVF 索引，适合大数据集
            quantizer = faiss.IndexFlatIP(dimension)
            index = faiss.IndexIVFFlat(
                quantizer, 
                dimension, 
                self.faiss_config.nlist,
                faiss.METRIC_INNER_PRODUCT
            )
            
        elif index_type == "hnsw":
            # HNSW 索引，高效近似搜索
            index = faiss.IndexHNSWFlat(
                dimension,
                self.faiss_config.hnsw_m,
                faiss.METRIC_INNER_PRODUCT
            )
            index.hnsw.efConstruction = self.faiss_config.hnsw_ef_construction
            index.hnsw.efSearch = self.faiss_config.hnsw_ef_search
            
        else:
            raise ValueError(f"不支持的索引类型: {index_type}")
        
        device_str = "GPU" if self._use_gpu else "CPU"
        logger.info(f"已创建 {index_type.upper()} 索引 (维度: {dimension}, 设备: {device_str})")
        return index
    
    def build_index(self, chunks: List[Chunk], batch_size: int = 128):
        """
        从 chunks 构建 FAISS 索引
        
        Args:
            chunks: RAG Chunks 列表
            batch_size: 嵌入批处理大小 (GPU 可用更大值)
        """
        if not chunks:
            logger.warning("没有可索引的 chunks")
            return
        
        # 初始化嵌入生成器
        self.initialize_embedding_generator()
        
        # 提取文本
        texts = [chunk.content for chunk in chunks]
        
        logger.info(f"正在为 {len(texts)} 个 chunks 生成嵌入向量...")
        embeddings = self.embedding_generator.encode(texts, batch_size=batch_size)
        
        # 创建索引
        self.index = self._create_index(self._dimension)
        
        # 对于 IVF 索引，需要先训练
        if self.faiss_config.index_type.lower() == "ivf":
            if not self.index.is_trained:
                logger.info("正在训练 IVF 索引...")
                self.index.train(embeddings)
        
        # 添加向量
        self.index.add(embeddings)
        
        # 转移到 GPU (如果可用)
        if self._use_gpu:
            self.gpu_index = self._to_gpu(self.index)
        
        # 保存 chunks 和映射
        self.chunks = chunks
        self.chunk_id_map = {i: chunk.chunk_id for i, chunk in enumerate(chunks)}
        
        logger.info(f"FAISS 索引构建完成，包含 {self.index.ntotal} 个向量")
    
    def _get_search_index(self) -> faiss.Index:
        """获取用于搜索的索引 (优先使用 GPU)"""
        if self.gpu_index is not None:
            return self.gpu_index
        return self.index
    
    def search(
        self, 
        query: str, 
        top_k: Optional[int] = None
    ) -> List[Tuple[Chunk, float]]:
        """
        搜索最相似的 chunks
        
        Args:
            query: 查询文本
            top_k: 返回的结果数量
            
        Returns:
            (chunk, score) 元组列表
        """
        if self.index is None:
            raise RuntimeError("索引未初始化，请先调用 build_index 或 load_index")
        
        if top_k is None:
            top_k = self.faiss_config.top_k
        
        # 生成查询向量
        self.initialize_embedding_generator()
        query_vector = self.embedding_generator.encode_single(query)
        query_vector = query_vector.reshape(1, -1)
        
        # 获取搜索索引 (优先 GPU)
        search_index = self._get_search_index()
        
        # 设置 IVF 搜索参数
        if self.faiss_config.index_type.lower() == "ivf":
            search_index.nprobe = self.faiss_config.nprobe
        
        # 搜索
        scores, indices = search_index.search(query_vector, top_k)
        
        # 组装结果
        results = []
        for score, idx in zip(scores[0], indices[0]):
            if idx >= 0:
                if idx < len(self.chunks):
                    results.append((self.chunks[idx], float(score)))
                else:
                    # 没有 chunks 元数据时，返回占位信息
                    placeholder = Chunk(
                        content=f"[Document index: {idx}]",
                        chunk_type="rag",
                        source_doc_id=f"doc_{idx}",
                        chunk_index=idx,
                        metadata={"note": "元数据未加载，仅有索引位置"}
                    )
                    results.append((placeholder, float(score)))
        
        return results
    
    def search_batch(
        self, 
        queries: List[str], 
        top_k: Optional[int] = None
    ) -> List[List[Tuple[Chunk, float]]]:
        """
        批量搜索
        
        Args:
            queries: 查询文本列表
            top_k: 每个查询返回的结果数量
            
        Returns:
            每个查询的结果列表
        """
        if self.index is None:
            raise RuntimeError("索引未初始化")
        
        if top_k is None:
            top_k = self.faiss_config.top_k
        
        # 批量生成查询向量
        self.initialize_embedding_generator()
        query_vectors = self.embedding_generator.encode(queries, show_progress=False)
        
        # 获取搜索索引 (优先 GPU)
        search_index = self._get_search_index()
        
        # 设置 IVF 搜索参数
        if self.faiss_config.index_type.lower() == "ivf":
            search_index.nprobe = self.faiss_config.nprobe
        
        # 批量搜索
        all_scores, all_indices = search_index.search(query_vectors, top_k)
        
        # 组装结果
        all_results = []
        for scores, indices in zip(all_scores, all_indices):
            results = []
            for score, idx in zip(scores, indices):
                if idx >= 0 and idx < len(self.chunks):
                    results.append((self.chunks[idx], float(score)))
            all_results.append(results)
        
        return all_results
    
    def save_index(self, path: Optional[Path] = None):
        """
        保存索引和元数据
        
        Args:
            path: 保存路径，默认使用配置中的路径
        """
        if self.index is None:
            raise RuntimeError("没有可保存的索引")
        
        if path is None:
            path = self.config.data_source.faiss_index_path
        
        path = Path(path)
        path.mkdir(parents=True, exist_ok=True)
        
        # 保存 FAISS 索引
        index_file = path / "index.faiss"
        faiss.write_index(self.index, str(index_file))
        logger.info(f"FAISS 索引已保存到: {index_file}")
        
        # 保存元数据
        metadata = {
            "chunks": self.chunks,
            "chunk_id_map": self.chunk_id_map,
            "config": {
                "index_type": self.faiss_config.index_type,
                "dimension": self._dimension,
                "embedding_model": self.model_config.embedding_model
            }
        }
        
        metadata_file = path / "index.pkl"
        with open(metadata_file, 'wb') as f:
            pickle.dump(metadata, f)
        logger.info(f"元数据已保存到: {metadata_file}")
    
    def load_index(self, path: Optional[Path] = None):
        """
        加载索引和元数据
        
        Args:
            path: 加载路径
        """
        if path is None:
            path = self.config.data_source.faiss_index_path
        
        path = Path(path)
        
        # 加载 FAISS 索引
        index_file = path / "index.faiss"
        if not index_file.exists():
            raise FileNotFoundError(f"索引文件不存在: {index_file}")
        
        logger.info(f"正在加载 FAISS 索引文件: {index_file}")
        self.index = faiss.read_index(str(index_file))
        logger.info(f"已加载 FAISS 索引 (包含 {self.index.ntotal} 个向量)")
        
        # 转移到 GPU (如果可用)
        if self._use_gpu:
            logger.info("正在将索引转移到 GPU...")
            self.gpu_index = self._to_gpu(self.index)
            logger.info("GPU 索引转移完成")
        
        # 加载元数据
        metadata_file = path / "index.pkl"
        if metadata_file.exists():
            # 检查文件大小
            file_size_mb = metadata_file.stat().st_size / (1024 * 1024)
            logger.info(f"正在加载元数据文件: {metadata_file} ({file_size_mb:.1f} MB)")
            
            try:
                with open(metadata_file, 'rb') as f:
                    metadata = pickle.load(f)
                
                logger.info("元数据文件加载完成，正在解析...")
                
                # 检查是否为我们的格式 (dict) 还是 LangChain 格式 (tuple)
                if isinstance(metadata, dict):
                    # 我们的格式
                    self.chunks = metadata.get("chunks", [])
                    self.chunk_id_map = metadata.get("chunk_id_map", {})
                    config_info = metadata.get("config", {})
                    self._dimension = config_info.get("dimension", self._dimension)
                    logger.info(f"已加载 {len(self.chunks)} 个 chunks 的元数据")
                elif isinstance(metadata, tuple):
                    # LangChain 格式: (docstore, index_to_docstore_id)
                    logger.warning("检测到 LangChain 格式的元数据，尝试兼容加载...")
                    self._load_langchain_metadata(metadata)
                else:
                    logger.warning(f"未知的元数据格式: {type(metadata)}")
            except Exception as e:
                logger.warning(f"加载元数据失败: {e}，索引仍可使用但无文档内容")
        else:
            logger.warning(f"元数据文件不存在: {metadata_file}")
    
    def _load_langchain_metadata(self, metadata: tuple):
        """加载 LangChain 格式的元数据"""
        try:
            docstore, index_to_id = metadata
            
            # 尝试从 docstore 提取文档
            if hasattr(docstore, '_dict'):
                docs = docstore._dict
                self.chunks = []
                self.chunk_id_map = {}
                
                for idx, doc_id in index_to_id.items():
                    if doc_id in docs:
                        doc = docs[doc_id]
                        # LangChain Document 有 page_content 和 metadata 属性
                        content = getattr(doc, 'page_content', str(doc))
                        doc_metadata = getattr(doc, 'metadata', {})
                        
                        chunk = Chunk(
                            content=content,
                            chunk_type="rag",
                            source_doc_id=doc_id,
                            chunk_index=idx,
                            metadata=doc_metadata
                        )
                        self.chunks.append(chunk)
                        self.chunk_id_map[idx] = chunk.chunk_id
                
                logger.info(f"从 LangChain 格式加载了 {len(self.chunks)} 个文档")
            else:
                logger.warning("无法解析 LangChain docstore 结构")
        except Exception as e:
            logger.warning(f"解析 LangChain 元数据失败: {e}")
    
    def get_statistics(self) -> Dict:
        """获取索引统计信息"""
        if self.index is None:
            return {"status": "未初始化"}
        
        return {
            "total_vectors": self.index.ntotal,
            "dimension": self._dimension,
            "index_type": self.faiss_config.index_type,
            "total_chunks": len(self.chunks),
            "is_trained": getattr(self.index, 'is_trained', True),
            "gpu_enabled": self._use_gpu,
            "gpu_index_active": self.gpu_index is not None
        }


# ============================================================
# Cross-Encoder Reranker 类 (用于 RAG 幻觉抑制)
# ============================================================
class CrossEncoderReranker:
    """
    Cross-Encoder 重排序器
    
    用于对 FAISS 初步检索结果进行精排，提高检索精度
    Cross-Encoder 能更精确地区分语义相似但概念不同的文档
    (例如: O2ims vs F1, NGAP vs E1AP)
    """
    
    # 类级别缓存: 按模型名称缓存实例
    _instances: Dict[str, 'CrossEncoderReranker'] = {}
    
    def __new__(cls, model_name: str = "cross-encoder/ms-marco-MiniLM-L-6-v2"):
        """按模型名称缓存，避免重复加载同一模型"""
        if model_name not in cls._instances:
            instance = super().__new__(cls)
            instance._initialized = False
            cls._instances[model_name] = instance
        return cls._instances[model_name]
    
    def __init__(self, model_name: str = "cross-encoder/ms-marco-MiniLM-L-6-v2"):
        """
        初始化 Cross-Encoder Reranker
        
        Args:
            model_name: HuggingFace 模型名称
                推荐:
                - "cross-encoder/ms-marco-MiniLM-L-6-v2" (轻量级，23MB，速度快) [默认]
                - "BAAI/bge-reranker-base" (中等大小，278MB，精度高)
                - "BAAI/bge-reranker-large" (更高精度，560MB，更慢)
        """
        if getattr(self, '_initialized', False):
            return
            
        if CrossEncoder is None:
            raise ImportError(
                "CrossEncoder 需要 sentence-transformers 库。"
                "请运行: pip install sentence-transformers"
            )
        
        self.model_name = model_name
        self._model = None
        self._load_model()
        self._initialized = True
    
    def _load_model(self):
        """延迟加载模型"""
        if self._model is None:
            logger.info(f"加载 Cross-Encoder 模型: {self.model_name}")
            try:
                self._model = CrossEncoder(
                    self.model_name,
                    max_length=512,
                    device=None  # 自动选择 GPU/CPU
                )
                logger.info(f"Cross-Encoder 模型加载成功")
            except Exception as e:
                logger.error(f"Cross-Encoder 模型加载失败: {e}")
                raise
    
    def rerank(
        self,
        query: str,
        documents: List[Tuple[Any, float]],
        top_k: int = 3,
        min_score: float = 0.0
    ) -> List[Tuple[Any, float]]:
        """
        对文档进行重排序
        
        Args:
            query: 查询问题
            documents: FAISS 初步检索结果 [(Chunk, faiss_score), ...]
            top_k: 返回的文档数量
            min_score: 最低分数阈值 (Reranker 分数通常在 0-1 之间)
            
        Returns:
            重排序后的文档列表 [(Chunk, reranker_score), ...]
        """
        if not documents:
            return []
        
        # 准备 (query, document) 对
        pairs = [(query, doc.content) for doc, _ in documents]
        
        # Cross-Encoder 评分
        try:
            scores = self._model.predict(pairs, show_progress_bar=False)
            
            # 对于 BGE-Reranker，分数可能是负数，需要转换为概率
            # 使用 sigmoid 转换
            import numpy as np
            if hasattr(scores, '__iter__'):
                scores = np.array(scores)
                # Sigmoid 转换使分数在 0-1 之间
                scores = 1 / (1 + np.exp(-scores))
            
        except Exception as e:
            logger.error(f"Cross-Encoder 评分失败: {e}")
            # 回退到原始 FAISS 分数
            return documents[:top_k]
        
        # 组合原始 chunk 和新分数
        reranked = [
            (documents[i][0], float(scores[i]))
            for i in range(len(documents))
        ]
        
        # 按新分数排序 (降序)
        reranked.sort(key=lambda x: x[1], reverse=True)
        
        # 应用最低分数阈值过滤
        if min_score > 0:
            reranked = [(doc, score) for doc, score in reranked if score >= min_score]
        
        # 返回 top-k
        return reranked[:top_k]
    
    def get_score(self, query: str, document: str) -> float:
        """
        获取单个 query-document 对的相关性分数
        
        Args:
            query: 查询问题
            document: 文档内容
            
        Returns:
            相关性分数 (0-1)
        """
        try:
            score = self._model.predict([(query, document)], show_progress_bar=False)[0]
            # Sigmoid 转换
            import numpy as np
            return float(1 / (1 + np.exp(-score)))
        except Exception as e:
            logger.error(f"Cross-Encoder 单次评分失败: {e}")
            return 0.0


class RAGRetriever:
    """
    RAG 检索器封装
    
    支持两阶段检索:
    1. FAISS 初筛 (Bi-Encoder, 快速)
    2. Cross-Encoder 精排 (可选, 精确)
    """
    
    def __init__(
        self, 
        faiss_manager: FAISSManager,
        enable_reranker: bool = True,
        reranker_model: str = "BAAI/bge-reranker-base"
    ):
        """
        初始化 RAG 检索器
        
        Args:
            faiss_manager: FAISS 管理器实例
            enable_reranker: 是否启用 Cross-Encoder 重排序
            reranker_model: Reranker 模型名称
        """
        self.faiss_manager = faiss_manager
        self.enable_reranker = enable_reranker
        self.reranker: Optional[CrossEncoderReranker] = None
        
        # 从 faiss_manager 的配置获取参数
        self.faiss_config = faiss_manager.faiss_config
        
        # 懒加载 Reranker
        self._reranker_model = reranker_model
    
    def _get_reranker(self) -> Optional[CrossEncoderReranker]:
        """懒加载 Reranker"""
        if not self.enable_reranker:
            return None
        
        if self.reranker is None:
            try:
                self.reranker = CrossEncoderReranker(self._reranker_model)
            except Exception as e:
                logger.warning(f"Reranker 初始化失败，将使用纯 FAISS 检索: {e}")
                self.enable_reranker = False
                return None
        
        return self.reranker
    
    def retrieve(
        self, 
        query: str, 
        top_k: int = 3,
        use_reranker: Optional[bool] = None
    ) -> List[Dict]:
        """
        检索相关文档 (支持两阶段检索)
        
        Args:
            query: 查询问题
            top_k: 最终返回数量
            use_reranker: 是否使用 Reranker (None 则使用默认配置)
            
        Returns:
            检索结果列表，每个包含 content, score, metadata, chunk_id, reranked
        """
        # 决定是否使用 Reranker
        should_rerank = use_reranker if use_reranker is not None else self.enable_reranker
        
        if should_rerank:
            # 两阶段检索
            reranker = self._get_reranker()
            if reranker is not None:
                return self._retrieve_with_reranker(query, top_k, reranker)
        
        # 单阶段检索 (仅 FAISS)
        return self._retrieve_faiss_only(query, top_k)
    
    def _retrieve_faiss_only(self, query: str, top_k: int) -> List[Dict]:
        """纯 FAISS 检索"""
        results = self.faiss_manager.search(query, top_k)
        
        return [
            {
                "content": chunk.content,
                "score": score,
                "metadata": chunk.metadata,
                "chunk_id": chunk.chunk_id,
                "reranked": False
            }
            for chunk, score in results
        ]
    
    def _retrieve_with_reranker(
        self, 
        query: str, 
        top_k: int,
        reranker: CrossEncoderReranker
    ) -> List[Dict]:
        """
        两阶段检索: FAISS 初筛 + Cross-Encoder 精排
        
        流程:
        1. FAISS 返回 reranker_top_k 个候选 (默认 10)
        2. Cross-Encoder 对候选进行评分
        3. 按新分数排序，返回 top_k 个 (默认 3)
        """
        # 获取配置
        reranker_top_k = getattr(self.faiss_config, 'reranker_top_k', 10)
        reranker_min_score = getattr(self.faiss_config, 'reranker_min_score', 0.1)
        
        # 第一阶段: FAISS 初筛
        faiss_results = self.faiss_manager.search(query, reranker_top_k)
        
        if not faiss_results:
            return []
        
        logger.debug(f"FAISS 初筛返回 {len(faiss_results)} 个候选")
        
        # 第二阶段: Cross-Encoder 精排
        reranked_results = reranker.rerank(
            query=query,
            documents=faiss_results,
            top_k=top_k,
            min_score=reranker_min_score
        )
        
        logger.debug(f"Reranker 精排后返回 {len(reranked_results)} 个结果")
        
        return [
            {
                "content": chunk.content,
                "score": score,  # 这是 Reranker 分数
                "metadata": chunk.metadata,
                "chunk_id": chunk.chunk_id,
                "reranked": True
            }
            for chunk, score in reranked_results
        ]
    
    def format_context(self, query: str, top_k: int = 3) -> str:
        """
        检索并格式化为上下文字符串
        
        Args:
            query: 查询问题
            top_k: 返回数量
            
        Returns:
            格式化的上下文字符串
        """
        results = self.retrieve(query, top_k)
        
        if not results:
            return ""
        
        context_parts = []
        for i, result in enumerate(results, 1):
            source = result["metadata"].get("filename", "Unknown")
            rerank_indicator = " [Reranked]" if result.get("reranked") else ""
            context_parts.append(
                f"[Document {i}]{rerank_indicator} (Source: {source}, Score: {result['score']:.4f})\n{result['content']}"
            )
        
        return "\n\n---\n\n".join(context_parts)
    
    def compare_retrieval(self, query: str, top_k: int = 3) -> Dict:
        """
        比较 FAISS-only 和 Reranked 结果 (用于调试)
        
        Args:
            query: 查询问题
            top_k: 返回数量
            
        Returns:
            包含两种检索结果的字典
        """
        faiss_results = self._retrieve_faiss_only(query, top_k)
        
        reranker = self._get_reranker()
        if reranker:
            reranked_results = self._retrieve_with_reranker(query, top_k, reranker)
        else:
            reranked_results = []
        
        return {
            "query": query,
            "faiss_only": faiss_results,
            "reranked": reranked_results,
            "order_changed": [r["chunk_id"] for r in faiss_results] != [r["chunk_id"] for r in reranked_results]
        }
    
    def retrieve_batch(
        self,
        queries: List[str],
        top_k: int = 3,
        use_reranker: Optional[bool] = None,
        show_progress: bool = True
    ) -> List[List[Dict]]:
        """
        批量检索相关文档 (支持 Reranker)
        
        Args:
            queries: 查询问题列表
            top_k: 每个查询最终返回数量
            use_reranker: 是否使用 Reranker (None 则使用默认配置)
            show_progress: 是否显示进度条
            
        Returns:
            每个查询的检索结果列表
        """
        should_rerank = use_reranker if use_reranker is not None else self.enable_reranker
        
        if should_rerank:
            reranker = self._get_reranker()
            if reranker is not None:
                return self._retrieve_batch_with_reranker(queries, top_k, reranker, show_progress)
        
        # 纯 FAISS 批量检索
        return self._retrieve_batch_faiss_only(queries, top_k)
    
    def _retrieve_batch_faiss_only(
        self,
        queries: List[str],
        top_k: int
    ) -> List[List[Dict]]:
        """批量纯 FAISS 检索"""
        all_results = self.faiss_manager.search_batch(queries, top_k)
        
        return [
            [
                {
                    "content": chunk.content,
                    "score": score,
                    "metadata": chunk.metadata,
                    "chunk_id": chunk.chunk_id,
                    "reranked": False
                }
                for chunk, score in results
            ]
            for results in all_results
        ]
    
    def _retrieve_batch_with_reranker(
        self,
        queries: List[str],
        top_k: int,
        reranker: CrossEncoderReranker,
        show_progress: bool = True
    ) -> List[List[Dict]]:
        """
        批量两阶段检索: FAISS 初筛 + Cross-Encoder 精排
        
        流程:
        1. FAISS 批量返回 reranker_top_k 个候选
        2. 对每个查询，Cross-Encoder 进行精排
        3. 返回 top_k 个最相关结果
        """
        reranker_top_k = getattr(self.faiss_config, 'reranker_top_k', 10)
        reranker_min_score = getattr(self.faiss_config, 'reranker_min_score', 0.1)
        
        # 第一阶段: FAISS 批量初筛
        logger.info(f"FAISS 批量初筛 {len(queries)} 个查询, 每个取 Top-{reranker_top_k}")
        all_faiss_results = self.faiss_manager.search_batch(queries, reranker_top_k)
        
        # 第二阶段: Cross-Encoder 逐个精排
        all_reranked_results = []
        
        iterator = enumerate(zip(queries, all_faiss_results))
        if show_progress:
            try:
                from tqdm import tqdm
                iterator = tqdm(
                    list(iterator),
                    desc="Cross-Encoder 重排序",
                    unit="query"
                )
            except ImportError:
                pass
        
        for i, (query, faiss_results) in iterator:
            if not faiss_results:
                all_reranked_results.append([])
                continue
            
            # Cross-Encoder 精排
            reranked = reranker.rerank(
                query=query,
                documents=faiss_results,
                top_k=top_k,
                min_score=reranker_min_score
            )
            
            all_reranked_results.append([
                {
                    "content": chunk.content,
                    "score": score,
                    "metadata": chunk.metadata,
                    "chunk_id": chunk.chunk_id,
                    "reranked": True
                }
                for chunk, score in reranked
            ])
        
        logger.info(f"Cross-Encoder 重排序完成，处理了 {len(queries)} 个查询")
        return all_reranked_results


if __name__ == "__main__":
    # 测试 FAISS 管理器
    logging.basicConfig(level=logging.INFO)
    
    config = Config()
    manager = FAISSManager(config)
    
    # 检查是否有现有索引
    index_path = config.data_source.faiss_index_path
    if index_path and (index_path / "index.faiss").exists():
        print(f"发现现有索引: {index_path}")
        manager.load_index()
        print(f"索引统计: {manager.get_statistics()}")
        
        # 测试搜索
        test_query = "What is O-RAN architecture?"
        results = manager.search(test_query, top_k=3)
        print(f"\n查询: {test_query}")
        print(f"找到 {len(results)} 个结果")
        for chunk, score in results[:2]:
            print(f"  - Score: {score:.4f}, Source: {chunk.metadata.get('filename', 'N/A')}")
    else:
        print("未发现现有索引，需要先构建索引")

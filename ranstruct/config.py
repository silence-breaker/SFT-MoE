"""
RANSTRUCT 配置管理模块

管理所有框架配置，包括：
- Ollama 模型路径和名称
- 数据源路径
- 分块参数
- FAISS 配置
"""

import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional, List


@dataclass
class ModelConfig:
    """模型配置"""
    # Ollama 配置
    ollama_base_url: str = "http://localhost:11434"
    ollama_models_path: str = "D:/Ollama/Models"
    
    # 问题生成模型
    question_model: str = "mistral:latest"
    question_model_temperature: float = 0.7
    question_model_top_p: float = 0.9
    
    # 答案生成模型
    answer_model: str = "qwen2.5:1.5b"
    answer_model_temperature: float = 0.3
    answer_model_top_p: float = 0.9
    
    # 嵌入模型 (用于FAISS)
    embedding_model: str = "bge-small-en-v1.5"
    embedding_dimension: int = 384


@dataclass
class ChunkConfig:
    """数据分块配置"""
    # RAG Chunks - 用于检索
    rag_chunk_size: int = 1024
    rag_chunk_overlap: int = 200  # 增加重叠以保持上下文连贯
    rag_min_chunk_size: int = 200  # 最小 chunk 大小，过滤过短内容
    
    # LTG Chunks - 用于问题生成
    ltg_chunk_size: int = 4096
    ltg_chunk_overlap: int = 512  # 增加重叠
    
    # 代码专用配置
    code_chunk_size: int = 2048  # 代码文件使用更大的 chunk
    code_preserve_functions: bool = True  # 尽量保持函数完整性
    
    # 分块分隔符 (优先级调整)
    separators: List[str] = field(default_factory=lambda: [
        "\n\n\n",  # 三空行（章节分隔）
        "\n\n",     # 双空行（段落）
        "\n## ",    # Markdown 二级标题
        "\n### ",   # Markdown 三级标题
        "\n",       # 单行
        ". ",       # 句子
        " ",        # 词
        ""          # 字符
    ])
    
    # 代码分隔符
    code_separators: List[str] = field(default_factory=lambda: [
        "\n\n",            # 空行（函数间）
        "\nclass ",        # 类定义
        "\ndef ",          # Python 函数
        "\nvoid ",         # C/C++ void 函数
        "\nint ",          # C/C++ int 函数
        "\nstatic ",       # 静态函数
        "\n{",             # 代码块开始
        "\n",              # 单行
    ])
    
    # 低价值内容过滤开关
    filter_low_value_content: bool = True


@dataclass
class DataSourceConfig:
    """数据源配置"""
    base_path: Path = field(default_factory=lambda: Path(__file__).parent.parent / "datasource")
    
    # O-RAN 规范文档路径
    oran_spec_path: Optional[Path] = None
    
    # srsRAN 代码路径
    srsran_code_path: Optional[Path] = None
    
    # 代码集路径
    codeset_path: Optional[Path] = None
    
    # FAISS 索引路径
    faiss_index_path: Optional[Path] = None
    
    # 支持的文件扩展名
    spec_extensions: List[str] = field(default_factory=lambda: [".md", ".txt", ".rst"])
    code_extensions: List[str] = field(default_factory=lambda: [".cpp", ".h", ".hpp", ".c", ".cc"])
    
    def __post_init__(self):
        """初始化后处理"""
        if self.oran_spec_path is None:
            self.oran_spec_path = self.base_path / "ORAN_Specification"
        if self.srsran_code_path is None:
            self.srsran_code_path = self.base_path.parent / "srsRAN_Project"
        if self.codeset_path is None:
            self.codeset_path = self.base_path / "codeset"
        if self.faiss_index_path is None:
            self.faiss_index_path = self.base_path / "FAISS-v2.0"


@dataclass
class FAISSConfig:
    """FAISS 配置"""
    # 检索时返回的 top-k 结果
    top_k: int = 3
    
    # 检索置信度阈值 (Confidence Thresholding)
    # 如果最高分低于该阈值，丢弃该问题以避免幻觉
    min_retrieval_score: float = 0.35  # FAISS L2距离转换后的分数，越高越相关
    
    # 是否启用置信度阈值过滤
    enable_confidence_threshold: bool = True
    
    # ============================================================
    # Cross-Encoder Reranker 配置 (新增)
    # ============================================================
    # 是否启用 Reranker
    enable_reranker: bool = True
    
    # Reranker 模型名称 (支持 HuggingFace 模型)
    # 推荐: "BAAI/bge-reranker-base" 或 "cross-encoder/ms-marco-MiniLM-L-6-v2"
    # 注意: ms-marco-MiniLM 只有 23MB，下载更快，适合测试
    reranker_model: str = "cross-encoder/ms-marco-MiniLM-L-6-v2"
    
    # FAISS 初筛返回数量 (传给 Reranker 进行精排)
    reranker_top_k: int = 10
    
    # Reranker 最终返回数量
    reranker_final_top_k: int = 3
    
    # Reranker 最低分数阈值 (低于此分数的文档将被过滤)
    reranker_min_score: float = 0.1
    
    # 索引类型: "flat", "ivf", "hnsw"
    index_type: str = "flat"
    
    # IVF 参数
    nlist: int = 100  # 聚类数量
    nprobe: int = 10  # 搜索时探测的聚类数
    
    # HNSW 参数
    hnsw_m: int = 32
    hnsw_ef_construction: int = 200
    hnsw_ef_search: int = 100


@dataclass
class GenerationConfig:
    """生成配置"""
    # 每个 LTG chunk 生成的问题数量
    questions_per_chunk: int = 5
    
    # 最大重试次数
    max_retries: int = 3
    
    # 批处理大小
    batch_size: int = 10
    
    # 是否启用去重
    enable_deduplication: bool = True
    
    # 问题最小长度
    min_question_length: int = 10
    
    # 问题最大长度
    max_question_length: int = 500
    
    # 答案最小长度（降低以接受简洁但有效的答案）
    min_answer_length: int = 30
    
    # 答案最大长度
    max_answer_length: int = 3000


@dataclass
class OutputConfig:
    """输出配置"""
    output_dir: Path = field(default_factory=lambda: Path(__file__).parent.parent / "output")
    
    # 数据集文件名
    dataset_filename: str = "ranstruct_dataset.jsonl"
    
    # 中间结果保存
    save_intermediate: bool = True
    questions_filename: str = "generated_questions.jsonl"
    
    # 时间戳文件名（防止覆盖）
    use_timestamp_filename: bool = False
    
    # 日志配置
    log_level: str = "INFO"
    log_file: Optional[str] = "ranstruct.log"
    
    def __post_init__(self):
        """确保输出目录存在"""
        self.output_dir.mkdir(parents=True, exist_ok=True)


@dataclass
class Config:
    """RANSTRUCT 主配置类"""
    model: ModelConfig = field(default_factory=ModelConfig)
    chunk: ChunkConfig = field(default_factory=ChunkConfig)
    data_source: DataSourceConfig = field(default_factory=DataSourceConfig)
    faiss: FAISSConfig = field(default_factory=FAISSConfig)
    generation: GenerationConfig = field(default_factory=GenerationConfig)
    output: OutputConfig = field(default_factory=OutputConfig)
    
    # 全局设置
    random_seed: int = 42
    num_workers: int = 4
    device: str = "cuda"  # "cuda", "cpu", "mps"
    
    @classmethod
    def from_yaml(cls, yaml_path: str) -> "Config":
        """从 YAML 文件加载配置"""
        import yaml
        with open(yaml_path, 'r', encoding='utf-8') as f:
            config_dict = yaml.safe_load(f)
        return cls._from_dict(config_dict)
    
    @classmethod
    def _from_dict(cls, config_dict: dict) -> "Config":
        """从字典创建配置"""
        config = cls()
        
        if 'model' in config_dict:
            for k, v in config_dict['model'].items():
                setattr(config.model, k, v)
        
        if 'chunk' in config_dict:
            for k, v in config_dict['chunk'].items():
                setattr(config.chunk, k, v)
        
        if 'data_source' in config_dict:
            for k, v in config_dict['data_source'].items():
                if k.endswith('_path') and v is not None:
                    v = Path(v)
                setattr(config.data_source, k, v)
        
        if 'faiss' in config_dict:
            for k, v in config_dict['faiss'].items():
                setattr(config.faiss, k, v)
        
        if 'generation' in config_dict:
            for k, v in config_dict['generation'].items():
                setattr(config.generation, k, v)
        
        if 'output' in config_dict:
            for k, v in config_dict['output'].items():
                if k.endswith('_dir') and v is not None:
                    v = Path(v)
                setattr(config.output, k, v)
        
        # 全局设置
        for key in ['random_seed', 'num_workers', 'device']:
            if key in config_dict:
                setattr(config, key, config_dict[key])
        
        return config
    
    def to_dict(self) -> dict:
        """将配置转换为字典"""
        from dataclasses import asdict
        return asdict(self)
    
    def save_yaml(self, yaml_path: str):
        """保存配置到 YAML 文件"""
        import yaml
        config_dict = self.to_dict()
        
        # 转换 Path 对象为字符串
        def convert_paths(d):
            for k, v in d.items():
                if isinstance(v, Path):
                    d[k] = str(v)
                elif isinstance(v, dict):
                    convert_paths(v)
            return d
        
        config_dict = convert_paths(config_dict)
        
        with open(yaml_path, 'w', encoding='utf-8') as f:
            yaml.dump(config_dict, f, default_flow_style=False, allow_unicode=True)


# 默认配置实例
default_config = Config()


if __name__ == "__main__":
    # 测试配置
    config = Config()
    print(f"问题生成模型: {config.model.question_model}")
    print(f"答案生成模型: {config.model.answer_model}")
    print(f"RAG Chunk 大小: {config.chunk.rag_chunk_size}")
    print(f"LTG Chunk 大小: {config.chunk.ltg_chunk_size}")
    print(f"O-RAN 规范路径: {config.data_source.oran_spec_path}")
    print(f"FAISS Top-K: {config.faiss.top_k}")

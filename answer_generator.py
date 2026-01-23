"""
RANSTRUCT 答案生成模块

使用 Qwen-2.5-Instruct-1.5B 模型结合 RAG 生成答案：
- 检索相关 RAG Chunks
- 基于上下文生成准确答案
- 支持批量生成
- 支持增量保存和中断恢复
"""

import re
import json
import signal
import logging
from pathlib import Path
from typing import List, Dict, Optional, Tuple, Any
from dataclasses import dataclass, field

try:
    import ollama
except ImportError:
    ollama = None
    print("警告: ollama 未安装，请运行 pip install ollama")

from .config import Config
from .faiss_manager import FAISSManager, RAGRetriever
from .question_generator import GeneratedQuestion

logger = logging.getLogger(__name__)

# 全局变量用于信号处理
_shutdown_requested = False
_emergency_save_callback = None


def _signal_handler(signum, frame):
    """处理 Ctrl+C 信号，触发紧急保存"""
    global _shutdown_requested
    if _shutdown_requested:
        logger.warning("强制退出...")
        raise SystemExit(1)
    
    _shutdown_requested = True
    logger.warning("收到中断信号，正在保存进度...")
    
    if _emergency_save_callback:
        try:
            _emergency_save_callback()
            logger.info("进度已保存")
        except Exception as e:
            logger.error(f"保存失败: {e}")


# 注册信号处理器
signal.signal(signal.SIGINT, _signal_handler)
signal.signal(signal.SIGTERM, _signal_handler)


@dataclass
class QAPair:
    """问答对数据类"""
    question: str
    answer: str
    source_chunk_id: str
    retrieved_chunks: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def to_dict(self) -> Dict:
        """转换为字典"""
        return {
            "question": self.question,
            "answer": self.answer,
            "source_chunk_id": self.source_chunk_id,
            "retrieved_chunks": self.retrieved_chunks,
            "metadata": self.metadata
        }
    
    def to_training_format(self) -> Dict:
        """转换为训练格式（指令微调格式）"""
        return {
            "instruction": self.question,
            "input": "",
            "output": self.answer
        }
    
    def to_conversation_format(self) -> Dict:
        """转换为对话格式"""
        return {
            "conversations": [
                {"role": "user", "content": self.question},
                {"role": "assistant", "content": self.answer}
            ]
        }


class AnswerGenerator:
    """答案生成器
    
    使用 Qwen-2.5-Instruct 模型结合 RAG 检索生成答案。
    """
    
    # 答案生成提示模板
    SYSTEM_PROMPT = """You are an expert assistant specializing in O-RAN (Open Radio Access Network) and telecommunications.
Your task is to provide accurate, comprehensive answers based on the provided context documents.

Guidelines:
1. Base your answer ONLY on the provided context
2. If the context doesn't contain enough information, acknowledge this limitation
3. Be technically accurate and use proper O-RAN terminology
4. Provide clear explanations suitable for technical professionals
5. Include specific details, numbers, or specifications when available in the context"""

    ANSWER_PROMPT_TEMPLATE = """Answer the following question based on the provided context documents.

Context Documents:
{context}

Question: {question}

Instructions:
- Provide a comprehensive and accurate answer based on the context
- Use technical terminology appropriately
- If the context is insufficient, indicate what information is missing
- Be concise but thorough

Answer:"""

    CODE_ANSWER_PROMPT_TEMPLATE = """Answer the following question about the code based on the provided context.

Code Context:
{context}

Question: {question}

Instructions:
- Explain the code's functionality, design, or implementation as asked
- Reference specific functions, classes, or code patterns when relevant
- Be technically precise and clear
- If the context is insufficient, indicate what additional code would be needed

Answer:"""

    def __init__(self, config: Config, faiss_manager: Optional[FAISSManager] = None):
        """
        初始化答案生成器
        
        Args:
            config: RANSTRUCT 配置
            faiss_manager: FAISS 管理器实例（可选）
        """
        if ollama is None:
            raise ImportError("请安装 ollama: pip install ollama")
        
        self.config = config
        self.model_config = config.model
        self.generation_config = config.generation
        self.faiss_config = config.faiss
        
        self.model_name = self.model_config.answer_model
        self.temperature = self.model_config.answer_model_temperature
        self.top_p = self.model_config.answer_model_top_p
        
        # RAG 检索器 (支持 Cross-Encoder Reranker)
        self.faiss_manager = faiss_manager
        if faiss_manager:
            self.retriever = RAGRetriever(
                faiss_manager,
                enable_reranker=getattr(self.faiss_config, 'enable_reranker', True),
                reranker_model=getattr(self.faiss_config, 'reranker_model', 'BAAI/bge-reranker-base')
            )
        else:
            self.retriever = None
        
        logger.info(f"答案生成器初始化完成，使用模型: {self.model_name}")
        if self.retriever and getattr(self.faiss_config, 'enable_reranker', True):
            logger.info(f"已启用 Cross-Encoder Reranker: {getattr(self.faiss_config, 'reranker_model', 'BAAI/bge-reranker-base')}")
    
    def set_faiss_manager(self, faiss_manager: FAISSManager):
        """设置 FAISS 管理器"""
        self.faiss_manager = faiss_manager
        self.retriever = RAGRetriever(
            faiss_manager,
            enable_reranker=getattr(self.faiss_config, 'enable_reranker', True),
            reranker_model=getattr(self.faiss_config, 'reranker_model', 'BAAI/bge-reranker-base')
        )
    
    def _call_llm(self, prompt: str, system_prompt: str = None) -> str:
        """调用 LLM 生成响应"""
        messages = []
        
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        
        messages.append({"role": "user", "content": prompt})
        
        try:
            response = ollama.chat(
                model=self.model_name,
                messages=messages,
                options={
                    "temperature": self.temperature,
                    "top_p": self.top_p,
                }
            )
            return response['message']['content']
        except Exception as e:
            logger.error(f"LLM 调用失败: {e}")
            raise
    
    def _validate_answer(self, answer: str) -> bool:
        """验证答案是否有效"""
        # 检查长度
        if len(answer) < self.generation_config.min_answer_length:
            logger.debug(f"答案太短 ({len(answer)} < {self.generation_config.min_answer_length})")
            return False
        if len(answer) > self.generation_config.max_answer_length:
            logger.debug(f"答案太长 ({len(answer)} > {self.generation_config.max_answer_length})")
            return False
        
        # 检查是否包含拒绝回答的内容
        invalid_patterns = [
            "i don't know",
            "i cannot",
            "i'm not sure",
            "insufficient information",
            "no relevant",
            "i'm unable to",
            "cannot provide",
            "not enough information",
            "context does not contain",
            "context doesn't contain",
        ]
        
        answer_lower = answer.lower()
        for pattern in invalid_patterns:
            # 只有当答案很短且包含这些模式时才拒绝
            if pattern in answer_lower and len(answer) < 150:
                logger.debug(f"答案包含无效模式: {pattern}")
                return False
        
        # 检查答案是否只是重复问题
        if answer_lower.strip().endswith('?'):
            logger.debug("答案以问号结尾，可能是重复问题")
            return False
        
        return True
    
    def _format_context(self, retrieved_docs: List[Dict]) -> Tuple[str, List[str]]:
        """格式化检索到的文档为上下文"""
        if not retrieved_docs:
            return "", []
        
        context_parts = []
        chunk_ids = []
        
        for i, doc in enumerate(retrieved_docs, 1):
            source = doc.get("metadata", {}).get("filename", "Unknown")
            content = doc.get("content", "")
            chunk_id = doc.get("chunk_id", "")
            
            context_parts.append(f"[Document {i}] (Source: {source})\n{content}")
            chunk_ids.append(chunk_id)
        
        return "\n\n---\n\n".join(context_parts), chunk_ids
    
    def _clean_question(self, question_text: str) -> str:
        """清洗问题文本，移除格式错误"""
        import re
        
        # 移除常见的JSON格式残留
        # 例如: 'Question": "What is...' -> 'What is...'
        json_prefixes = [
            r'^["\']?Question["\']?\s*[:\"]+ *["\']?',  # Question": "...
            r'^["\']?Q["\']?\s*[:\"]+ *["\']?',  # Q": "...
            r'^\{\s*["\']?question["\']?\s*[:\"]+ *["\']?',  # {"question": "...
        ]
        
        cleaned = question_text.strip()
        for pattern in json_prefixes:
            cleaned = re.sub(pattern, '', cleaned, flags=re.IGNORECASE)
        
        # 移除尾部JSON格式残留
        json_suffixes = [
            r'["\']?\s*,?\s*\}?\s*$',  # ", } 等
            r'\s*,\s*$',  # 尾部逗号
        ]
        for pattern in json_suffixes:
            cleaned = re.sub(pattern, '', cleaned)
        
        # 移除首尾引号
        cleaned = cleaned.strip().strip('"\'')
        
        # 移除重复问号
        cleaned = re.sub(r'\?+', '?', cleaned)
        
        # 移除尾部的 ",?" 组合
        cleaned = re.sub(r'[,;]+\?$', '?', cleaned)
        
        # 确保以问号结尾
        if cleaned and not cleaned.endswith('?'):
            cleaned += '?'
            
        # 首字母大写
        if cleaned:
            cleaned = cleaned[0].upper() + cleaned[1:]
        
        return cleaned
    
    def generate_answer(
        self, 
        question: GeneratedQuestion,
        top_k: Optional[int] = None
    ) -> Optional[QAPair]:
        """
        为单个问题生成答案
        
        Args:
            question: 生成的问题对象
            top_k: 检索的文档数量
            
        Returns:
            问答对，如果生成失败返回 None
        """
        if self.retriever is None:
            raise RuntimeError("未设置 FAISS 管理器，请先调用 set_faiss_manager")
        
        if top_k is None:
            top_k = self.faiss_config.top_k
        
        # 清洗问题文本
        cleaned_question = self._clean_question(question.question)
        
        # 验证清洗后的问题是否有效
        if len(cleaned_question) < 10 or cleaned_question.lower().startswith('question'):
            logger.warning(f"问题清洗后无效: {question.question[:50]}...")
            return None
        
        # 检索相关文档
        retrieved_docs = self.retriever.retrieve(cleaned_question, top_k)
        
        if not retrieved_docs:
            logger.warning(f"未找到相关文档: {question.question[:50]}...")
            return None
        
        # 格式化上下文
        context, chunk_ids = self._format_context(retrieved_docs)
        
        # 选择提示模板
        is_code = question.metadata.get("source_type") in ["srsran_code", "codeset"]
        
        if is_code:
            prompt = self.CODE_ANSWER_PROMPT_TEMPLATE.format(
                context=context,
                question=cleaned_question
            )
        else:
            prompt = self.ANSWER_PROMPT_TEMPLATE.format(
                context=context,
                question=cleaned_question
            )
        
        # 重试机制
        for attempt in range(self.generation_config.max_retries):
            try:
                answer = self._call_llm(prompt, self.SYSTEM_PROMPT)
                answer = answer.strip()
                
                if self._validate_answer(answer):
                    return QAPair(
                        question=cleaned_question,  # 使用清洗后的问题
                        answer=answer,
                        source_chunk_id=question.source_chunk_id,
                        retrieved_chunks=chunk_ids,
                        metadata={
                            **question.metadata,
                            "retrieval_scores": [doc.get("score", 0) for doc in retrieved_docs]
                        }
                    )
                    
            except Exception as e:
                logger.warning(f"生成答案失败 (尝试 {attempt + 1}/{self.generation_config.max_retries}): {e}")
        
        logger.warning(f"无法为问题生成有效答案: {question.question[:50]}...")
        return None
    
    def _warmup_retriever(self):
        """预热检索器（提前加载嵌入模型）"""
        if self.faiss_manager is not None:
            self.faiss_manager.initialize_embedding_generator()
            # 做一次空查询来预热模型
            try:
                self.faiss_manager.embedding_generator.encode_single("warmup query")
                logger.debug("检索器预热完成")
            except Exception as e:
                logger.warning(f"检索器预热失败: {e}")
    
    def generate_batch(
        self, 
        questions: List[GeneratedQuestion],
        top_k: Optional[int] = None,
        save_interval: int = 50,
        output_file: Optional[str] = None
    ) -> List[QAPair]:
        """
        批量生成答案（优化版：批量检索 + 增量保存 + 中断恢复）
        
        Args:
            questions: 问题列表
            top_k: 检索的文档数量
            save_interval: 每处理多少个问题保存一次（默认50）
            output_file: 增量保存的输出文件路径
            
        Returns:
            问答对列表
        """
        global _shutdown_requested, _emergency_save_callback
        _shutdown_requested = False
        
        if self.retriever is None:
            raise RuntimeError("未设置 FAISS 管理器，请先调用 set_faiss_manager")
        
        if top_k is None:
            top_k = self.faiss_config.top_k
        
        # 设置默认输出文件
        if output_file is None:
            output_file = Path(self.config.output.output_dir) / "ranstruct_dataset_incremental.jsonl"
        output_file = Path(output_file)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        qa_pairs = []
        failed_count = 0
        
        # 定义保存函数
        def save_progress():
            if qa_pairs:
                with open(output_file, 'w', encoding='utf-8') as f:
                    for qa in qa_pairs:
                        f.write(json.dumps(qa.to_dict(), ensure_ascii=False) + '\n')
                logger.info(f"已保存 {len(qa_pairs)} 个问答对到 {output_file}")
        
        # 注册紧急保存回调
        _emergency_save_callback = save_progress
        
        logger.info(f"开始为 {len(questions)} 个问题生成答案...")
        logger.info(f"增量保存间隔: 每 {save_interval} 个问题")
        logger.info(f"输出文件: {output_file}")
        
        # 1. 预热检索器
        self._warmup_retriever()
        
        # 2. 预处理：清洗所有问题并过滤无效问题
        valid_questions = []
        cleaned_questions = []
        for question in questions:
            cleaned = self._clean_question(question.question)
            if len(cleaned) >= 10 and not cleaned.lower().startswith('question'):
                valid_questions.append(question)
                cleaned_questions.append(cleaned)
            else:
                logger.warning(f"问题清洗后无效: {question.question[:50]}...")
                failed_count += 1
        
        if not valid_questions:
            logger.warning("没有有效的问题需要处理")
            return []
        
        logger.info(f"有效问题数量: {len(valid_questions)}/{len(questions)}")
        
        # 3. 批量检索所有问题的相关文档
        logger.info("批量检索相关文档...")
        all_retrieved = self.faiss_manager.search_batch(cleaned_questions, top_k)
        logger.info("批量检索完成")
        
        # 4. 逐个生成答案
        for i, (question, cleaned_q, retrieved_results) in enumerate(
            zip(valid_questions, cleaned_questions, all_retrieved)
        ):
            # 检查是否收到中断信号
            if _shutdown_requested:
                logger.warning(f"收到中断信号，在第 {i} 个问题处停止")
                break
            
            try:
                if not retrieved_results:
                    logger.warning(f"未找到相关文档: {cleaned_q[:50]}...")
                    failed_count += 1
                    continue
                
                # 转换检索结果格式
                retrieved_docs = [
                    {
                        "content": chunk.content,
                        "score": score,
                        "metadata": chunk.metadata,
                        "chunk_id": chunk.chunk_id
                    }
                    for chunk, score in retrieved_results
                ]
                
                # 格式化上下文
                context, chunk_ids = self._format_context(retrieved_docs)
                
                # 选择提示模板
                is_code = question.metadata.get("source_type") in ["srsran_code", "codeset"]
                
                if is_code:
                    prompt = self.CODE_ANSWER_PROMPT_TEMPLATE.format(
                        context=context,
                        question=cleaned_q
                    )
                else:
                    prompt = self.ANSWER_PROMPT_TEMPLATE.format(
                        context=context,
                        question=cleaned_q
                    )
                
                # 生成答案（带重试）
                qa_pair = None
                for attempt in range(self.generation_config.max_retries):
                    try:
                        answer = self._call_llm(prompt, self.SYSTEM_PROMPT)
                        answer = answer.strip()
                        
                        if self._validate_answer(answer):
                            qa_pair = QAPair(
                                question=cleaned_q,
                                answer=answer,
                                source_chunk_id=question.source_chunk_id,
                                retrieved_chunks=chunk_ids,
                                metadata={
                                    **question.metadata,
                                    "retrieval_scores": [doc.get("score", 0) for doc in retrieved_docs]
                                }
                            )
                            break
                    except Exception as e:
                        logger.warning(f"生成答案失败 (尝试 {attempt + 1}): {e}")
                
                if qa_pair:
                    qa_pairs.append(qa_pair)
                else:
                    logger.warning(f"无法为问题生成有效答案: {cleaned_q[:50]}...")
                    failed_count += 1
                
                # 进度日志
                if (i + 1) % 10 == 0:
                    logger.info(
                        f"已处理 {i + 1}/{len(valid_questions)} 个问题，"
                        f"成功: {len(qa_pairs)}，失败: {failed_count}"
                    )
                
                # 增量保存
                if (i + 1) % save_interval == 0:
                    save_progress()
                    
            except Exception as e:
                logger.error(f"处理问题时出错: {e}")
                failed_count += 1
                continue
        
        # 最终保存
        save_progress()
        
        logger.info(f"答案生成完成，成功: {len(qa_pairs)}，失败: {failed_count}")
        return qa_pairs


class DatasetBuilder:
    """数据集构建器"""
    
    def __init__(self, config: Config):
        """
        初始化数据集构建器
        
        Args:
            config: RANSTRUCT 配置
        """
        self.config = config
        self.output_config = config.output
    
    def save_dataset(
        self, 
        qa_pairs: List[QAPair], 
        format: str = "jsonl",
        filepath: Optional[str] = None
    ):
        """
        保存数据集
        
        Args:
            qa_pairs: 问答对列表
            format: 输出格式 ("jsonl", "json", "training", "conversation")
            filepath: 输出文件路径
        """
        if filepath is None:
            filepath = self.output_config.output_dir / self.output_config.dataset_filename
        
        filepath = str(filepath)
        
        if format == "jsonl":
            self._save_jsonl(qa_pairs, filepath)
        elif format == "json":
            self._save_json(qa_pairs, filepath)
        elif format == "training":
            self._save_training_format(qa_pairs, filepath)
        elif format == "conversation":
            self._save_conversation_format(qa_pairs, filepath)
        else:
            raise ValueError(f"不支持的格式: {format}")
        
        logger.info(f"数据集已保存到 {filepath}，共 {len(qa_pairs)} 条记录")
    
    def _save_jsonl(self, qa_pairs: List[QAPair], filepath: str):
        """保存为 JSONL 格式"""
        with open(filepath, 'w', encoding='utf-8') as f:
            for qa in qa_pairs:
                f.write(json.dumps(qa.to_dict(), ensure_ascii=False) + '\n')
    
    def _save_json(self, qa_pairs: List[QAPair], filepath: str):
        """保存为 JSON 格式"""
        data = [qa.to_dict() for qa in qa_pairs]
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    def _save_training_format(self, qa_pairs: List[QAPair], filepath: str):
        """保存为训练格式（指令微调）"""
        with open(filepath, 'w', encoding='utf-8') as f:
            for qa in qa_pairs:
                f.write(json.dumps(qa.to_training_format(), ensure_ascii=False) + '\n')
    
    def _save_conversation_format(self, qa_pairs: List[QAPair], filepath: str):
        """保存为对话格式"""
        with open(filepath, 'w', encoding='utf-8') as f:
            for qa in qa_pairs:
                f.write(json.dumps(qa.to_conversation_format(), ensure_ascii=False) + '\n')
    
    @staticmethod
    def load_dataset(filepath: str) -> List[QAPair]:
        """加载数据集"""
        qa_pairs = []
        
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    data = json.loads(line)
                    qa = QAPair(
                        question=data["question"],
                        answer=data["answer"],
                        source_chunk_id=data.get("source_chunk_id", ""),
                        retrieved_chunks=data.get("retrieved_chunks", []),
                        metadata=data.get("metadata", {})
                    )
                    qa_pairs.append(qa)
        
        logger.info(f"从 {filepath} 加载了 {len(qa_pairs)} 条记录")
        return qa_pairs
    
    def get_statistics(self, qa_pairs: List[QAPair]) -> Dict:
        """获取数据集统计信息"""
        if not qa_pairs:
            return {"count": 0}
        
        question_lengths = [len(qa.question) for qa in qa_pairs]
        answer_lengths = [len(qa.answer) for qa in qa_pairs]
        
        return {
            "count": len(qa_pairs),
            "question_stats": {
                "min_length": min(question_lengths),
                "max_length": max(question_lengths),
                "avg_length": sum(question_lengths) / len(question_lengths)
            },
            "answer_stats": {
                "min_length": min(answer_lengths),
                "max_length": max(answer_lengths),
                "avg_length": sum(answer_lengths) / len(answer_lengths)
            },
            "sources": {
                qa.source_chunk_id: qa.metadata.get("source_file")
                for qa in qa_pairs[:10]  # 只显示前10个
            }
        }


if __name__ == "__main__":
    # 测试答案生成器
    logging.basicConfig(level=logging.INFO)
    
    config = Config()
    
    # 需要先初始化 FAISS 管理器
    faiss_manager = FAISSManager(config)
    
    # 检查是否有现有索引
    index_path = config.data_source.faiss_index_path
    if index_path and (index_path / "index.faiss").exists():
        faiss_manager.load_index()
        
        generator = AnswerGenerator(config, faiss_manager)
        
        # 创建测试问题
        test_question = GeneratedQuestion(
            question="What are the main components of O-RAN architecture?",
            source_chunk_id="test_chunk",
            metadata={"source_type": "oran_specification"}
        )
        
        print("正在生成答案...")
        qa_pair = generator.generate_answer(test_question)
        
        if qa_pair:
            print(f"\n问题: {qa_pair.question}")
            print(f"答案: {qa_pair.answer[:500]}...")
        else:
            print("未能生成答案")
    else:
        print("未发现 FAISS 索引，请先构建索引")

"""
RANSTRUCT 主管道模块

整合所有步骤的完整流程：
1. 数据加载与处理
2. FAISS 索引构建
3. 问题生成
4. 答案生成
5. 数据集输出
6. 质量后处理与清洗
"""

import logging
import time
from pathlib import Path
from typing import List, Dict, Optional, Any
from dataclasses import dataclass, field

from .config import Config
from .data_processor import DataProcessor, Document, Chunk
from .faiss_manager import FAISSManager
from .question_generator import QuestionGenerator, GeneratedQuestion
from .answer_generator import AnswerGenerator, QAPair, DatasetBuilder
from .post_processor import PostProcessor, QualityIssue

logger = logging.getLogger(__name__)


@dataclass
class PipelineStatistics:
    """管道执行统计"""
    start_time: float = 0
    end_time: float = 0
    
    # 数据统计
    total_documents: int = 0
    total_rag_chunks: int = 0
    total_ltg_chunks: int = 0
    
    # 生成统计
    total_questions_generated: int = 0
    total_answers_generated: int = 0
    failed_questions: int = 0
    failed_answers: int = 0
    
    # 后处理统计
    post_process_clean: int = 0
    post_process_fixed: int = 0
    post_process_discarded: int = 0
    
    # 各阶段耗时
    data_loading_time: float = 0
    faiss_building_time: float = 0
    question_generation_time: float = 0
    answer_generation_time: float = 0
    post_process_time: float = 0
    
    @property
    def total_time(self) -> float:
        return self.end_time - self.start_time
    
    def to_dict(self) -> Dict:
        return {
            "total_time_seconds": self.total_time,
            "total_documents": self.total_documents,
            "total_rag_chunks": self.total_rag_chunks,
            "total_ltg_chunks": self.total_ltg_chunks,
            "total_questions": self.total_questions_generated,
            "total_qa_pairs": self.total_answers_generated,
            "success_rate": self.total_answers_generated / max(self.total_questions_generated, 1),
            "post_process": {
                "clean": self.post_process_clean,
                "fixed": self.post_process_fixed,
                "discarded": self.post_process_discarded,
            },
            "phase_times": {
                "data_loading": self.data_loading_time,
                "faiss_building": self.faiss_building_time,
                "question_generation": self.question_generation_time,
                "answer_generation": self.answer_generation_time,
                "post_process": self.post_process_time,
            }
        }


class RANSTRUCTPipeline:
    """RANSTRUCT 数据集生成管道
    
    完整的端到端流程，包括：
    1. 数据加载与处理
    2. FAISS 索引构建
    3. 问题生成
    4. 答案生成
    5. 数据集输出
    """
    
    def __init__(self, config: Optional[Config] = None):
        """
        初始化管道
        
        Args:
            config: RANSTRUCT 配置，如果为 None 则使用默认配置
        """
        self.config = config or Config()
        
        # 初始化各模块
        self.data_processor = DataProcessor(self.config)
        self.faiss_manager = FAISSManager(self.config)
        self.question_generator: Optional[QuestionGenerator] = None
        self.answer_generator: Optional[AnswerGenerator] = None
        self.dataset_builder = DatasetBuilder(self.config)
        
        # 中间结果缓存
        self._documents: List[Document] = []
        self._rag_chunks: List[Chunk] = []
        self._ltg_chunks: List[Chunk] = []
        self._questions: List[GeneratedQuestion] = []
        self._qa_pairs: List[QAPair] = []
        
        # 统计信息
        self.stats = PipelineStatistics()
        
        # 设置日志
        self._setup_logging()
        
        logger.info("RANSTRUCT 管道初始化完成")
    
    def _setup_logging(self):
        """设置日志"""
        log_level = getattr(logging, self.config.output.log_level.upper(), logging.INFO)
        logging.basicConfig(
            level=log_level,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.StreamHandler(),
            ]
        )
        
        # 如果配置了日志文件
        if self.config.output.log_file:
            log_path = self.config.output.output_dir / self.config.output.log_file
            file_handler = logging.FileHandler(log_path, encoding='utf-8')
            file_handler.setFormatter(
                logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            )
            logging.getLogger().addHandler(file_handler)
    
    def _get_output_filename(self, base_filename: str) -> Path:
        """
        获取输出文件名，如果启用时间戳则添加时间戳后缀
        
        Args:
            base_filename: 基础文件名，如 "generated_questions.jsonl"
            
        Returns:
            完整的输出文件路径
        """
        from datetime import datetime
        
        if self.config.output.use_timestamp_filename:
            # 添加时间戳
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            name, ext = base_filename.rsplit('.', 1) if '.' in base_filename else (base_filename, '')
            timestamped_filename = f"{name}_{timestamp}.{ext}" if ext else f"{name}_{timestamp}"
            return self.config.output.output_dir / timestamped_filename
        else:
            return self.config.output.output_dir / base_filename
    
    def step1_load_data(self) -> Dict:
        """
        步骤1: 数据加载与处理
        
        加载 O-RAN 规范和 srsRAN 代码，创建 RAG 和 LTG chunks。
        
        Returns:
            数据统计信息
        """
        logger.info("=" * 50)
        logger.info("步骤 1: 数据加载与处理")
        logger.info("=" * 50)
        
        start_time = time.time()
        
        # 加载数据
        self._rag_chunks, self._ltg_chunks = self.data_processor.process_all()
        
        # 统计
        self.stats.total_rag_chunks = len(self._rag_chunks)
        self.stats.total_ltg_chunks = len(self._ltg_chunks)
        self.stats.data_loading_time = time.time() - start_time
        
        result = {
            "rag_chunks": len(self._rag_chunks),
            "ltg_chunks": len(self._ltg_chunks),
            "time_seconds": self.stats.data_loading_time
        }
        
        logger.info(f"数据加载完成: RAG Chunks={result['rag_chunks']}, LTG Chunks={result['ltg_chunks']}")
        logger.info(f"耗时: {result['time_seconds']:.2f} 秒")
        
        return result
    
    def step2_build_faiss(self, use_existing: bool = True) -> Dict:
        """
        步骤2: 构建 FAISS 索引
        
        Args:
            use_existing: 如果存在已有索引，是否直接使用
            
        Returns:
            索引统计信息
        """
        logger.info("=" * 50)
        logger.info("步骤 2: 构建 FAISS 索引")
        logger.info("=" * 50)
        
        start_time = time.time()
        
        index_path = self.config.data_source.faiss_index_path
        index_exists = index_path and (index_path / "index.faiss").exists()
        
        if use_existing and index_exists:
            logger.info("发现已有索引，正在加载...")
            self.faiss_manager.load_index()
        else:
            if not self._rag_chunks:
                logger.warning("没有 RAG chunks，请先执行步骤 1")
                return {"status": "error", "message": "No RAG chunks available"}
            
            logger.info("正在构建新索引...")
            self.faiss_manager.build_index(self._rag_chunks)
            
            # 保存索引
            self.faiss_manager.save_index()
        
        self.stats.faiss_building_time = time.time() - start_time
        
        result = self.faiss_manager.get_statistics()
        result["time_seconds"] = self.stats.faiss_building_time
        
        logger.info(f"FAISS 索引就绪: {result['total_vectors']} 个向量")
        logger.info(f"耗时: {result['time_seconds']:.2f} 秒")
        
        return result
    
    def step3_generate_questions(
        self, 
        max_chunks: Optional[int] = None,
        questions_per_chunk: Optional[int] = None,
        shard_id: Optional[int] = None,
        num_shards: Optional[int] = None
    ) -> Dict:
        """
        步骤3: 生成问题
        
        Args:
            max_chunks: 最大处理的 LTG chunks 数量
            questions_per_chunk: 每个 chunk 生成的问题数
            shard_id: 当前分片 ID (0 ~ num_shards-1)
            num_shards: 总分片数
            
        Returns:
            问题生成统计信息
        """
        logger.info("=" * 50)
        logger.info("步骤 3: 生成问题")
        logger.info("=" * 50)
        
        start_time = time.time()
        
        if not self._ltg_chunks:
            logger.warning("没有 LTG chunks，请先执行步骤 1")
            return {"status": "error", "message": "No LTG chunks available"}
        
        # 初始化问题生成器
        if self.question_generator is None:
            self.question_generator = QuestionGenerator(self.config)
        
        # 选择要处理的 chunks
        chunks_to_process = self._ltg_chunks
        
        # 应用分片逻辑
        if shard_id is not None and num_shards is not None:
            total_chunks = len(chunks_to_process)
            chunk_size = total_chunks // num_shards
            start_idx = shard_id * chunk_size
            end_idx = start_idx + chunk_size if shard_id < num_shards - 1 else total_chunks
            
            chunks_to_process = chunks_to_process[start_idx:end_idx]
            logger.info(f"应用分片 {shard_id}/{num_shards}: 处理 chunks {start_idx} 到 {end_idx} (共 {len(chunks_to_process)}/{total_chunks})")

        if max_chunks:
            chunks_to_process = chunks_to_process[:max_chunks]
        
        # 生成问题
        self._questions = self.question_generator.generate_batch(
            chunks_to_process,
            num_questions_per_chunk=questions_per_chunk
        )
        
        self.stats.total_questions_generated = len(self._questions)
        self.stats.question_generation_time = time.time() - start_time
        
        # 保存中间结果
        if self.config.output.save_intermediate:
            base_name = self.config.output.questions_filename
            if shard_id is not None:
                name, ext = base_name.rsplit('.', 1) if '.' in base_name else (base_name, '')
                base_name = f"{name}_part{shard_id}.{ext}" if ext else f"{name}_part{shard_id}"
                
            questions_file = self._get_output_filename(base_name)
            self.question_generator.save_questions(self._questions, str(questions_file))
        
        result = {
            "chunks_processed": len(chunks_to_process),
            "questions_generated": len(self._questions),
            "time_seconds": self.stats.question_generation_time
        }
        
        logger.info(f"问题生成完成: {result['questions_generated']} 个问题")
        logger.info(f"耗时: {result['time_seconds']:.2f} 秒")
        
        return result
    
    def step4_generate_answers(self, top_k: Optional[int] = None) -> Dict:
        """
        步骤4: 生成答案
        
        Args:
            top_k: RAG 检索返回的文档数量
            
        Returns:
            答案生成统计信息
        """
        logger.info("=" * 50)
        logger.info("步骤 4: 生成答案")
        logger.info("=" * 50)
        
        start_time = time.time()
        
        if not self._questions:
            logger.warning("没有问题，请先执行步骤 3")
            return {"status": "error", "message": "No questions available"}
        
        if self.faiss_manager.index is None:
            logger.warning("FAISS 索引未就绪，请先执行步骤 2")
            return {"status": "error", "message": "FAISS index not ready"}
        
        # 初始化答案生成器
        if self.answer_generator is None:
            self.answer_generator = AnswerGenerator(self.config, self.faiss_manager)
        else:
            self.answer_generator.set_faiss_manager(self.faiss_manager)
        
        # 生成答案
        self._qa_pairs = self.answer_generator.generate_batch(self._questions, top_k)
        
        self.stats.total_answers_generated = len(self._qa_pairs)
        self.stats.failed_answers = len(self._questions) - len(self._qa_pairs)
        self.stats.answer_generation_time = time.time() - start_time
        
        result = {
            "questions_processed": len(self._questions),
            "qa_pairs_generated": len(self._qa_pairs),
            "failed": self.stats.failed_answers,
            "success_rate": len(self._qa_pairs) / max(len(self._questions), 1),
            "time_seconds": self.stats.answer_generation_time
        }
        
        logger.info(f"答案生成完成: {result['qa_pairs_generated']} 对问答")
        logger.info(f"成功率: {result['success_rate']:.2%}")
        logger.info(f"耗时: {result['time_seconds']:.2f} 秒")
        
        return result
    
    def step5_save_dataset(
        self, 
        format: str = "jsonl",
        filepath: Optional[str] = None
    ) -> Dict:
        """
        步骤5: 保存数据集
        
        Args:
            format: 输出格式 ("jsonl", "json", "training", "conversation")
            filepath: 输出文件路径
            
        Returns:
            保存结果信息
        """
        logger.info("=" * 50)
        logger.info("步骤 5: 保存数据集")
        logger.info("=" * 50)
        
        if not self._qa_pairs:
            logger.warning("没有问答对，请先执行步骤 4")
            return {"status": "error", "message": "No QA pairs available"}
        
        # 如果没有指定路径，使用配置（支持时间戳）
        if filepath is None:
            filepath = str(self._get_output_filename(self.config.output.dataset_filename))
        
        # 保存数据集
        self.dataset_builder.save_dataset(self._qa_pairs, format, filepath)
        
        # 获取统计信息
        stats = self.dataset_builder.get_statistics(self._qa_pairs)
        
        result = {
            "format": format,
            "filepath": filepath,
            "total_records": len(self._qa_pairs),
            "statistics": stats
        }
        
        logger.info(f"数据集已保存: {result['filepath']}")
        logger.info(f"共 {result['total_records']} 条记录")
        
        return result
    
    def step6_post_process(
        self,
        strict_mode: bool = False,
        save_cleaned: bool = True,
        filepath: Optional[str] = None,
        output_format: str = "jsonl"
    ) -> Dict:
        """
        步骤6: 质量后处理与清洗
        
        对生成的问答对进行质量检测和修复：
        - 修复元认知泄漏 (如 "Based on the provided context...")
        - 检测并修复缩写幻觉
        - 过滤低质量内容
        
        Args:
            strict_mode: 严格模式下丢弃有问题数据，宽松模式下尝试修复
            save_cleaned: 是否保存清洗后的数据集
            filepath: 输出文件路径
            output_format: 输出格式 (jsonl, chatml, conversation 等)
            
        Returns:
            后处理统计信息
        """
        logger.info("=" * 50)
        logger.info("步骤 6: 质量后处理与清洗")
        logger.info("=" * 50)
        
        start_time = time.time()
        
        if not self._qa_pairs:
            logger.warning("没有问答对，请先执行步骤 4")
            return {"status": "error", "message": "No QA pairs available"}
        
        # 初始化后处理器
        processor = PostProcessor(strict_mode=strict_mode)
        
        # 处理问答对
        cleaned_pairs = []
        for qa in self._qa_pairs:
            processor.stats['total'] += 1
            
            report = processor.analyze_qa(
                qa.question, 
                qa.answer, 
                qa.metadata
            )
            
            if report.issues:
                processor.stats['issues_found'] += 1
                for issue in report.issues:
                    processor.stats['by_issue'][issue] += 1
                
                if strict_mode or not report.fixable:
                    processor.stats['discarded'] += 1
                    continue
                else:
                    # 尝试修复
                    fixed_answer = processor.fix_answer(qa.answer, report, qa.metadata)
                    qa.answer = fixed_answer
                    qa.metadata['quality_fixed'] = True
                    qa.metadata['original_issues'] = [i.name for i in report.issues]
                    processor.stats['fixed'] += 1
            else:
                processor.stats['clean'] += 1
            
            cleaned_pairs.append(qa)
        
        # 更新内部状态
        original_count = len(self._qa_pairs)
        self._qa_pairs = cleaned_pairs
        
        # 更新统计
        self.stats.post_process_clean = processor.stats['clean']
        self.stats.post_process_fixed = processor.stats['fixed']
        self.stats.post_process_discarded = processor.stats['discarded']
        self.stats.post_process_time = time.time() - start_time
        
        # 保存清洗后的数据集
        if save_cleaned and cleaned_pairs:
            if filepath is None:
                # 获取带时间戳的文件名（如果启用）
                base_filename = self.config.output.dataset_filename.replace('.jsonl', '_cleaned.jsonl')
                filepath = str(self._get_output_filename(base_filename))
            
            # 使用指定的输出格式
            self.dataset_builder.save_dataset(cleaned_pairs, output_format, filepath)
            
            # 如果是 chatml 或 conversation 格式，额外保存一份带格式后缀的文件
            if output_format in ['chatml', 'conversation', 'training_system']:
                sft_filepath = filepath.replace('.jsonl', f'_sft_{output_format}.jsonl')
                self.dataset_builder.save_dataset(cleaned_pairs, output_format, sft_filepath)
                logger.info(f"已导出 SFT 格式: {sft_filepath}")
        
        result = {
            "original_count": original_count,
            "cleaned_count": len(cleaned_pairs),
            "clean_data": processor.stats['clean'],
            "fixed_data": processor.stats['fixed'],
            "discarded_data": processor.stats['discarded'],
            "issues_by_type": {issue.name: count for issue, count in processor.stats['by_issue'].items() if count > 0},
            "time_seconds": self.stats.post_process_time,
            "output_file": filepath if save_cleaned else None
        }
        
        logger.info(f"后处理完成: {result['cleaned_count']}/{result['original_count']} 条保留")
        logger.info(f"  干净数据: {result['clean_data']}")
        logger.info(f"  已修复: {result['fixed_data']}")
        logger.info(f"  已丢弃: {result['discarded_data']}")
        if result['issues_by_type']:
            logger.info(f"  问题分布: {result['issues_by_type']}")
        logger.info(f"耗时: {result['time_seconds']:.2f} 秒")
        
        return result
    
    def analyze_quality(self) -> Dict:
        """
        分析当前数据集质量（不修改数据）
        
        Returns:
            质量分析报告
        """
        if not self._qa_pairs:
            return {"status": "error", "message": "No QA pairs available"}
        
        processor = PostProcessor(strict_mode=False)
        
        issues_by_type = {issue: 0 for issue in QualityIssue}
        total_confidence = 0
        examples = {}
        
        for qa in self._qa_pairs:
            report = processor.analyze_qa(qa.question, qa.answer, qa.metadata)
            total_confidence += report.confidence_score
            
            for issue in report.issues:
                issues_by_type[issue] += 1
                if issue not in examples and len(examples) < 5:
                    examples[issue.name] = {
                        'question': qa.question[:100],
                        'answer_preview': qa.answer[:200],
                        'details': report.issue_details
                    }
        
        total = len(self._qa_pairs)
        clean = total - sum(issues_by_type.values())
        
        return {
            "total_qa_pairs": total,
            "clean_data": clean,
            "clean_rate": clean / max(total, 1),
            "avg_confidence": total_confidence / max(total, 1),
            "issues_by_type": {k.name: v for k, v in issues_by_type.items() if v > 0},
            "examples": examples
        }

    def run(
        self,
        skip_data_loading: bool = False,
        use_existing_faiss: bool = True,
        max_chunks: Optional[int] = None,
        questions_per_chunk: Optional[int] = None,
        top_k: Optional[int] = None,
        output_format: str = "jsonl",
        enable_post_process: bool = True,
        strict_mode: bool = False,
        shard_id: Optional[int] = None,
        num_shards: Optional[int] = None
    ) -> Dict:
        """
        运行完整管道
        
        Args:
            skip_data_loading: 是否跳过数据加载（使用缓存）
            use_existing_faiss: 是否使用已有的 FAISS 索引
            max_chunks: 最大处理的 chunks 数量
            questions_per_chunk: 每个 chunk 生成的问题数
            top_k: RAG 检索返回的文档数量
            output_format: 输出格式
            enable_post_process: 是否启用质量后处理
            strict_mode: 后处理严格模式
            shard_id: 当前分片 ID (0 ~ num_shards-1)
            num_shards: 总分片数
            
        Returns:
            管道执行结果
        """
        logger.info("=" * 60)
        logger.info("RANSTRUCT 数据集生成管道启动")
        if shard_id is not None and num_shards is not None:
             logger.info(f"模式: 分片执行 {shard_id + 1}/{num_shards}")
        logger.info("=" * 60)
        
        self.stats.start_time = time.time()
        results = {}
        
        try:
            # 步骤 1: 数据加载
            if not skip_data_loading:
                results["step1_data_loading"] = self.step1_load_data()
            else:
                logger.info("跳过数据加载步骤")
            
            # 步骤 2: FAISS 索引
            results["step2_faiss"] = self.step2_build_faiss(use_existing_faiss)
            
            # 步骤 3: 问题生成 (支持分片)
            results["step3_questions"] = self.step3_generate_questions(
                max_chunks, questions_per_chunk, shard_id, num_shards
            )
            
            # 步骤 4: 答案生成
            results["step4_answers"] = self.step4_generate_answers(top_k)
            
            # 步骤 5: 保存原始数据集
            # 如果是分片模式，修改文件名
            save_filepath = None
            if shard_id is not None:
                base_name = self.config.output.dataset_filename
                name, ext = base_name.rsplit('.', 1) if '.' in base_name else (base_name, '')
                save_filepath = str(self._get_output_filename(f"{name}_part{shard_id}.{ext}" if ext else f"{name}_part{shard_id}"))

            results["step5_save"] = self.step5_save_dataset(output_format, save_filepath)
            
            # 步骤 6: 质量后处理（可选）
            # 注意: 分片模式下可能建议最后合并后再处理，或者分别处理
            if enable_post_process:
                # 分片模式下，后处理输出也加上后缀
                results["step6_post_process"] = self.step6_post_process(
                    strict_mode=strict_mode,
                    save_cleaned=True,
                    output_format=output_format  # 传递输出格式
                )
            
            self.stats.end_time = time.time()
            results["final_statistics"] = self.stats.to_dict()
            
            logger.info("=" * 60)
            logger.info("管道执行完成!")
            logger.info(f"总耗时: {self.stats.total_time:.2f} 秒")
            logger.info(f"生成问答对: {self.stats.total_answers_generated}")
            if enable_post_process:
                logger.info(f"清洗后保留: {len(self._qa_pairs)}")
            logger.info("=" * 60)
            
        except Exception as e:
            logger.error(f"管道执行失败: {e}")
            results["error"] = str(e)
            raise
        
        return results
    
    def load_intermediate_questions(self, filepath: Optional[str] = None):
        """加载中间保存的问题"""
        if filepath is None:
            filepath = str(self.config.output.output_dir / self.config.output.questions_filename)
        
        self._questions = QuestionGenerator.load_questions(str(filepath))
        logger.info(f"已加载 {len(self._questions)} 个问题")
    
    def get_qa_pairs(self) -> List[QAPair]:
        """获取生成的问答对"""
        return self._qa_pairs
    
    def get_statistics(self) -> Dict:
        """获取当前统计信息"""
        return {
            "pipeline": self.stats.to_dict(),
            "data": {
                "rag_chunks": len(self._rag_chunks),
                "ltg_chunks": len(self._ltg_chunks),
                "questions": len(self._questions),
                "qa_pairs": len(self._qa_pairs)
            },
            "faiss": self.faiss_manager.get_statistics() if self.faiss_manager.index else None
        }


def create_pipeline(config_path: Optional[str] = None) -> RANSTRUCTPipeline:
    """
    创建管道实例的工厂函数
    
    Args:
        config_path: 配置文件路径（YAML）
        
    Returns:
        配置好的管道实例
    """
    if config_path:
        config = Config.from_yaml(config_path)
    else:
        config = Config()
    
    return RANSTRUCTPipeline(config)


if __name__ == "__main__":
    # 测试管道
    pipeline = RANSTRUCTPipeline()
    
    # 打印配置信息
    print("RANSTRUCT 管道配置:")
    print(f"  问题生成模型: {pipeline.config.model.question_model}")
    print(f"  答案生成模型: {pipeline.config.model.answer_model}")
    print(f"  RAG Chunk 大小: {pipeline.config.chunk.rag_chunk_size}")
    print(f"  LTG Chunk 大小: {pipeline.config.chunk.ltg_chunk_size}")
    print(f"  输出目录: {pipeline.config.output.output_dir}")
    
    # 可以运行完整管道
    # results = pipeline.run(max_chunks=10)  # 限制 chunks 数量进行测试

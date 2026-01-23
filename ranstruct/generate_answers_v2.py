#!/usr/bin/env python3
"""
独立答案生成脚本 v2 - 完全独立，不依赖 answer_generator.py

特性：
- 可以和其他进程并行运行
- 自动使用时间戳命名输出文件，避免冲突
- 支持中断恢复
- 支持增量保存
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import re
import json
import time
import signal
import logging
import argparse
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional, Any
from dataclasses import dataclass, field

try:
    import ollama
except ImportError:
    ollama = None
    print("错误: ollama 未安装，请运行 pip install ollama")
    sys.exit(1)

# 设置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


# ==================== 数据类定义 ====================

@dataclass
class GeneratedQuestion:
    """生成的问题数据类"""
    question: str
    source_chunk_id: str
    metadata: Dict[str, Any] = field(default_factory=dict)


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


# ==================== 答案生成器 ====================

class StandaloneAnswerGenerator:
    """独立的答案生成器"""
    
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

    def __init__(
        self, 
        faiss_manager,
        model_name: str = "qwen2.5:1.5b",
        temperature: float = 0.3,
        top_p: float = 0.9,
        top_k: int = 5,
        min_answer_length: int = 30,
        max_answer_length: int = 3000,
        max_retries: int = 2
    ):
        """初始化答案生成器"""
        self.faiss_manager = faiss_manager
        self.model_name = model_name
        self.temperature = temperature
        self.top_p = top_p
        self.top_k = top_k
        self.min_answer_length = min_answer_length
        self.max_answer_length = max_answer_length
        self.max_retries = max_retries
        
        logger.info(f"答案生成器初始化完成，使用模型: {self.model_name}")
    
    def _call_llm(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        """调用 LLM 生成响应"""
        messages = []
        
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        
        messages.append({"role": "user", "content": prompt})
        
        response = ollama.chat(
            model=self.model_name,
            messages=messages,
            options={
                "temperature": self.temperature,
                "top_p": self.top_p,
            }
        )
        return response['message']['content']
    
    def _validate_answer(self, answer: str) -> bool:
        """验证答案是否有效"""
        if len(answer) < self.min_answer_length:
            return False
        if len(answer) > self.max_answer_length:
            return False
        
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
            if pattern in answer_lower and len(answer) < 150:
                return False
        
        if answer_lower.strip().endswith('?'):
            return False
        
        return True
    
    def _format_context(self, retrieved_docs: List[Dict]) -> tuple:
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
        """清洗问题文本"""
        json_prefixes = [
            r'^["\']?Question["\']?\s*[:\"]+ *["\']?',
            r'^["\']?Q["\']?\s*[:\"]+ *["\']?',
            r'^\{\s*["\']?question["\']?\s*[:\"]+ *["\']?',
        ]
        
        cleaned = question_text.strip()
        for pattern in json_prefixes:
            cleaned = re.sub(pattern, '', cleaned, flags=re.IGNORECASE)
        
        json_suffixes = [
            r'["\']?\s*,?\s*\}?\s*$',
            r'\s*,\s*$',
        ]
        for pattern in json_suffixes:
            cleaned = re.sub(pattern, '', cleaned)
        
        cleaned = cleaned.strip().strip('"\'')
        cleaned = re.sub(r'\?+', '?', cleaned)
        cleaned = re.sub(r'[,;]+\?$', '?', cleaned)
        
        if cleaned and not cleaned.endswith('?'):
            cleaned += '?'
            
        if cleaned:
            cleaned = cleaned[0].upper() + cleaned[1:]
        
        return cleaned
    
    def _retrieve(self, query: str, top_k: Optional[int] = None) -> List[Dict]:
        """检索相关文档"""
        if top_k is None:
            top_k = self.top_k
        
        # 搜索（faiss_manager.search 内部会自动生成嵌入向量）
        # search() 返回 List[Tuple[Chunk, float]]
        results = self.faiss_manager.search(query, top_k)
        
        # 转换为 Dict 格式
        formatted_results = []
        for chunk, score in results:
            formatted_results.append({
                "content": chunk.content,
                "score": score,
                "metadata": chunk.metadata,
                "chunk_id": chunk.chunk_id
            })
        
        return formatted_results
    
    def generate_answer(self, question: GeneratedQuestion) -> Optional[QAPair]:
        """为单个问题生成答案"""
        # 清洗问题
        cleaned_question = self._clean_question(question.question)
        
        if len(cleaned_question) < 10 or cleaned_question.lower().startswith('question'):
            return None
        
        # 检索相关文档
        retrieved_docs = self._retrieve(cleaned_question)
        
        if not retrieved_docs:
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
        for attempt in range(self.max_retries):
            try:
                answer = self._call_llm(prompt, self.SYSTEM_PROMPT)
                answer = answer.strip()
                
                if self._validate_answer(answer):
                    return QAPair(
                        question=cleaned_question,
                        answer=answer,
                        source_chunk_id=question.source_chunk_id,
                        retrieved_chunks=chunk_ids,
                        metadata={
                            **question.metadata,
                            "retrieval_scores": [doc.get("score", 0) for doc in retrieved_docs]
                        }
                    )
            except Exception as e:
                logger.warning(f"生成答案失败 (尝试 {attempt + 1}/{self.max_retries}): {e}")
        
        return None


# ==================== 信号处理 ====================

_shutdown_requested = False
_save_state = None


def signal_handler(signum, frame):
    """处理 Ctrl+C 信号"""
    global _shutdown_requested
    if _shutdown_requested:
        print("\n强制退出...")
        sys.exit(1)
    
    _shutdown_requested = True
    print("\n\n>>> 收到中断信号，正在保存进度...")
    
    if _save_state:
        _save_state()
        print(">>> 进度已保存，可以安全退出")
    
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)


# ==================== 工具函数 ====================

def save_results(output_file: Path, progress_file: Path, qa_pairs: List[QAPair], last_idx: int):
    """保存结果和进度"""
    with open(output_file, 'w', encoding='utf-8') as f:
        for qa in qa_pairs:
            f.write(json.dumps(qa.to_dict(), ensure_ascii=False) + '\n')
    
    with open(progress_file, 'w') as f:
        json.dump({
            'last_processed': last_idx,
            'total_success': len(qa_pairs),
            'timestamp': datetime.now().isoformat()
        }, f)


def generate_session_id() -> str:
    """生成唯一的会话ID（基于时间戳）"""
    return datetime.now().strftime("%Y%m%d_%H%M%S")


# ==================== 主函数 ====================

def main():
    parser = argparse.ArgumentParser(description='独立答案生成脚本 v2')
    parser.add_argument('--start', type=int, default=0, help='起始问题索引（从0开始）')
    parser.add_argument('--end', type=int, default=None, help='结束问题索引（不包含），默认处理到最后')
    parser.add_argument('--batch-size', type=int, default=100, help='每批处理的问题数量')
    parser.add_argument('--save-interval', type=int, default=50, help='每处理多少个问题保存一次')
    parser.add_argument('--session-id', type=str, default=None, help='会话ID，用于恢复进度。不指定则自动生成时间戳')
    parser.add_argument('--model', type=str, default='qwen2.5:1.5b', help='使用的模型名称')
    parser.add_argument('--top-k', type=int, default=5, help='RAG检索返回的文档数量')
    parser.add_argument('--questions-file', type=str, default=None, help='问题文件路径')
    parser.add_argument('--output-dir', type=str, default=None, help='输出目录')
    args = parser.parse_args()
    
    # 延迟导入，减少启动时间
    from ranstruct.config import Config
    from ranstruct.faiss_manager import FAISSManager
    
    # 配置
    config = Config()
    
    # 文件路径
    questions_file = Path(args.questions_file) if args.questions_file else config.output.output_dir / "generated_questions.jsonl"
    output_dir = Path(args.output_dir) if args.output_dir else config.output.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # 生成或使用会话ID
    session_id = args.session_id or generate_session_id()
    
    # 输出文件（使用时间戳命名）
    output_file = output_dir / f"ranstruct_dataset_{session_id}.jsonl"
    progress_file = output_dir / f"progress_{session_id}.json"
    
    print("=" * 70)
    print(f"独立答案生成进程 v2")
    print("=" * 70)
    print(f"会话ID: {session_id}")
    print(f"输出文件: {output_file}")
    print(f"进度文件: {progress_file}")
    print(f"处理范围: {args.start} - {args.end if args.end else '末尾'}")
    print(f"模型: {args.model}")
    print(f"RAG Top-K: {args.top_k}")
    print("=" * 70)
    
    # 检查是否有之前的进度
    last_processed = args.start
    if progress_file.exists():
        try:
            with open(progress_file, 'r') as f:
                progress = json.load(f)
                last_processed = progress.get('last_processed', args.start)
                print(f"发现之前的进度，从 {last_processed} 继续")
        except:
            pass
    
    # 1. 加载问题
    print(f"\n[1/4] 加载问题文件...")
    all_questions = []
    with open(questions_file, 'r', encoding='utf-8') as f:
        for line in f:
            data = json.loads(line)
            all_questions.append(GeneratedQuestion(
                question=data['question'],
                source_chunk_id=data['source_chunk_id'],
                metadata=data.get('metadata', {})
            ))
    
    total_questions = len(all_questions)
    end_idx = args.end if args.end else total_questions
    end_idx = min(end_idx, total_questions)
    
    # 从上次进度继续
    start_idx = max(last_processed, args.start)
    
    questions_to_process = all_questions[start_idx:end_idx]
    print(f"   总问题数: {total_questions}")
    print(f"   本进程处理: {start_idx} - {end_idx} (共 {len(questions_to_process)} 个)")
    
    if not questions_to_process:
        print("没有需要处理的问题！")
        return
    
    # 2. 初始化 FAISS
    print(f"\n[2/4] 加载 FAISS 索引...")
    start_time = time.time()
    faiss_manager = FAISSManager(config)
    faiss_manager.load_index()
    
    # 预热嵌入模型
    print("   预热嵌入模型...")
    faiss_manager.initialize_embedding_generator()
    faiss_manager.embedding_generator.encode_single("warmup query")
    print(f"   FAISS 加载完成，耗时: {time.time() - start_time:.2f} 秒")
    
    # 3. 初始化答案生成器
    print(f"\n[3/4] 初始化答案生成器...")
    answer_gen = StandaloneAnswerGenerator(
        faiss_manager=faiss_manager,
        model_name=args.model,
        top_k=args.top_k
    )
    
    # 4. 批量生成答案
    print(f"\n[4/4] 开始生成答案...")
    print("-" * 70)
    
    qa_pairs: List[QAPair] = []
    failed_count = 0
    batch_times = []
    current_idx = start_idx
    
    # 设置保存状态的回调函数
    global _save_state
    def save_current_state():
        save_results(output_file, progress_file, qa_pairs, current_idx)
    _save_state = save_current_state
    
    # 如果输出文件已存在，加载已有的结果
    if output_file.exists() and start_idx > args.start:
        print(f"   加载已有结果...")
        with open(output_file, 'r', encoding='utf-8') as f:
            for line in f:
                data = json.loads(line)
                qa_pairs.append(QAPair(
                    question=data['question'],
                    answer=data['answer'],
                    source_chunk_id=data['source_chunk_id'],
                    retrieved_chunks=data.get('retrieved_chunks', []),
                    metadata=data.get('metadata', {})
                ))
        print(f"   已加载 {len(qa_pairs)} 个已有结果")
    
    total_to_process = len(questions_to_process)
    
    for i, question in enumerate(questions_to_process):
        if _shutdown_requested:
            break
            
        batch_start = time.time()
        current_idx = start_idx + i
        
        try:
            qa_pair = answer_gen.generate_answer(question)
            
            if qa_pair:
                qa_pairs.append(qa_pair)
                status = "✓"
            else:
                failed_count += 1
                status = "✗"
            
            elapsed = time.time() - batch_start
            batch_times.append(elapsed)
            
            # 计算预估剩余时间
            avg_time = sum(batch_times[-100:]) / len(batch_times[-100:])
            remaining = total_to_process - i - 1
            eta_seconds = avg_time * remaining
            eta_str = f"{int(eta_seconds//3600)}h{int((eta_seconds%3600)//60)}m"
            
            print(f"[{current_idx+1:6d}] {status} {elapsed:5.2f}s | "
                  f"成功:{len(qa_pairs)} 失败:{failed_count} | "
                  f"ETA:{eta_str} | Q: {question.question[:30]}...")
            
        except Exception as e:
            failed_count += 1
            elapsed = time.time() - batch_start
            batch_times.append(elapsed)
            print(f"[{current_idx+1:6d}] ✗ {elapsed:5.2f}s | 错误: {e}")
        
        # 定期保存
        if (i + 1) % args.save_interval == 0:
            save_results(output_file, progress_file, qa_pairs, current_idx + 1)
            print(f"   >>> 已保存进度: {current_idx + 1}")
    
    # 最终保存
    save_results(output_file, progress_file, qa_pairs, end_idx)
    
    # 统计
    print("-" * 70)
    print(f"\n完成统计:")
    print(f"  会话ID: {session_id}")
    print(f"  处理范围: {start_idx} - {end_idx}")
    print(f"  成功: {len(qa_pairs)}")
    print(f"  失败: {failed_count}")
    if len(qa_pairs) + failed_count > 0:
        print(f"  成功率: {100*len(qa_pairs)/(len(qa_pairs)+failed_count):.1f}%")
    if batch_times:
        print(f"  平均耗时: {sum(batch_times)/len(batch_times):.2f} 秒/问题")
    print(f"  输出文件: {output_file}")


if __name__ == "__main__":
    main()

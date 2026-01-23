"""
RANSTRUCT 问题生成模块

使用 Mistral-7B-Instruct-0.3 模型生成问题：
- 基于 LTG Chunks 生成多个独特问题
- 问题去重和清洗
- 支持批量生成
"""

import re
import json
import logging
from typing import List, Dict, Optional, Set, Tuple, Any
from dataclasses import dataclass, field

try:
    import ollama
except ImportError:
    ollama = None
    print("警告: ollama 未安装，请运行 pip install ollama")

from .config import Config
from .data_processor import Chunk

logger = logging.getLogger(__name__)


@dataclass
class GeneratedQuestion:
    """生成的问题数据类"""
    question: str
    source_chunk_id: str
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def __hash__(self):
        return hash(self.question.lower().strip())
    
    def __eq__(self, other):
        if isinstance(other, GeneratedQuestion):
            return self.question.lower().strip() == other.question.lower().strip()
        return False


class QuestionGenerator:
    """问题生成器
    
    使用 Mistral-7B-Instruct 模型从 LTG Chunks 生成问题。
    """
    
    # 问题生成提示模板 - 深度技术问题模式 (v2.0)
    SYSTEM_PROMPT = """You are an expert question generator specializing in O-RAN (Open Radio Access Network) and telecommunications systems.

YOUR GOAL: Generate questions that would help train an AI to become a TRUE O-RAN EXPERT.

QUESTION QUALITY REQUIREMENTS:
1. Questions must require TECHNICAL UNDERSTANDING to answer, not just reading comprehension
2. Focus on: architecture decisions, protocol behaviors, implementation strategies, design trade-offs
3. Questions should be answerable by an expert WITHOUT needing the source document
4. Each question should teach something valuable about O-RAN systems

EXPLICITLY FORBIDDEN (DO NOT GENERATE):
- "What is the title of Section X?" - Document structure questions
- "On which page is X mentioned?" - Page/location questions
- "What does the document say about X?" - Document reference questions
- "How many items are listed in X?" - Counting/enumeration questions
- "What is mentioned in paragraph X?" - Paragraph reference questions
- "What are the chapter headings?" - Table of contents questions
- "What references are cited?" - Bibliography questions

ENCOURAGED QUESTION TYPES:
- HOW: "How does the E1 interface handle bearer context setup?"
- WHY: "Why is SCTP chosen over TCP for F1-C?"
- COMPARISON: "How do Near-RT RIC and Non-RT RIC differ in their control loops?"
- MECHANISM: "What mechanism ensures synchronization between O-DU and O-RU?"
- IMPLEMENTATION: "How should an xApp implement QoS policy enforcement?"
- DESIGN: "What architectural pattern enables RIC to scale horizontally?"

Remember: You are generating training data for an AI expert, not a reading comprehension test."""

    QUESTION_PROMPT_TEMPLATE = """Generate {num_questions} DEEP TECHNICAL questions based on this O-RAN content.

Content:
---
{context}
---

CRITICAL RULES:
1. Questions must test TECHNICAL UNDERSTANDING, not document navigation
2. An O-RAN expert should be able to answer WITHOUT seeing this specific document
3. Focus on: protocols, interfaces, architectures, procedures, mechanisms

FORBIDDEN PATTERNS (never generate):
- "What is Section X about?" ❌
- "What does the document mention about...?" ❌
- "According to the text, what is...?" ❌  
- "What is listed in the table/figure?" ❌
- "How many X are mentioned?" ❌

GOOD PATTERNS (generate these):
- "How does [protocol] handle [specific scenario]?" ✅
- "What is the purpose of [interface/component]?" ✅
- "Why is [design choice] necessary for [function]?" ✅
- "What are the key differences between [A] and [B]?" ✅
- "How should [component] be implemented to achieve [goal]?" ✅

Return ONLY a JSON array of {num_questions} question strings:
["Technical question 1?", "Technical question 2?", ...]"""

    CODE_QUESTION_PROMPT_TEMPLATE = """Generate {num_questions} DEEP TECHNICAL questions about this srsRAN code.

Source File: {filename}
---
{context}
---

QUESTION FOCUS (in order of importance):
1. DESIGN INTENT: "Why is this implemented this way?"
2. ARCHITECTURE: "How does this fit into the larger system?"
3. ALGORITHM: "What approach does this code take to solve X?"
4. TRADE-OFFS: "What trade-offs does this design make?"
5. USAGE: "How should other components interact with this?"

FORBIDDEN (never generate):
- "What type is returned by function X?" ❌ (syntax description)
- "What parameters does X take?" ❌ (signature reading)
- "What does line X do?" ❌ (line-by-line narration)
- "What is the name of this class?" ❌ (trivial)

GOOD PATTERNS:
- "What design pattern is used here and why?" ✅
- "How does this handle [edge case/error condition]?" ✅
- "Why is [specific approach] chosen over [alternative]?" ✅
- "How does this implementation relate to [O-RAN/3GPP concept]?" ✅

Return ONLY a JSON array of {num_questions} question strings:"""

    def __init__(self, config: Config):
        """
        初始化问题生成器
        
        Args:
            config: RANSTRUCT 配置
        """
        if ollama is None:
            raise ImportError("请安装 ollama: pip install ollama")
        
        self.config = config
        self.model_config = config.model
        self.generation_config = config.generation
        
        self.model_name = self.model_config.question_model
        self.temperature = self.model_config.question_model_temperature
        self.top_p = self.model_config.question_model_top_p
        
        # 问题去重集合
        self._seen_questions: Set[str] = set()
        
        logger.info(f"问题生成器初始化完成，使用模型: {self.model_name}")
    
    def _normalize_question(self, question: str) -> str:
        """标准化问题文本"""
        # 去除首尾空白
        question = question.strip()
        
        # 移除常见的JSON格式残留
        # 例如: 'Question": "What is...' -> 'What is...'
        json_prefixes = [
            r'^["\']?Question["\']?\s*[:\"]+\s*["\']?',  # Question": "...
            r'^["\']?Q["\']?\s*[:\"]+\s*["\']?',  # Q": "...
            r'^\{\s*["\']?question["\']?\s*[:\"]+\s*["\']?',  # {"question": "...
        ]
        for pattern in json_prefixes:
            question = re.sub(pattern, '', question, flags=re.IGNORECASE)
        
        # 移除尾部JSON格式残留
        json_suffixes = [
            r'["\']?\s*,?\s*\}?\s*$',  # ", } 等
            r'\s*,\s*$',  # 尾部逗号
        ]
        for pattern in json_suffixes:
            question = re.sub(pattern, '', question)
        
        # 再次去除首尾空白和引号
        question = question.strip().strip('"\'')
        
        # 移除重复的问号
        question = re.sub(r'\?+', '?', question)
        
        # 移除尾部的逗号和问号组合（如 ",?"）
        question = re.sub(r'[,;]+\?$', '?', question)
        
        # 确保以问号结尾
        if question and not question.endswith('?'):
            question += '?'
        
        # 首字母大写
        if question:
            question = question[0].upper() + question[1:]
        
        return question
    
    def _validate_question(self, question: str) -> bool:
        """验证问题是否有效（增强版 v2.0 - 过滤文档结构问题）"""
        # 检查长度
        if len(question) < self.generation_config.min_question_length:
            return False
        if len(question) > self.generation_config.max_question_length:
            return False
        
        # 检查是否为有效问题
        question_lower = question.lower()
        
        # 排除无效模式（基础清洗）
        invalid_patterns = [
            r'^(yes|no|true|false)\??$',  # 是/否答案
            r'^\d+\??$',  # 纯数字
            r'^(here|this|that|it)\s',  # 指代不明
            r'^\[',  # 以方括号开头
            r'^question',  # 仍以 'question' 开头（清洗失败）
            r'^\{',  # 以花括号开头（JSON残留）
            r'^"',  # 以引号开头
        ]
        
        for pattern in invalid_patterns:
            if re.match(pattern, question_lower):
                return False
        
        # ============================================================
        # 新增: 过滤文档结构类低价值问题
        # ============================================================
        document_structure_patterns = [
            # Section/Chapter/Page 引用
            r'section\s+\d+',           # "Section 4", "section 10.2"
            r'chapter\s+\d+',           # "Chapter 3"
            r'clause\s+\d+',            # "Clause 5.1"
            r'paragraph\s+\d+',         # "Paragraph 2"
            r'page\s+\d+',              # "Page 15"
            r'figure\s+\d+',            # "Figure 7"
            r'table\s+\d+',             # "Table 3"
            r'annex\s+[a-z\d]+',        # "Annex A", "Annex 1"
            r'appendix\s+[a-z\d]+',     # "Appendix B"
            
            # 文档元数据问题
            r'what is the title',       # "What is the title of..."
            r'what are the chapter',    # "What are the chapter headings"
            r'what references',         # "What references are cited"
            r'which document',          # "Which document describes..."
            r'in which section',        # "In which section is X mentioned"
            r'on which page',           # "On which page..."
            r'what does the document say',
            r'what is mentioned in',
            r'what is stated in',
            r'what is listed in',
            r'what is described in the',
            r'according to the (document|text|specification)',
            
            # 计数/枚举问题
            r'how many .* are (mentioned|listed|described)',
            r'list all .* mentioned',
            r'enumerate the',
            r'what are all the .* in the',
        ]
        
        for pattern in document_structure_patterns:
            if re.search(pattern, question_lower):
                logger.debug(f"问题被过滤（文档结构类）: {question[:50]}...")
                return False
        
        # ============================================================
        # 新增: 过滤浅层代码问题
        # ============================================================
        shallow_code_patterns = [
            r'what (type|data type) (is|does) .* return',   # "What type does X return"
            r'what (parameters?|arguments?) does .* take',  # "What parameters does X take"
            r'what is the (return type|signature) of',      # "What is the return type of"
            r'what does line \d+',                          # "What does line 15 do"
            r'what is the name of (this|the) (class|function|method)',
            r'how many (parameters?|arguments?|lines)',     # "How many parameters"
        ]
        
        for pattern in shallow_code_patterns:
            if re.search(pattern, question_lower):
                logger.debug(f"问题被过滤（浅层代码类）: {question[:50]}...")
                return False
        
        # 应该包含问题词或以问号结尾
        question_words = ['what', 'how', 'why', 'when', 'where', 'which', 'who', 'can', 'does', 'is', 'are', 'should', 'explain', 'describe']
        has_question_word = any(word in question_lower for word in question_words)
        ends_with_question = question.endswith('?')
        
        return has_question_word or ends_with_question
    
    def _parse_questions(self, response: str) -> List[str]:
        """解析模型响应中的问题"""
        questions = []
        
        # 尝试解析 JSON 数组
        try:
            # 查找 JSON 数组
            json_match = re.search(r'\[[\s\S]*\]', response)
            if json_match:
                parsed = json.loads(json_match.group())
                if isinstance(parsed, list):
                    questions = [str(q) for q in parsed if isinstance(q, str)]
        except json.JSONDecodeError:
            pass
        
        # 如果 JSON 解析失败，尝试逐行解析
        if not questions:
            lines = response.strip().split('\n')
            for line in lines:
                line = line.strip()
                # 移除编号前缀
                line = re.sub(r'^[\d]+[\.\)]\s*', '', line)
                line = re.sub(r'^[-\*]\s*', '', line)
                # 移除引号
                line = re.sub(r'^["\']|["\']$', '', line)
                
                if line and '?' in line:
                    questions.append(line)
        
        return questions
    
    def _call_llm(self, prompt: str, system_prompt: Optional[str] = None) -> str:
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
    
    def generate_from_chunk(
        self, 
        chunk: Chunk, 
        num_questions: Optional[int] = None
    ) -> List[GeneratedQuestion]:
        """
        从单个 chunk 生成问题
        
        Args:
            chunk: LTG Chunk
            num_questions: 生成问题数量
            
        Returns:
            生成的问题列表
        """
        if num_questions is None:
            num_questions = self.generation_config.questions_per_chunk
        
        # 选择合适的提示模板
        is_code = chunk.metadata.get("type") in ["srsran_code", "codeset"]
        
        if is_code:
            prompt = self.CODE_QUESTION_PROMPT_TEMPLATE.format(
                context=chunk.content,
                filename=chunk.metadata.get("filename", "unknown"),
                num_questions=num_questions
            )
        else:
            prompt = self.QUESTION_PROMPT_TEMPLATE.format(
                context=chunk.content,
                num_questions=num_questions
            )
        
        # 重试机制
        questions = []
        for attempt in range(self.generation_config.max_retries):
            try:
                response = self._call_llm(prompt, self.SYSTEM_PROMPT)
                raw_questions = self._parse_questions(response)
                
                # 验证和清洗问题
                for q in raw_questions:
                    normalized = self._normalize_question(q)
                    if self._validate_question(normalized):
                        questions.append(normalized)
                
                if questions:
                    break
                    
            except Exception as e:
                logger.warning(f"生成问题失败 (尝试 {attempt + 1}/{self.generation_config.max_retries}): {e}")
        
        # 创建问题对象
        generated = []
        for q in questions:
            gq = GeneratedQuestion(
                question=q,
                source_chunk_id=chunk.chunk_id,
                metadata={
                    "source_file": chunk.metadata.get("filename"),
                    "source_type": chunk.metadata.get("type"),
                    "chunk_index": chunk.chunk_index
                }
            )
            generated.append(gq)
        
        logger.debug(f"从 chunk {chunk.chunk_id} 生成了 {len(generated)} 个问题")
        return generated
    
    def generate_batch(
        self, 
        chunks: List[Chunk],
        num_questions_per_chunk: Optional[int] = None,
        deduplicate: bool = True
    ) -> List[GeneratedQuestion]:
        """
        批量生成问题
        
        Args:
            chunks: LTG Chunks 列表
            num_questions_per_chunk: 每个 chunk 生成的问题数
            deduplicate: 是否去重
            
        Returns:
            生成的问题列表
        """
        all_questions = []
        
        logger.info(f"开始从 {len(chunks)} 个 chunks 生成问题...")
        
        for i, chunk in enumerate(chunks):
            try:
                questions = self.generate_from_chunk(chunk, num_questions_per_chunk)
                
                if deduplicate:
                    # 去重
                    unique_questions = []
                    for q in questions:
                        q_key = q.question.lower().strip()
                        if q_key not in self._seen_questions:
                            self._seen_questions.add(q_key)
                            unique_questions.append(q)
                    all_questions.extend(unique_questions)
                else:
                    all_questions.extend(questions)
                
                if (i + 1) % 10 == 0:
                    logger.info(f"已处理 {i + 1}/{len(chunks)} 个 chunks，生成 {len(all_questions)} 个问题")
                    
            except Exception as e:
                logger.error(f"处理 chunk {chunk.chunk_id} 时出错: {e}")
                continue
        
        logger.info(f"问题生成完成，共 {len(all_questions)} 个唯一问题")
        return all_questions
    
    def reset_deduplication(self):
        """重置去重集合"""
        self._seen_questions.clear()
    
    def save_questions(self, questions: List[GeneratedQuestion], filepath: str):
        """保存问题到文件"""
        import json
        
        with open(filepath, 'w', encoding='utf-8') as f:
            for q in questions:
                record = {
                    "question": q.question,
                    "source_chunk_id": q.source_chunk_id,
                    "metadata": q.metadata
                }
                f.write(json.dumps(record, ensure_ascii=False) + '\n')
        
        logger.info(f"已保存 {len(questions)} 个问题到 {filepath}")
    
    @staticmethod
    def load_questions(filepath: str) -> List[GeneratedQuestion]:
        """从文件加载问题"""
        import json
        
        questions = []
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    record = json.loads(line)
                    q = GeneratedQuestion(
                        question=record["question"],
                        source_chunk_id=record["source_chunk_id"],
                        metadata=record.get("metadata", {})
                    )
                    questions.append(q)
        
        logger.info(f"从 {filepath} 加载了 {len(questions)} 个问题")
        return questions


if __name__ == "__main__":
    # 测试问题生成器
    logging.basicConfig(level=logging.INFO)
    
    config = Config()
    generator = QuestionGenerator(config)
    
    # 创建测试 chunk
    test_content = """
    O-RAN Alliance defines the Open RAN architecture with key components:
    
    1. O-RU (O-RAN Radio Unit): Handles RF processing and lower PHY functions
    2. O-DU (O-RAN Distributed Unit): Handles RLC, MAC, and upper PHY
    3. O-CU (O-RAN Central Unit): Handles RRC and PDCP, split into O-CU-CP and O-CU-UP
    
    The fronthaul interface between O-RU and O-DU uses eCPRI protocol.
    Near-RT RIC provides intelligent radio resource management with <1s latency.
    """
    
    test_chunk = Chunk(
        content=test_content,
        chunk_type="ltg",
        source_doc_id="test_doc",
        chunk_index=0,
        metadata={"type": "oran_specification", "filename": "test.md"}
    )
    
    print("正在生成问题...")
    questions = generator.generate_from_chunk(test_chunk, num_questions=3)
    
    print(f"\n生成了 {len(questions)} 个问题:")
    for i, q in enumerate(questions, 1):
        print(f"  {i}. {q.question}")

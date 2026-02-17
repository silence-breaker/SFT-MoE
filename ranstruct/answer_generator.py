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
    """问答对数据类
    
    Attributes:
        question: 问题文本
        answer: 答案文本
        source_chunk_id: 原始 LTG chunk 的 ID
        retrieved_chunks: 检索到的 RAG chunks（支持完整信息或仅ID）
        metadata: 元数据（包含 retrieval_scores 等）
    """
    question: str
    answer: str
    source_chunk_id: str
    retrieved_chunks: List[Any] = field(default_factory=list)  # 支持 List[str] 或 List[Dict]
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
    
    # O-RAN 专家系统提示 (用于 SFT 训练)
    SYSTEM_PROMPT_FOR_TRAINING = """You are an O-RAN Technical Expert with comprehensive knowledge of Open RAN architecture, 3GPP specifications, and telecommunications systems. Provide accurate, detailed, and technically precise answers about O-RAN components, interfaces, protocols, and implementations."""
    
    def to_training_format(self) -> Dict:
        """转换为训练格式（Alpaca 指令微调格式）"""
        return {
            "instruction": self.question,
            "input": "",
            "output": self.answer
        }
    
    def to_training_format_with_system(self) -> Dict:
        """转换为带系统提示的训练格式（推荐用于专业领域 SFT）"""
        return {
            "system": self.SYSTEM_PROMPT_FOR_TRAINING,
            "instruction": self.question,
            "input": "",
            "output": self.answer
        }
    
    def to_conversation_format(self) -> Dict:
        """转换为对话格式（ShareGPT/OpenAI 格式）"""
        return {
            "conversations": [
                {"role": "system", "content": self.SYSTEM_PROMPT_FOR_TRAINING},
                {"role": "user", "content": self.question},
                {"role": "assistant", "content": self.answer}
            ]
        }
    
    def to_chatml_format(self) -> Dict:
        """转换为 ChatML 格式（适用于 Qwen、Llama-3 等模型 SFT）"""
        return {
            "messages": [
                {"role": "system", "content": self.SYSTEM_PROMPT_FOR_TRAINING},
                {"role": "user", "content": self.question},
                {"role": "assistant", "content": self.answer}
            ]
        }


class AnswerGenerator:
    """答案生成器
    
    使用 Qwen-2.5-Instruct 模型结合 RAG 检索生成答案。
    """
    
    # 答案生成提示模板 - O-RAN 专家模式 (v2.0)
    SYSTEM_PROMPT = """You are an O-RAN Technical Expert with deep knowledge of Open RAN architecture, 3GPP specifications, and telecommunications systems.

YOUR IDENTITY:
- You ARE an expert, not a retrieval system
- Speak with authority using first-person expert voice ("The O-DU handles...", "This is implemented by...")
- Internalize the knowledge - respond as if you genuinely know the material

ABSOLUTE PROHIBITIONS (CRITICAL):
1. NEVER mention "context", "document", "provided text", "passage", "excerpt"
2. NEVER use phrases like "According to...", "Based on the...", "The text states..."
3. NEVER use [Document X] or similar citation markers
4. NEVER reveal you are reading from source material
5. If you cannot answer, say EXACTLY: "INSUFFICIENT_DATA" (nothing else)

RESPONSE STYLE:
- Be direct, authoritative, and technically precise
- Use specific O-RAN terminology naturally (E1, F1, RIC, O-DU, O-CU-CP, etc.)
- Reference actual standards when relevant (e.g., "as defined in 3GPP TS 38.xxx")
- Structure complex answers with clear organization
- Explain WHY, not just WHAT

EXAMPLE GOOD ANSWER:
"The E1 interface connects the O-CU-CP and O-CU-UP, carrying control plane signaling for bearer management. It uses SCTP for transport reliability and supports procedures like bearer context setup and modification."

EXAMPLE BAD ANSWER (NEVER DO THIS):
"According to the provided context, the E1 interface is described in Document 1 as connecting..." """

    ANSWER_PROMPT_TEMPLATE = """You have deep expertise in O-RAN systems. Use the following technical reference to answer.

Reference Material:
{context}

Question: {question}

Instructions:
- Answer as a domain expert explaining to a colleague
- DO NOT mention "context", "document", "provided text" or any source references
- Speak with authority: "The F1 interface...", "This is implemented via..."
- If the reference is insufficient to answer accurately, respond with EXACTLY: "INSUFFICIENT_DATA"
- Include specific technical details, parameters, and protocol behaviors
- Explain the 'why' and 'how', not just 'what'

Expert Answer:"""

    CODE_ANSWER_PROMPT_TEMPLATE = """You are a senior software architect familiar with srsRAN and O-RAN implementations.

Code Reference:
{context}

Question: {question}

Instructions:
- Explain the DESIGN INTENT and ARCHITECTURAL DECISIONS, not just syntax
- Focus on WHY the code is structured this way, not just WHAT it does
- Discuss patterns, trade-offs, and engineering rationale
- DO NOT just describe function signatures or variable types
- If the code is insufficient to understand the design, respond with EXACTLY: "INSUFFICIENT_DATA"
- Reference related O-RAN/3GPP concepts when applicable

Expert Analysis:"""

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
        """验证答案是否有效（增强拒答过滤 v2.0）"""
        # 0. 检测明确的拒绝信号（INSUFFICIENT_DATA）
        if "INSUFFICIENT_DATA" in answer:
            logger.debug("答案包含 INSUFFICIENT_DATA 标记")
            return False
        
        # 1. 检查长度
        if len(answer) < self.generation_config.min_answer_length:
            logger.debug(f"答案太短 ({len(answer)} < {self.generation_config.min_answer_length})")
            return False
        if len(answer) > self.generation_config.max_answer_length:
            logger.debug(f"答案太长 ({len(answer)} > {self.generation_config.max_answer_length})")
            return False
        
        answer_lower = answer.lower()
        
        # 2. 严格拒答模式 - 检测 "不知道/无法回答" 类回复（宁缺毋滥）
        rejection_patterns = [
            # 明确的信息缺失
            "not provided",
            "not mentioned", 
            "not specified",
            "not available",
            "not given",
            "not included",
            "not stated",
            "not found",
            "cannot be found",
            "cannot find",
            "context does not",
            "context doesn't",
            "document does not",
            "document doesn't",
            "information is not",
            "no information about",
            "no information on",
            "no data about",
            "no details about",
            "insufficient information",
            "insufficient data",
            "not enough information",
            # 无法回答类
            "i cannot",
            "i can't",
            "i am unable",
            "i'm unable",
            "cannot determine",
            "cannot answer",
            "unable to determine",
            "unable to answer",
            "would need more",
            "would require more",
            "need additional",
            "require additional",
            # 不确定推测类（生成幻觉的前兆）
            "i'm not sure",
            "i am not sure",
            "i don't know",
            "i do not know",
            "it is unclear",
            "it's unclear",
            "it is not clear",
            "we cannot know",
            "there is no way to know",
        ]
        
        for pattern in rejection_patterns:
            if pattern in answer_lower:
                logger.debug(f"答案包含拒答模式: {pattern}")
                return False
        
        # 3. 检测过度不确定性表述（多个不确定词 = 幻觉风险高）
        uncertainty_patterns = [
            r'\bprobably\b', r'\bmight\b', r'\bcould be\b', r'\bperhaps\b',
            r'\bpossibly\b', r'\bmaybe\b', r'\blikely\b', r'\bpresumably\b',
            r'\bit seems\b', r'\bappears to\b', r'\bi think\b', r'\bi believe\b',
            r'\bi assume\b', r'\bi guess\b', r'\bseems like\b',
        ]
        import re
        uncertainty_count = sum(1 for p in uncertainty_patterns if re.search(p, answer_lower))
        if uncertainty_count >= 2:
            logger.debug(f"答案包含过多不确定性表述 ({uncertainty_count}个)")
            return False
        
        # 4. 检测元认知泄漏（严重质量问题）
        metacognitive_patterns = [
            r'according to the (provided |given )?(context|document|text)',
            r'based on the (provided |given )?(context|document|text)',
            r'the (provided |given )?(context|document|text) (shows?|states?|mentions?)',
            r'\[document \d+\]',
            r'\[doc\.? ?\d+\]',
        ]
        for pattern in metacognitive_patterns:
            if re.search(pattern, answer_lower):
                logger.debug(f"答案包含元认知泄漏: {pattern}")
                return False
        
        # 5. 检查答案是否只是重复问题
        if answer_lower.strip().endswith('?'):
            logger.debug("答案以问号结尾，可能是重复问题")
            return False
        
        return True
    
    def _clean_answer(self, answer: str) -> str:
        """清洗答案文本，移除引用标记和元认知痕迹
        
        执行以下清洗:
        1. 移除 <doc>, </doc> 等 XML 标记
        2. 移除 [Document X], [Doc X] 等引用标记
        3. 移除元认知泄漏短语开头
        4. 修复格式问题
        """
        cleaned = answer.strip()
        
        # 1. 移除 XML/HTML 标签标记
        xml_patterns = [
            r'</?doc\d*>',           # <doc>, </doc>, <doc1>
            r'</?document\d*>',      # <document>, </document>
            r'</?source\d*>',        # <source>, </source>
            r'</?context>',          # <context>, </context>
            r'</?reference\d*>',     # <reference>, </reference>
            r'</?excerpt>',          # <excerpt>, </excerpt>
        ]
        for pattern in xml_patterns:
            cleaned = re.sub(pattern, '', cleaned, flags=re.IGNORECASE)
        
        # 2. 移除 [Document X] 和 [Doc X] 引用标记
        citation_patterns = [
            r'\[Document\s*\d+\]:?\s*',
            r'\[Doc\.?\s*\d+\]:?\s*',
            r'\[Source\s*\d+\]:?\s*',
            r'\[Ref\.?\s*\d+\]:?\s*',
            r'\(\s*Document\s*\d+\s*\)',
            r'\(\s*Source:\s*[^)]+\)',
        ]
        for pattern in citation_patterns:
            cleaned = re.sub(pattern, '', cleaned, flags=re.IGNORECASE)
        
        # 3. 移除元认知泄漏开头短语
        prefix_patterns = [
            r'^According to the (provided |given )?(context|documents?|text|information)[,\s]*',
            r'^Based on the (provided |given )?(context|documents?|text|information)[,\s]*',
            r'^From the (provided |given )?(context|documents?|text|information)[,\s]*',
            r'^The (provided |given )?(context|documents?|text) (shows?|indicates?|mentions?|states?|describes?)[,\s]*that\s*',
            r'^In the (provided |given )?(context|documents?|text)[,\s]*',
            r'^As (mentioned|stated|described|noted) in the (context|documents?|text)[,\s]*',
        ]
        for pattern in prefix_patterns:
            cleaned = re.sub(pattern, '', cleaned, flags=re.IGNORECASE)
        
        # 4. 清理格式问题
        cleaned = re.sub(r'^[\s,;:]+', '', cleaned)  # 移除开头的空白和标点
        cleaned = re.sub(r'\s+', ' ', cleaned)       # 合并多个空格
        cleaned = cleaned.strip()
        
        # 5. 确保首字母大写
        if cleaned and cleaned[0].islower():
            cleaned = cleaned[0].upper() + cleaned[1:]
        
        return cleaned
    
    def _format_context(self, retrieved_docs: List[Dict]) -> Tuple[str, List[Dict], List[str]]:
        """格式化检索到的文档为上下文
        
        Returns:
            Tuple of (context_string, chunk_details, chunk_ids)
            - context_string: 给 LLM 的格式化上下文
            - chunk_details: 完整的 chunk 信息列表（用于保存）
            - chunk_ids: chunk ID 列表
        """
        if not retrieved_docs:
            return "", [], []
        
        context_parts = []
        chunk_details = []
        chunk_ids = []
        
        for i, doc in enumerate(retrieved_docs, 1):
            source = doc.get("metadata", {}).get("filename", "Unknown")
            content = doc.get("content", "")
            chunk_id = doc.get("chunk_id", "")
            score = doc.get("score", 0.0)
            
            # 构建 LLM 上下文（不显示 Document X 避免被答案引用）
            context_parts.append(f"--- Source: {source} ---\n{content}")
            
            # 保存完整的 chunk 信息
            chunk_details.append({
                "chunk_id": chunk_id,
                "content": content[:500] + "..." if len(content) > 500 else content,  # 截断长内容
                "source": source,
                "score": score,
                "metadata": doc.get("metadata", {})
            })
            chunk_ids.append(chunk_id)
        
        return "\n\n".join(context_parts), chunk_details, chunk_ids
    
    # ============================================================================
    # O-RAN 实体一致性规则 (Entity Consistency Rules)
    # 用于检测问题与检索内容之间的实体不匹配（幻觉前兆）
    # ============================================================================
    ENTITY_CONSISTENCY_RULES = {
        # 接口相关规则: 问题提到接口 -> 检索内容必须包含相关实体
        "F1": {
            "question_patterns": [r'\bF1\b', r'\bF1-C\b', r'\bF1-U\b', r'F1 interface'],
            "required_entities": ["O-CU", "O-DU", "CU", "DU", "gNB-CU", "gNB-DU"],
            "forbidden_entities": ["O-RU", "RU", "fronthaul"],  # F1 不涉及 RU
            "min_required": 1,
        },
        "E1": {
            "question_patterns": [r'\bE1\b', r'E1 interface'],
            "required_entities": ["O-CU-CP", "O-CU-UP", "CU-CP", "CU-UP"],
            "forbidden_entities": ["O-DU", "O-RU", "DU", "RU"],
            "min_required": 1,
        },
        "E2": {
            "question_patterns": [r'\bE2\b', r'E2 interface', r'E2AP'],
            "required_entities": ["RIC", "Near-RT RIC", "O-CU", "O-DU", "xApp"],
            "forbidden_entities": [],
            "min_required": 1,
        },
        "Open Fronthaul": {
            "question_patterns": [r'fronthaul', r'Open FH', r'\bFH\b', r'O-RU.*O-DU', r'O-DU.*O-RU'],
            "required_entities": ["O-RU", "O-DU", "RU", "DU", "eCPRI", "CUS-Plane", "M-Plane"],
            "forbidden_entities": ["O-CU", "CU", "E1", "E2"],
            "min_required": 1,
        },
        "A1": {
            "question_patterns": [r'\bA1\b', r'A1 interface', r'A1AP'],
            "required_entities": ["Non-RT RIC", "Near-RT RIC", "SMO", "rApp"],
            "forbidden_entities": [],
            "min_required": 1,
        },
        "NGAP": {
            "question_patterns": [r'\bNGAP\b', r'NG interface', r'NG-C'],
            "required_entities": ["AMF", "gNB", "5GC", "5G Core", "NG"],
            "forbidden_entities": [],
            "min_required": 1,
        },
        # 协议层相关规则
        "PDCP": {
            "question_patterns": [r'\bPDCP\b'],
            "required_entities": ["PDCP", "ciphering", "integrity", "header compression", "RLC"],
            "forbidden_entities": [],
            "min_required": 1,
        },
        "RLC": {
            "question_patterns": [r'\bRLC\b', r'Radio Link Control'],
            "required_entities": ["RLC", "ARQ", "segmentation", "reassembly", "AM", "UM", "TM"],
            "forbidden_entities": [],
            "min_required": 1,
        },
        "MAC": {
            "question_patterns": [r'\bMAC\b(?! address)', r'MAC layer', r'MAC scheduler'],
            "required_entities": ["MAC", "scheduler", "HARQ", "multiplexing", "demultiplexing"],
            "forbidden_entities": [],
            "min_required": 1,
        },
    }
    
    def _check_entity_consistency(
        self, 
        question: str, 
        retrieved_docs: List[Dict]
    ) -> Dict[str, Any]:
        """
        检查问题与检索内容之间的实体一致性
        
        Args:
            question: 问题文本
            retrieved_docs: 检索到的文档列表
            
        Returns:
            {
                "consistent": bool,
                "reason": str,
                "matched_rule": str or None,
                "found_entities": List[str],
                "missing_entities": List[str]
            }
        """
        question_lower = question.lower()
        
        # 合并所有检索内容
        all_context = " ".join([
            doc.get("content", "").lower() 
            for doc in retrieved_docs
        ])
        
        # 检查每条规则
        for rule_name, rule in self.ENTITY_CONSISTENCY_RULES.items():
            # 检查问题是否匹配该规则
            question_matches = any(
                re.search(pattern, question, re.IGNORECASE) 
                for pattern in rule["question_patterns"]
            )
            
            if not question_matches:
                continue
            
            # 问题匹配了，检查检索内容
            found_entities = []
            missing_entities = []
            
            for entity in rule["required_entities"]:
                if entity.lower() in all_context:
                    found_entities.append(entity)
                else:
                    missing_entities.append(entity)
            
            # 检查是否有足够的必需实体
            if len(found_entities) < rule["min_required"]:
                return {
                    "consistent": False,
                    "reason": f"问题涉及 {rule_name}，但检索内容缺少关键实体: {missing_entities[:3]}",
                    "matched_rule": rule_name,
                    "found_entities": found_entities,
                    "missing_entities": missing_entities
                }
            
            # 检查是否有禁止的实体（表明检索到错误内容）
            for forbidden in rule.get("forbidden_entities", []):
                # 只有当禁止实体出现频率高于所需实体时才标记
                forbidden_count = all_context.count(forbidden.lower())
                found_count = sum(all_context.count(e.lower()) for e in found_entities)
                
                if forbidden_count > found_count * 2:  # 禁止实体占主导
                    return {
                        "consistent": False,
                        "reason": f"问题涉及 {rule_name}，但检索内容主要讲的是 {forbidden}（实体不匹配）",
                        "matched_rule": rule_name,
                        "found_entities": found_entities,
                        "missing_entities": missing_entities
                    }
        
        # 没有匹配任何规则，或者通过了检查
        return {
            "consistent": True,
            "reason": "通过实体一致性检查",
            "matched_rule": None,
            "found_entities": [],
            "missing_entities": []
        }
    
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
        
        # ============================================================
        # 幻觉抑制机制 1: 检索相关性阈值 (Confidence Thresholding)
        # ============================================================
        retrieval_scores = [doc.get("score", 0.0) for doc in retrieved_docs]
        max_score = max(retrieval_scores) if retrieval_scores else 0.0
        
        if self.faiss_config.enable_confidence_threshold:
            if max_score < self.faiss_config.min_retrieval_score:
                logger.debug(
                    f"检索置信度过低 (max={max_score:.3f} < threshold={self.faiss_config.min_retrieval_score}), "
                    f"丢弃问题: {cleaned_question[:50]}..."
                )
                return None
        
        # ============================================================
        # 幻觉抑制机制 2: 实体一致性预检查 (Entity Consistency Pre-check)
        # ============================================================
        entity_check_result = self._check_entity_consistency(cleaned_question, retrieved_docs)
        if not entity_check_result['consistent']:
            logger.debug(
                f"实体一致性检查失败: {entity_check_result['reason']}, "
                f"问题: {cleaned_question[:50]}..."
            )
            return None
        
        # 格式化上下文（返回完整的 chunk 信息）
        context, chunk_details, chunk_ids = self._format_context(retrieved_docs)
        
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
                    # 清洗答案中的引用标记和元认知痕迹
                    cleaned_answer = self._clean_answer(answer)
                    
                    return QAPair(
                        question=cleaned_question,  # 使用清洗后的问题
                        answer=cleaned_answer,      # 使用清洗后的答案
                        source_chunk_id=question.source_chunk_id,
                        retrieved_chunks=chunk_details,  # 保存完整的 chunk 信息（含内容）
                        metadata={
                            **question.metadata,
                            "retrieval_scores": retrieval_scores,  # 保留检索分数
                            "top_k_used": top_k,
                            "avg_retrieval_score": sum(retrieval_scores) / len(retrieval_scores) if retrieval_scores else 0
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
        
        # 3. 批量检索所有问题的相关文档 (使用 RAGRetriever，支持 Reranker)
        logger.info("批量检索相关文档 (启用 Cross-Encoder Reranker)...")
        all_retrieved = self.retriever.retrieve_batch(cleaned_questions, top_k)
        logger.info("批量检索完成")
        
        # 4. 逐个生成答案
        for i, (question, cleaned_q, retrieved_docs) in enumerate(
            zip(valid_questions, cleaned_questions, all_retrieved)
        ):
            # 检查是否收到中断信号
            if _shutdown_requested:
                logger.warning(f"收到中断信号，在第 {i} 个问题处停止")
                break
            
            try:
                if not retrieved_docs:
                    logger.warning(f"未找到相关文档: {cleaned_q[:50]}...")
                    failed_count += 1
                    continue
                
                # retrieved_docs 已经是正确格式: List[Dict]
                # 包含 content, score, metadata, chunk_id, reranked
                
                # 格式化上下文（返回完整的 chunk 信息）
                context, chunk_details, chunk_ids = self._format_context(retrieved_docs)
                
                # 提取 retrieval_scores (Reranker 分数，0.9+ 表示高相关性)
                retrieval_scores = [doc.get("score", 0.0) for doc in retrieved_docs]
                
                # 记录是否使用了 Reranker
                is_reranked = retrieved_docs[0].get("reranked", False) if retrieved_docs else False
                if i == 0:  # 只在第一个问题时记录
                    logger.info(f"检索分数示例: {retrieval_scores}, Reranked: {is_reranked}")
                
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
                            # 清洗答案中的引用标记和元认知痕迹
                            cleaned_answer = self._clean_answer(answer)
                            
                            qa_pair = QAPair(
                                question=cleaned_q,
                                answer=cleaned_answer,
                                source_chunk_id=question.source_chunk_id,
                                retrieved_chunks=chunk_details,  # 保存完整的 chunk 信息
                                metadata={
                                    **question.metadata,
                                    "retrieval_scores": retrieval_scores,
                                    "top_k_used": top_k,
                                    "avg_retrieval_score": sum(retrieval_scores) / len(retrieval_scores) if retrieval_scores else 0
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
            format: 输出格式 
                - "jsonl": 原始格式，包含所有元数据（用于调试/分析）
                - "json": JSON数组格式
                - "training": Alpaca格式 (instruction/input/output)
                - "training_system": 带系统提示的Alpaca格式（推荐）
                - "conversation": ShareGPT对话格式
                - "chatml": ChatML格式（适用于Qwen/Llama-3等模型SFT）
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
        elif format == "training_system":
            self._save_training_format_with_system(qa_pairs, filepath)
        elif format == "conversation":
            self._save_conversation_format(qa_pairs, filepath)
        elif format == "chatml":
            self._save_chatml_format(qa_pairs, filepath)
        else:
            raise ValueError(f"不支持的格式: {format}。支持: jsonl, json, training, training_system, conversation, chatml")
        
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
    
    def _save_training_format_with_system(self, qa_pairs: List[QAPair], filepath: str):
        """保存为带系统提示的训练格式（推荐用于专业领域SFT）"""
        with open(filepath, 'w', encoding='utf-8') as f:
            for qa in qa_pairs:
                f.write(json.dumps(qa.to_training_format_with_system(), ensure_ascii=False) + '\n')
    
    def _save_conversation_format(self, qa_pairs: List[QAPair], filepath: str):
        """保存为对话格式（ShareGPT格式）"""
        with open(filepath, 'w', encoding='utf-8') as f:
            for qa in qa_pairs:
                f.write(json.dumps(qa.to_conversation_format(), ensure_ascii=False) + '\n')
    
    def _save_chatml_format(self, qa_pairs: List[QAPair], filepath: str):
        """保存为ChatML格式（适用于Qwen/Llama-3等模型SFT）"""
        with open(filepath, 'w', encoding='utf-8') as f:
            for qa in qa_pairs:
                f.write(json.dumps(qa.to_chatml_format(), ensure_ascii=False) + '\n')
    
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

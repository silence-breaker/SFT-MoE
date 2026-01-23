#!/usr/bin/env python3
"""
RANSTRUCT Post-Processor: 数据集质量修复工具

解决三大质量问题:
1. 元认知泄漏 (38.1%) - 答案中包含 "Based on the provided context..."
2. 缩写猜谜幻觉 (69% of acronym questions) - 小模型对O-RAN缩写不熟悉
3. 代码废话文学 (76.4% lack design insight) - 只解释语法不解释意图

用法:
    python post_processor.py --input ranstruct_dataset_*.jsonl --output cleaned_dataset.jsonl
    
    # 仅分析不修改
    python post_processor.py --input ranstruct_dataset_*.jsonl --analyze-only
    
    # 强过滤模式（丢弃而非修复）
    python post_processor.py --input ranstruct_dataset_*.jsonl --output cleaned.jsonl --strict
"""

import json
import re
import argparse
from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Dict, Tuple, Optional, Any
from enum import Enum, auto
import sys


class QualityIssue(Enum):
    """质量问题类型"""
    META_COGNITIVE_LEAK = auto()      # 元认知泄漏
    ACRONYM_HALLUCINATION = auto()    # 缩写幻觉
    SHALLOW_CODE_EXPLAIN = auto()     # 浅层代码解释
    TAUTOLOGY = auto()                # 同义反复
    TOO_SHORT = auto()                # 答案过短
    UNCERTAINTY = auto()              # 不确定性表达
    DOCUMENT_STRUCTURE_Q = auto()     # 文档结构类问题
    REJECTION_ANSWER = auto()         # 拒绝/不知道类答案
    CITATION_MARKERS = auto()         # 引用标记干扰
    ENTITY_INCONSISTENCY = auto()     # 新增: 实体不一致（问题与答案实体不匹配）
    LOW_RETRIEVAL_CONFIDENCE = auto() # 新增: 低检索置信度


@dataclass
class QualityReport:
    """单条QA的质量报告"""
    issues: List[QualityIssue] = field(default_factory=list)
    issue_details: Dict[str, str] = field(default_factory=dict)
    fixable: bool = True
    fixed_answer: Optional[str] = None
    confidence_score: float = 1.0  # 0-1, 越低越可能有问题


# ============================================================================
# O-RAN 专业术语词典 (用于修复缩写幻觉)
# ============================================================================
ORAN_ACRONYM_GLOSSARY = {
    # 核心架构组件
    "O-RAN": "Open Radio Access Network",
    "O-RU": "O-RAN Radio Unit",
    "O-DU": "O-RAN Distributed Unit", 
    "O-CU": "O-RAN Central Unit",
    "O-CU-CP": "O-RAN Central Unit - Control Plane",
    "O-CU-UP": "O-RAN Central Unit - User Plane",
    "RIC": "RAN Intelligent Controller",
    "Near-RT RIC": "Near-Real-Time RAN Intelligent Controller",
    "Non-RT RIC": "Non-Real-Time RAN Intelligent Controller",
    "SMO": "Service Management and Orchestration",
    
    # 接口
    "E1": "Interface between O-CU-CP and O-CU-UP",
    "E2": "Interface between Near-RT RIC and O-CU/O-DU",
    "F1": "Interface between O-CU and O-DU",
    "F1-C": "F1 Control Plane Interface",
    "F1-U": "F1 User Plane Interface",
    "A1": "Interface between Non-RT RIC and Near-RT RIC",
    "O1": "Interface between SMO and O-RAN managed elements",
    "O2": "Interface between SMO and O-Cloud",
    "Open FH": "Open Fronthaul Interface (between O-DU and O-RU)",
    
    # 协议和功能
    "xApp": "Application running on Near-RT RIC",
    "rApp": "Application running on Non-RT RIC (also called r1App)",
    "PDCP": "Packet Data Convergence Protocol",
    "RLC": "Radio Link Control",
    "MAC": "Medium Access Control",
    "PHY": "Physical Layer",
    "RRC": "Radio Resource Control",
    "SDAP": "Service Data Adaptation Protocol",
    "NGAP": "NG Application Protocol",
    "GTP-U": "GPRS Tunneling Protocol User Plane",
    "SCTP": "Stream Control Transmission Protocol",
    
    # 物理层信号
    "PT-RS": "Phase Tracking Reference Signal",
    "DM-RS": "Demodulation Reference Signal", 
    "CSI-RS": "Channel State Information Reference Signal",
    "SRS": "Sounding Reference Signal",
    "SSB": "Synchronization Signal Block",
    "PBCH": "Physical Broadcast Channel",
    "PDSCH": "Physical Downlink Shared Channel",
    "PDCCH": "Physical Downlink Control Channel",
    "PUSCH": "Physical Uplink Shared Channel",
    "PUCCH": "Physical Uplink Control Channel",
    "PRACH": "Physical Random Access Channel",
    
    # 资源和调度
    "PRB": "Physical Resource Block",
    "RB": "Resource Block",
    "RE": "Resource Element",
    "OFDM": "Orthogonal Frequency Division Multiplexing",
    "TTI": "Transmission Time Interval",
    "HARQ": "Hybrid Automatic Repeat Request",
    "MCS": "Modulation and Coding Scheme",
    "CQI": "Channel Quality Indicator",
    "PMI": "Precoding Matrix Indicator",
    "RI": "Rank Indicator",
    
    # 网络和管理
    "UE": "User Equipment",
    "gNB": "gNodeB (5G Base Station)",
    "eNB": "eNodeB (4G Base Station)",
    "AMF": "Access and Mobility Management Function",
    "UPF": "User Plane Function",
    "NSSAI": "Network Slice Selection Assistance Information",
    "PLMN": "Public Land Mobile Network",
    "TAC": "Tracking Area Code",
    "PCI": "Physical Cell Identity",
    
    # O-RAN特有
    "FAPI": "Functional Application Platform Interface",
    "nFAPI": "Network FAPI",
    "WG": "Working Group",
    "CUS-Plane": "Control, User, and Synchronization Plane",
    "M-Plane": "Management Plane",
    "O-Cloud": "O-RAN Cloud Platform",
}


# ============================================================================
# 元认知泄漏模式 (需要清除的短语) - v2.0 增强版
# ============================================================================
META_COGNITIVE_PATTERNS = [
    # 直接引用上下文 - 严重问题
    (r'\[Document \d+\]:?\s*', ''),
    (r'\[Doc\.? ?\d+\]:?\s*', ''),
    (r'\[Source \d+\]:?\s*', ''),
    (r'\[Ref\.? ?\d+\]:?\s*', ''),
    (r'\(Document \d+\)\s*', ''),
    (r'\(Source: [^)]+\)\s*', ''),
    
    # "According to..." 系列 - 最常见的泄漏
    (r'^According to the (provided |given )?(context|documents?|text|information|passage|excerpt)[,\s]*', ''),
    (r'^Based on the (provided |given )?(context|documents?|text|information|passage|excerpt)[,\s]*', ''),
    (r'^From the (provided |given )?(context|documents?|text|information|passage|excerpt)[,\s]*', ''),
    (r'^In the (provided |given )?(context|documents?|text|information)[,\s]*', ''),
    (r'^As (stated|mentioned|described|noted|indicated) in the (context|documents?|text)[,\s]*', ''),
    (r'^The (provided |given )?(context|documents?|text|passage) (shows?|indicates?|mentions?|states?|describes?|explains?)[,\s]*(that )?', ''),
    (r'^Looking at the (provided |given )?(context|documents?|text)[,\s]*', ''),
    (r'^Referring to the (provided |given )?(context|documents?|text)[,\s]*', ''),
    
    # 中间位置的引用
    (r', as (stated|mentioned|described) in the (context|documents?|text),', ','),
    (r' according to the (context|documents?|text)', ''),
    (r' as per the (provided |given )?(documents?|text)', ''),
    
    # 不确定性表达开头（保守处理）
    (r'^(Well, |So, |Now, |Actually, |Basically, |Essentially, )', ''),
    (r'^I (would |might |could )?(say|think|believe|guess) that ', ''),
    (r"^I'm not (entirely |completely )?(sure|certain),? but ", ''),
    (r'^Let me (explain|describe|elaborate)[:\s]*', ''),
    
    # 元评论
    (r'(As|Like) (I |we )?(mentioned|stated|said|noted) (earlier|before|above)[,\s]*', ''),
]


# ============================================================================
# 文档结构类问题模式 (新增)
# ============================================================================
DOCUMENT_STRUCTURE_QUESTION_PATTERNS = [
    r'section\s+\d+',
    r'chapter\s+\d+',
    r'clause\s+\d+',
    r'paragraph\s+\d+',
    r'page\s+\d+',
    r'figure\s+\d+',
    r'table\s+\d+',
    r'annex\s+[a-z\d]+',
    r'appendix\s+[a-z\d]+',
    r'what is the title',
    r'what are the (chapter|section)',
    r'in which section',
    r'on which page',
    r'what does the document',
    r'what is (mentioned|stated|listed|described) in',
    r'how many .* (mentioned|listed)',
    r'list all .* mentioned',
]


# ============================================================================
# 拒绝/不知道类答案模式 (新增)
# ============================================================================
REJECTION_ANSWER_PATTERNS = [
    r'not provided',
    r'not mentioned',
    r'not specified',
    r'not available',
    r'not given',
    r'not stated',
    r'not found',
    r'cannot be found',
    r'cannot find',
    r'context does not',
    r'document does not',
    r'information is not',
    r'no information (about|on)',
    r'insufficient (information|data)',
    r'not enough information',
    r'i cannot',
    r"i can't",
    r'unable to (determine|answer|find)',
    r'would need more',
    r'INSUFFICIENT_DATA',
]


# ============================================================================
# 引用标记模式 (新增)
# ============================================================================
CITATION_MARKER_PATTERNS = [
    (r'</?doc\d*>', ''),
    (r'</?document\d*>', ''),
    (r'</?source\d*>', ''),
    (r'</?context>', ''),
    (r'</?reference\d*>', ''),
    (r'</?excerpt>', ''),
]


# ============================================================================
# 浅层解释模式检测
# ============================================================================
SHALLOW_EXPLANATION_PATTERNS = [
    r'because (it|the|its) (is|has|returns?|takes?) (a |an |the )?',
    r'the (function|method|class) (simply |just )?(does|performs|returns)',
    r'as (the |its )?(name|signature) (suggests?|implies?|indicates?)',
    r'this (is |does )?exactly what',
    r'the return type is \w+\.',
    r'it returns? \w+ (because|since)',
    r'this (function|method|class) is (used|called) to',
]


# ============================================================================
# 实体一致性检查规则 (Entity Consistency Rules)
# 用于后处理阶段检测问题与答案之间的实体不匹配
# ============================================================================
ENTITY_CONSISTENCY_RULES = {
    # 接口 -> 答案必须提到相关实体
    "F1": {
        "question_patterns": [r'\bF1\b', r'\bF1-C\b', r'\bF1-U\b', r'F1 interface'],
        "answer_required": ["O-CU", "O-DU", "CU", "DU", "gNB-CU", "gNB-DU", "central unit", "distributed unit"],
        "answer_forbidden_dominant": ["O-RU", "RU", "radio unit", "fronthaul"],  # 如果这些占主导说明幻觉
    },
    "E1": {
        "question_patterns": [r'\bE1\b', r'E1 interface'],
        "answer_required": ["O-CU-CP", "O-CU-UP", "CU-CP", "CU-UP", "control plane", "user plane"],
        "answer_forbidden_dominant": ["O-DU", "O-RU", "DU", "RU"],
    },
    "E2": {
        "question_patterns": [r'\bE2\b', r'E2 interface', r'E2AP'],
        "answer_required": ["RIC", "Near-RT RIC", "xApp", "E2 node", "E2SM"],
        "answer_forbidden_dominant": [],
    },
    "Fronthaul": {
        "question_patterns": [r'fronthaul', r'Open FH', r'\bFH\b', r'O-RU.*O-DU', r'O-DU.*O-RU'],
        "answer_required": ["O-RU", "O-DU", "RU", "DU", "eCPRI", "radio unit"],
        "answer_forbidden_dominant": ["E1", "E2", "O-CU-CP", "O-CU-UP", "AMF"],
    },
    "A1": {
        "question_patterns": [r'\bA1\b', r'A1 interface'],
        "answer_required": ["Non-RT RIC", "Near-RT RIC", "policy", "rApp"],
        "answer_forbidden_dominant": [],
    },
    "NGAP": {
        "question_patterns": [r'\bNGAP\b', r'NG interface'],
        "answer_required": ["AMF", "5GC", "5G Core", "core network", "N2"],
        "answer_forbidden_dominant": ["O-RU", "fronthaul"],
    },
    # 协议层
    "PDCP": {
        "question_patterns": [r'\bPDCP\b'],
        "answer_required": ["PDCP", "ciphering", "integrity", "header compression", "sequence number"],
        "answer_forbidden_dominant": [],
    },
    "RLC": {
        "question_patterns": [r'\bRLC\b'],
        "answer_required": ["RLC", "ARQ", "segmentation", "AM", "UM", "acknowledged", "unacknowledged"],
        "answer_forbidden_dominant": [],
    },
    "MAC": {
        "question_patterns": [r'\bMAC\b(?! address)', r'MAC scheduler', r'MAC layer'],
        "answer_required": ["MAC", "scheduler", "HARQ", "resource", "multiplexing"],
        "answer_forbidden_dominant": [],
    },
    # RIC 相关
    "xApp": {
        "question_patterns": [r'\bxApp\b', r'\bx-App\b'],
        "answer_required": ["xApp", "Near-RT RIC", "E2", "application"],
        "answer_forbidden_dominant": ["Non-RT RIC", "rApp"],
    },
    "rApp": {
        "question_patterns": [r'\brApp\b', r'\br-App\b', r'r1App'],
        "answer_required": ["rApp", "Non-RT RIC", "A1", "SMO"],
        "answer_forbidden_dominant": ["Near-RT RIC", "xApp", "E2"],
    },
}


class PostProcessor:
    """数据集后处理器"""
    
    def __init__(self, strict_mode: bool = False, min_retrieval_score: float = 0.35):
        """
        Args:
            strict_mode: 严格模式下，有问题的数据直接丢弃；宽松模式下尝试修复
            min_retrieval_score: 最低检索置信度阈值
        """
        self.strict_mode = strict_mode
        self.min_retrieval_score = min_retrieval_score
        self.stats = {
            'total': 0,
            'issues_found': 0,
            'fixed': 0,
            'discarded': 0,
            'clean': 0,
            'by_issue': {issue: 0 for issue in QualityIssue}
        }
    
    def _check_entity_consistency(self, question: str, answer: str) -> Tuple[bool, str]:
        """
        检查问题与答案之间的实体一致性
        
        Args:
            question: 问题文本
            answer: 答案文本
            
        Returns:
            (is_consistent, reason)
        """
        q_lower = question.lower()
        a_lower = answer.lower()
        
        for rule_name, rule in ENTITY_CONSISTENCY_RULES.items():
            # 检查问题是否匹配该规则
            question_matches = any(
                re.search(pattern, question, re.IGNORECASE) 
                for pattern in rule["question_patterns"]
            )
            
            if not question_matches:
                continue
            
            # 问题匹配了，检查答案
            found_required = sum(
                1 for entity in rule["answer_required"] 
                if entity.lower() in a_lower
            )
            
            # 至少需要找到 1 个相关实体
            if found_required == 0:
                return False, f"问题涉及 {rule_name}，但答案未提及任何相关实体"
            
            # 检查禁止实体是否占主导
            forbidden_count = sum(
                a_lower.count(entity.lower()) 
                for entity in rule.get("answer_forbidden_dominant", [])
            )
            required_count = sum(
                a_lower.count(entity.lower()) 
                for entity in rule["answer_required"]
                if entity.lower() in a_lower
            )
            
            if forbidden_count > required_count * 2:
                return False, f"问题涉及 {rule_name}，但答案主要讲的是不相关内容（实体不匹配）"
        
        return True, "通过实体一致性检查"
    
    def _check_retrieval_confidence(self, metadata: dict) -> Tuple[bool, float]:
        """
        检查检索置信度
        
        Args:
            metadata: QA 的元数据
            
        Returns:
            (is_confident, avg_score)
        """
        retrieval_scores = metadata.get("retrieval_scores", [])
        if not retrieval_scores:
            return True, 0.0  # 没有分数信息，跳过检查
        
        avg_score = sum(retrieval_scores) / len(retrieval_scores)
        max_score = max(retrieval_scores)
        
        # 检查最高分是否达到阈值
        if max_score < self.min_retrieval_score:
            return False, max_score
        
        return True, max_score
    
    def analyze_qa(self, question: str, answer: str, metadata: dict) -> QualityReport:
        """分析单条QA的质量问题 (v2.0 增强版)"""
        report = QualityReport()
        q_lower = question.lower()
        a_lower = answer.lower()
        
        # ============================================================
        # 1. 检测元认知泄漏 (最高优先级)
        # ============================================================
        for pattern, _ in META_COGNITIVE_PATTERNS:
            if re.search(pattern, answer, re.IGNORECASE):
                report.issues.append(QualityIssue.META_COGNITIVE_LEAK)
                report.issue_details['meta_cognitive'] = pattern[:50]
                break
        
        # ============================================================
        # 2. 新增: 检测文档结构类问题 (直接丢弃，不修复)
        # ============================================================
        for pattern in DOCUMENT_STRUCTURE_QUESTION_PATTERNS:
            if re.search(pattern, q_lower):
                report.issues.append(QualityIssue.DOCUMENT_STRUCTURE_Q)
                report.issue_details['doc_structure'] = pattern[:30]
                report.fixable = False  # 无法修复，只能丢弃
                break
        
        # ============================================================
        # 3. 新增: 检测拒绝/不知道类答案 (负样本污染)
        # ============================================================
        for pattern in REJECTION_ANSWER_PATTERNS:
            if re.search(pattern, a_lower):
                report.issues.append(QualityIssue.REJECTION_ANSWER)
                report.issue_details['rejection'] = pattern[:30]
                report.fixable = False  # 无法修复，只能丢弃
                report.confidence_score *= 0.3
                break
        
        # ============================================================
        # 4. 新增: 检测引用标记干扰 (可修复)
        # ============================================================
        for pattern, _ in CITATION_MARKER_PATTERNS:
            if re.search(pattern, answer, re.IGNORECASE):
                report.issues.append(QualityIssue.CITATION_MARKERS)
                report.issue_details['citation'] = pattern[:30]
                break
        
        # ============================================================
        # 5. 检测缩写幻觉
        # ============================================================
        if self._is_acronym_question(question):
            acronym = self._extract_acronym(question)
            if acronym and not self._answer_has_correct_expansion(acronym, answer):
                report.issues.append(QualityIssue.ACRONYM_HALLUCINATION)
                report.issue_details['acronym'] = acronym
                report.confidence_score *= 0.5
        
        # ============================================================
        # 6. 检测浅层代码解释
        # ============================================================
        source_type = metadata.get('source_type', '')
        if source_type in ['srsran_code', 'codeset']:
            shallow_count = sum(1 for p in SHALLOW_EXPLANATION_PATTERNS 
                               if re.search(p, a_lower))
            design_keywords = ['design', 'reason', 'why', 'intent', 'purpose', 
                             'goal', 'architecture', 'pattern', 'decision', 'trade-off']
            has_design = any(kw in a_lower for kw in design_keywords)
            
            if shallow_count >= 2 and not has_design:
                report.issues.append(QualityIssue.SHALLOW_CODE_EXPLAIN)
                report.issue_details['shallow_patterns'] = str(shallow_count)
        
        # ============================================================
        # 7. 检测同义反复
        # ============================================================
        q_words = set(re.findall(r'\b\w{4,}\b', q_lower))
        a_first_sentence = a_lower.split('.')[0] if '.' in a_lower else a_lower[:200]
        a_words = set(re.findall(r'\b\w{4,}\b', a_first_sentence))
        overlap = len(q_words & a_words) / max(len(q_words), 1)
        if overlap > 0.7 and len(answer) < 300:
            report.issues.append(QualityIssue.TAUTOLOGY)
            report.issue_details['overlap'] = f'{overlap:.2f}'
        
        # ============================================================
        # 8. 检测答案过短
        # ============================================================
        if len(answer) < 100:
            report.issues.append(QualityIssue.TOO_SHORT)
            report.issue_details['length'] = str(len(answer))
        
        # ============================================================
        # 9. 检测过多不确定性
        # ============================================================
        uncertainty_patterns = [r'\bmight\b', r'\bcould be\b', r'\bperhaps\b', 
                               r'\bpossibly\b', r'\bmaybe\b', r'\bnot sure\b']
        uncertainty_count = sum(len(re.findall(p, a_lower)) for p in uncertainty_patterns)
        if uncertainty_count >= 3:
            report.issues.append(QualityIssue.UNCERTAINTY)
            report.issue_details['uncertainty_count'] = str(uncertainty_count)
        
        # ============================================================
        # 10. 新增: 实体一致性检查 (Entity Consistency Check)
        # 检测问题与答案之间的实体不匹配（幻觉检测）
        # ============================================================
        entity_consistent, entity_reason = self._check_entity_consistency(question, answer)
        if not entity_consistent:
            report.issues.append(QualityIssue.ENTITY_INCONSISTENCY)
            report.issue_details['entity_mismatch'] = entity_reason[:80]
            report.fixable = False  # 实体不匹配通常意味着幻觉，无法修复
            report.confidence_score *= 0.4
        
        # ============================================================
        # 11. 新增: 检索置信度检查 (Retrieval Confidence Check)
        # 检测检索分数过低的数据（可能导致幻觉）
        # ============================================================
        retrieval_confident, max_score = self._check_retrieval_confidence(metadata)
        if not retrieval_confident:
            report.issues.append(QualityIssue.LOW_RETRIEVAL_CONFIDENCE)
            report.issue_details['max_retrieval_score'] = f'{max_score:.3f}'
            report.confidence_score *= 0.5
            # 低置信度不一定是幻觉，保留 fixable 状态由其他检查决定
        
        # ============================================================
        # 最终判断是否可修复
        # ============================================================
        unfixable_issues = {
            QualityIssue.ACRONYM_HALLUCINATION,
            QualityIssue.TAUTOLOGY,
            QualityIssue.DOCUMENT_STRUCTURE_Q,
            QualityIssue.REJECTION_ANSWER,
            QualityIssue.ENTITY_INCONSISTENCY,  # 新增: 实体不匹配不可修复
        }
        if any(issue in unfixable_issues for issue in report.issues):
            report.fixable = False
        if QualityIssue.TOO_SHORT in report.issues and len(answer) < 50:
            report.fixable = False
        
        return report
    
    def _is_acronym_question(self, question: str) -> bool:
        """判断是否是缩写定义类问题"""
        patterns = [
            r'what (does|is) [\w-]+ (stand for|mean|refer to)',
            r'(define|explain|describe) [\w-]+',
            r'what is (the |an? )?(full |expanded )?(form|name|meaning) of',
            r'[\w-]+ (stands for|means|refers to)',
        ]
        q_lower = question.lower()
        return any(re.search(p, q_lower) for p in patterns)
    
    def _extract_acronym(self, question: str) -> Optional[str]:
        """从问题中提取缩写"""
        # 查找大写缩写或带连字符的术语
        matches = re.findall(r'\b([A-Z][A-Z0-9-]{1,10})\b', question)
        if matches:
            return matches[0]
        
        # 查找O-RAN风格术语
        matches = re.findall(r'\b(O-[A-Z]{2,}(?:-[A-Z]{2,})?)\b', question, re.IGNORECASE)
        if matches:
            return matches[0].upper()
        
        return None
    
    def _answer_has_correct_expansion(self, acronym: str, answer: str) -> bool:
        """检查答案是否包含正确的缩写展开"""
        acronym_upper = acronym.upper().replace('-', '')
        
        # 尝试多种变体
        variants = [acronym, acronym.upper(), acronym.replace('-', '')]
        
        for variant in variants:
            if variant in ORAN_ACRONYM_GLOSSARY:
                expansion = ORAN_ACRONYM_GLOSSARY[variant].lower()
                # 检查展开形式的关键词是否出现在答案中
                key_words = [w for w in expansion.split() if len(w) > 3]
                matches = sum(1 for w in key_words if w in answer.lower())
                if matches >= len(key_words) * 0.6:  # 60%以上关键词匹配
                    return True
        
        return False
    
    def fix_answer(self, answer: str, report: QualityReport, metadata: dict) -> str:
        """尝试修复答案中的问题 (v2.0 增强版)"""
        fixed = answer
        
        # ============================================================
        # 1. 修复元认知泄漏 (最高优先级)
        # ============================================================
        if QualityIssue.META_COGNITIVE_LEAK in report.issues:
            for pattern, replacement in META_COGNITIVE_PATTERNS:
                fixed = re.sub(pattern, replacement, fixed, flags=re.IGNORECASE)
            
            # 清理开头的空白和逗号
            fixed = re.sub(r'^[\s,;:]+', '', fixed)
            
            # 确保首字母大写
            if fixed and fixed[0].islower():
                fixed = fixed[0].upper() + fixed[1:]
        
        # ============================================================
        # 2. 新增: 修复引用标记干扰
        # ============================================================
        if QualityIssue.CITATION_MARKERS in report.issues:
            for pattern, replacement in CITATION_MARKER_PATTERNS:
                fixed = re.sub(pattern, replacement, fixed, flags=re.IGNORECASE)
            
            # 清理多余空白
            fixed = re.sub(r'\s+', ' ', fixed)
            fixed = fixed.strip()
        
        # ============================================================
        # 3. 为缩写问题补充正确定义（如果词典中有）
        # ============================================================
        if QualityIssue.ACRONYM_HALLUCINATION in report.issues:
            acronym = report.issue_details.get('acronym', '')
            if acronym in ORAN_ACRONYM_GLOSSARY:
                expansion = ORAN_ACRONYM_GLOSSARY[acronym]
                prefix = f"{acronym} stands for {expansion}. "
                if prefix.lower() not in fixed.lower():
                    fixed = prefix + fixed
        
        # ============================================================
        # 4. 新增: 最终清理 - ComplianceChecker
        # ============================================================
        # 截断 "Based on...", "According to..." 前缀（如果仍有残留）
        compliance_patterns = [
            r'^(Based on|According to|Referring to|Looking at|From|In) (the |this |these )?(provided |given )?(context|document|text|information|passage|source|excerpt)[,\s]*',
            r'^(As |Like )?(stated|mentioned|described|noted|indicated) (in|by) (the |this )?(context|document|text)[,\s]*',
        ]
        for pattern in compliance_patterns:
            fixed = re.sub(pattern, '', fixed, flags=re.IGNORECASE)
        
        # 最终清理
        fixed = re.sub(r'^[\s,;:]+', '', fixed)
        fixed = re.sub(r'\s+', ' ', fixed)
        fixed = fixed.strip()
        
        # 确保首字母大写
        if fixed and fixed[0].islower():
            fixed = fixed[0].upper() + fixed[1:]
        
        return fixed
    
    def process_file(self, input_path: Path, output_path: Optional[Path] = None) -> dict:
        """处理单个文件"""
        results = []
        
        with open(input_path, 'r', encoding='utf-8') as f:
            for line in f:
                if not line.strip():
                    continue
                
                self.stats['total'] += 1
                data = json.loads(line)
                
                question = data.get('question', '')
                answer = data.get('answer', '')
                metadata = data.get('metadata', {})
                
                report = self.analyze_qa(question, answer, metadata)
                
                if report.issues:
                    self.stats['issues_found'] += 1
                    for issue in report.issues:
                        self.stats['by_issue'][issue] += 1
                    
                    if self.strict_mode or not report.fixable:
                        self.stats['discarded'] += 1
                        continue
                    else:
                        # 尝试修复
                        fixed_answer = self.fix_answer(answer, report, metadata)
                        data['answer'] = fixed_answer
                        data['metadata']['quality_fixed'] = True
                        data['metadata']['original_issues'] = [i.name for i in report.issues]
                        self.stats['fixed'] += 1
                else:
                    self.stats['clean'] += 1
                
                results.append(data)
        
        # 写入输出文件
        if output_path:
            with open(output_path, 'w', encoding='utf-8') as f:
                for item in results:
                    f.write(json.dumps(item, ensure_ascii=False) + '\n')
        
        return self.stats
    
    def process_multiple_files(self, input_pattern: str, output_path: Path) -> dict:
        """处理多个文件"""
        from glob import glob
        
        all_results = []
        
        for input_file in sorted(glob(input_pattern)):
            print(f"Processing: {input_file}")
            
            with open(input_file, 'r', encoding='utf-8') as f:
                for line in f:
                    if not line.strip():
                        continue
                    
                    self.stats['total'] += 1
                    data = json.loads(line)
                    
                    question = data.get('question', '')
                    answer = data.get('answer', '')
                    metadata = data.get('metadata', {})
                    
                    report = self.analyze_qa(question, answer, metadata)
                    
                    if report.issues:
                        self.stats['issues_found'] += 1
                        for issue in report.issues:
                            self.stats['by_issue'][issue] += 1
                        
                        if self.strict_mode or not report.fixable:
                            self.stats['discarded'] += 1
                            continue
                        else:
                            fixed_answer = self.fix_answer(answer, report, metadata)
                            data['answer'] = fixed_answer
                            data['metadata']['quality_fixed'] = True
                            data['metadata']['original_issues'] = [i.name for i in report.issues]
                            self.stats['fixed'] += 1
                    else:
                        self.stats['clean'] += 1
                    
                    all_results.append(data)
        
        # 写入输出文件
        with open(output_path, 'w', encoding='utf-8') as f:
            for item in all_results:
                f.write(json.dumps(item, ensure_ascii=False) + '\n')
        
        return self.stats
    
    def print_report(self):
        """打印处理报告"""
        print("\n" + "="*70)
        print("RANSTRUCT 数据集质量处理报告")
        print("="*70)
        
        print(f"\n📊 总体统计:")
        print(f"   总条目数:     {self.stats['total']:,}")
        print(f"   发现问题:     {self.stats['issues_found']:,} ({self.stats['issues_found']/max(self.stats['total'],1)*100:.1f}%)")
        print(f"   干净数据:     {self.stats['clean']:,} ({self.stats['clean']/max(self.stats['total'],1)*100:.1f}%)")
        print(f"   已修复:       {self.stats['fixed']:,}")
        print(f"   已丢弃:       {self.stats['discarded']:,}")
        
        print(f"\n🔍 问题类型分布:")
        for issue, count in sorted(self.stats['by_issue'].items(), key=lambda x: -x[1]):
            if count > 0:
                pct = count / max(self.stats['total'], 1) * 100
                issue_name = issue.name.replace('_', ' ').title()
                print(f"   {issue_name:30} {count:6,} ({pct:5.1f}%)")
        
        output_count = self.stats['clean'] + self.stats['fixed']
        print(f"\n✅ 输出数据: {output_count:,} 条 (原始 {self.stats['total']:,} 条的 {output_count/max(self.stats['total'],1)*100:.1f}%)")


def analyze_only(input_pattern: str):
    """仅分析模式，不修改数据"""
    from glob import glob
    
    processor = PostProcessor(strict_mode=False)
    
    issue_examples = {issue: [] for issue in QualityIssue}
    
    for input_file in sorted(glob(input_pattern)):
        with open(input_file, 'r', encoding='utf-8') as f:
            for line in f:
                if not line.strip():
                    continue
                
                processor.stats['total'] += 1
                data = json.loads(line)
                
                question = data.get('question', '')
                answer = data.get('answer', '')
                metadata = data.get('metadata', {})
                
                report = processor.analyze_qa(question, answer, metadata)
                
                if report.issues:
                    processor.stats['issues_found'] += 1
                    for issue in report.issues:
                        processor.stats['by_issue'][issue] += 1
                        if len(issue_examples[issue]) < 2:
                            issue_examples[issue].append({
                                'q': question[:100],
                                'a': answer[:200],
                                'details': report.issue_details
                            })
                else:
                    processor.stats['clean'] += 1
    
    processor.print_report()
    
    print("\n" + "="*70)
    print("问题示例")
    print("="*70)
    
    for issue, examples in issue_examples.items():
        if examples:
            print(f"\n【{issue.name}】")
            for ex in examples:
                print(f"  Q: {ex['q']}...")
                print(f"  A: {ex['a']}...")
                print(f"  Details: {ex['details']}")
                print()


def main():
    parser = argparse.ArgumentParser(
        description='RANSTRUCT 数据集后处理工具',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    
    parser.add_argument('--input', '-i', required=True,
                       help='输入文件路径或通配符模式')
    parser.add_argument('--output', '-o',
                       help='输出文件路径')
    parser.add_argument('--analyze-only', action='store_true',
                       help='仅分析，不修改数据')
    parser.add_argument('--strict', action='store_true',
                       help='严格模式：丢弃有问题的数据而非修复')
    
    args = parser.parse_args()
    
    if args.analyze_only:
        analyze_only(args.input)
    else:
        if not args.output:
            print("错误: 非分析模式需要指定 --output 参数")
            sys.exit(1)
        
        processor = PostProcessor(strict_mode=args.strict)
        
        if '*' in args.input:
            processor.process_multiple_files(args.input, Path(args.output))
        else:
            processor.process_file(Path(args.input), Path(args.output))
        
        processor.print_report()
        print(f"\n📁 输出文件: {args.output}")


if __name__ == '__main__':
    main()

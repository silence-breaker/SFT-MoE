#!/usr/bin/env python3
"""
RANSTRUCT 数据集质量改进模块

本模块提供数据质量提升功能，不修改现有数据，只用于：
1. 数据集后处理过滤
2. 新生成数据的质量检测
3. RAG chunk 切分优化建议

注意：所有改进都是非破坏性的，不会覆盖原有数据
"""

import re
import json
import logging
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass

logger = logging.getLogger(__name__)


# ===================== 幻觉检测 =====================

@dataclass
class HallucinationCheckResult:
    """幻觉检测结果"""
    has_uncertainty: bool
    uncertainty_patterns: List[str]
    confidence_score: float  # 0-1, 越高越可信
    suggestion: str


class HallucinationDetector:
    """幻觉/不确定性检测器"""
    
    # 不确定性表述模式（按严重程度分级）
    HIGH_UNCERTAINTY_PATTERNS = [
        r'\bi believe\b',
        r'\bi think\b', 
        r'\bi assume\b',
        r'\bpresumably\b',
        r'\bnot entirely sure\b',
        r'\bi\'m not sure\b',
        r'\bthis might mean\b',
    ]
    
    MEDIUM_UNCERTAINTY_PATTERNS = [
        r'\bprobably\b',
        r'\bmight be\b',
        r'\bcould be\b',
        r'\bpossibly\b',
        r'\bit seems\b',
        r'\bappears to be\b',
        r'\blikely\b',
    ]
    
    LOW_UNCERTAINTY_PATTERNS = [
        r'\bgenerally\b',
        r'\btypically\b',
        r'\busually\b',
        r'\boften\b',
    ]
    
    # 过度推测的指标
    SPECULATION_INDICATORS = [
        r'\bwe would need to\b',
        r'\badditional.*would be needed\b',
        r'\bnot explicitly\b',
        r'\bdoes not.*mention\b',
        r'\bcontext does not\b',
    ]
    
    def check(self, answer: str) -> HallucinationCheckResult:
        """检测答案中的幻觉/不确定性"""
        answer_lower = answer.lower()
        found_patterns = []
        severity_score = 0
        
        # 检测高严重度模式
        for pattern in self.HIGH_UNCERTAINTY_PATTERNS:
            if re.search(pattern, answer_lower):
                found_patterns.append(f"HIGH: {pattern}")
                severity_score += 3
        
        # 检测中等严重度模式
        for pattern in self.MEDIUM_UNCERTAINTY_PATTERNS:
            if re.search(pattern, answer_lower):
                found_patterns.append(f"MEDIUM: {pattern}")
                severity_score += 2
        
        # 检测低严重度模式
        for pattern in self.LOW_UNCERTAINTY_PATTERNS:
            if re.search(pattern, answer_lower):
                found_patterns.append(f"LOW: {pattern}")
                severity_score += 1
        
        # 检测推测指标
        for pattern in self.SPECULATION_INDICATORS:
            if re.search(pattern, answer_lower):
                found_patterns.append(f"SPECULATION: {pattern}")
                severity_score += 2
        
        # 计算置信度分数 (反比于严重度)
        # 答案长度因子：长答案中偶尔出现不确定词汇是可接受的
        length_factor = min(len(answer) / 1000, 1.5)  # 长答案有更高容忍度
        adjusted_score = severity_score / max(length_factor, 1)
        
        confidence = max(0, 1 - adjusted_score / 10)
        
        # 生成建议
        if severity_score == 0:
            suggestion = "PASS: 答案无明显不确定性表述"
        elif severity_score <= 2:
            suggestion = "ACCEPTABLE: 轻微不确定性，可接受"
        elif severity_score <= 5:
            suggestion = "REVIEW: 建议人工审核此答案"
        else:
            suggestion = "REJECT: 答案包含过多推测性内容，建议过滤"
        
        return HallucinationCheckResult(
            has_uncertainty=len(found_patterns) > 0,
            uncertainty_patterns=found_patterns,
            confidence_score=confidence,
            suggestion=suggestion
        )


# ===================== 答案质量检测 =====================

class AnswerQualityChecker:
    """答案质量检测器"""
    
    # 低价值问答模式
    LOW_VALUE_PATTERNS = [
        r'^the copyright',
        r'copying or incorporation',
        r'prior written permission',
        r'register of associations',
        r'vat id',
    ]
    
    # 过度引用上下文的模式
    OVER_CITATION_PATTERN = r'\[Document \d+\]'
    
    def check_quality(self, question: str, answer: str, retrieval_scores: List[float]) -> Dict:
        """检查问答对质量"""
        issues = []
        score = 100  # 满分100
        
        q_lower = question.lower()
        a_lower = answer.lower()
        
        # 1. 检查是否是低价值问题（版权、注册信息等）
        for pattern in self.LOW_VALUE_PATTERNS:
            if re.search(pattern, q_lower) or re.search(pattern, a_lower[:200]):
                issues.append("LOW_VALUE: 问题涉及版权/法律声明等低价值内容")
                score -= 30
                break
        
        # 2. 检查检索分数
        if retrieval_scores:
            max_score = max(retrieval_scores)
            if max_score < 0.7:
                issues.append(f"LOW_RETRIEVAL: 最高检索分数仅 {max_score:.3f}")
                score -= 20
            elif max_score < 0.75:
                issues.append(f"MODERATE_RETRIEVAL: 检索分数一般 {max_score:.3f}")
                score -= 10
        
        # 3. 检查过度引用
        citations = re.findall(self.OVER_CITATION_PATTERN, answer)
        if len(citations) > 6:
            issues.append(f"OVER_CITATION: 答案引用了 {len(citations)} 次文档标记")
            score -= 10
        
        # 4. 检查答案长度合理性
        if len(answer) < 100:
            issues.append("TOO_SHORT: 答案过短")
            score -= 15
        elif len(answer) > 2500:
            issues.append("TOO_LONG: 答案可能冗余")
            score -= 5
        
        # 5. 幻觉检测
        hallucination_result = HallucinationDetector().check(answer)
        if hallucination_result.confidence_score < 0.7:
            issues.append(f"HALLUCINATION_RISK: {hallucination_result.suggestion}")
            score -= int((1 - hallucination_result.confidence_score) * 30)
        
        return {
            "score": max(0, score),
            "issues": issues,
            "pass": score >= 60,
            "hallucination_check": hallucination_result
        }


# ===================== 数据集过滤器 =====================

class DatasetFilter:
    """数据集过滤器 - 用于后处理已生成的数据"""
    
    def __init__(self, 
                 min_quality_score: int = 60,
                 min_retrieval_score: float = 0.7,
                 max_uncertainty_patterns: int = 3):
        self.min_quality_score = min_quality_score
        self.min_retrieval_score = min_retrieval_score
        self.max_uncertainty_patterns = max_uncertainty_patterns
        self.quality_checker = AnswerQualityChecker()
        self.hallucination_detector = HallucinationDetector()
    
    def filter_dataset(self, input_file: str, output_file: str) -> Dict:
        """
        过滤数据集，输出高质量子集
        
        Args:
            input_file: 输入的 jsonl 文件路径
            output_file: 输出的 jsonl 文件路径
            
        Returns:
            过滤统计信息
        """
        stats = {
            "total": 0,
            "passed": 0,
            "filtered_reasons": {}
        }
        
        with open(input_file, 'r', encoding='utf-8') as fin, \
             open(output_file, 'w', encoding='utf-8') as fout:
            
            for line in fin:
                if not line.strip():
                    continue
                    
                stats["total"] += 1
                data = json.loads(line)
                
                # 检查质量
                retrieval_scores = data.get("metadata", {}).get("retrieval_scores", [])
                quality = self.quality_checker.check_quality(
                    data["question"],
                    data["answer"],
                    retrieval_scores
                )
                
                if quality["pass"]:
                    stats["passed"] += 1
                    fout.write(line)
                else:
                    for issue in quality["issues"]:
                        reason = issue.split(":")[0]
                        stats["filtered_reasons"][reason] = \
                            stats["filtered_reasons"].get(reason, 0) + 1
        
        stats["pass_rate"] = stats["passed"] / stats["total"] if stats["total"] > 0 else 0
        return stats


# ===================== RAG Chunk 优化建议 =====================

class ChunkQualityAnalyzer:
    """Chunk 质量分析器"""
    
    @staticmethod
    def analyze_chunk(content: str, metadata: Dict) -> Dict:
        """分析单个 chunk 的质量"""
        issues = []
        
        # 1. 检查长度
        if len(content) < 100:
            issues.append("TOO_SHORT: chunk 过短，可能丢失上下文")
        
        # 2. 检查代码完整性
        if metadata.get("type") in ["srsran_code", "codeset"]:
            # 检查是否在函数中间断裂
            if content.strip().startswith('{') or content.strip().endswith('{'):
                issues.append("CODE_INCOMPLETE: 代码块可能不完整")
            
            # 检查括号平衡
            open_braces = content.count('{')
            close_braces = content.count('}')
            if abs(open_braces - close_braces) > 2:
                issues.append(f"UNBALANCED_BRACES: 括号不平衡 ({open_braces} vs {close_braces})")
        
        # 3. 检查表格完整性
        if '|' in content and metadata.get("type") == "oran_specification":
            lines = content.split('\n')
            table_lines = [l for l in lines if '|' in l]
            if table_lines:
                # 检查表头是否完整
                if not any('---' in l or '===' in l for l in table_lines[:3]):
                    issues.append("TABLE_HEADER_MISSING: 表格可能缺少表头")
        
        # 4. 检查是否是元数据/版权声明等低价值内容
        low_value_keywords = ['copyright', 'all rights reserved', 'register of associations']
        if any(kw in content.lower() for kw in low_value_keywords):
            issues.append("LOW_VALUE_CONTENT: chunk 包含版权/元数据信息")
        
        return {
            "length": len(content),
            "issues": issues,
            "quality_score": max(0, 100 - len(issues) * 20)
        }


# ===================== 改进的 Prompt 模板 =====================

IMPROVED_SYSTEM_PROMPT = """You are a precise technical assistant for O-RAN (Open Radio Access Network) documentation.

CRITICAL RULES:
1. ONLY use information EXPLICITLY stated in the provided context
2. NEVER speculate, assume, or infer beyond what is written
3. If information is not in the context, respond: "The provided context does not contain information about [topic]."
4. Do NOT use phrases like "probably", "might be", "could be", "I think", "it seems"
5. When citing specifications, include exact clause/section numbers when available
6. For code questions, reference specific function names, line numbers, or file paths

Your answers must be:
- Factual and verifiable from the context
- Technically precise using correct O-RAN terminology
- Concise without unnecessary elaboration"""

IMPROVED_ANSWER_PROMPT = """Based ONLY on the following context documents, answer the question.

Context:
{context}

Question: {question}

IMPORTANT:
- Provide ONLY information that is explicitly stated in the context
- If the context lacks sufficient information, clearly state this limitation
- Do NOT guess or make assumptions
- Reference specific document sections when possible

Answer:"""


# ===================== 命令行工具 =====================

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='RANSTRUCT 数据质量检查工具')
    subparsers = parser.add_subparsers(dest='command')
    
    # filter 命令
    filter_parser = subparsers.add_parser('filter', help='过滤数据集')
    filter_parser.add_argument('input', help='输入文件')
    filter_parser.add_argument('output', help='输出文件')
    filter_parser.add_argument('--min-score', type=int, default=60, help='最低质量分数')
    
    # analyze 命令
    analyze_parser = subparsers.add_parser('analyze', help='分析数据集质量')
    analyze_parser.add_argument('input', help='输入文件')
    analyze_parser.add_argument('--sample', type=int, default=100, help='抽样数量')
    
    args = parser.parse_args()
    
    if args.command == 'filter':
        print(f"正在过滤数据集: {args.input} -> {args.output}")
        filter_obj = DatasetFilter(min_quality_score=args.min_score)
        stats = filter_obj.filter_dataset(args.input, args.output)
        print(f"过滤完成:")
        print(f"  总数: {stats['total']}")
        print(f"  通过: {stats['passed']}")
        print(f"  通过率: {stats['pass_rate']:.1%}")
        print(f"  过滤原因分布: {stats['filtered_reasons']}")
    
    elif args.command == 'analyze':
        print(f"正在分析数据集: {args.input}")
        checker = AnswerQualityChecker()
        
        scores = []
        issue_counts = {}
        
        import random
        with open(args.input, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        sample_lines = random.sample(lines, min(args.sample, len(lines)))
        
        for line in sample_lines:
            if not line.strip():
                continue
            data = json.loads(line)
            retrieval_scores = data.get("metadata", {}).get("retrieval_scores", [])
            result = checker.check_quality(data["question"], data["answer"], retrieval_scores)
            scores.append(result["score"])
            for issue in result["issues"]:
                reason = issue.split(":")[0]
                issue_counts[reason] = issue_counts.get(reason, 0) + 1
        
        print(f"\n分析完成 (抽样 {len(scores)} 条):")
        print(f"  平均质量分数: {sum(scores)/len(scores):.1f}")
        print(f"  通过率 (>=60): {sum(1 for s in scores if s >= 60)/len(scores):.1%}")
        print(f"\n问题分布:")
        for issue, count in sorted(issue_counts.items(), key=lambda x: -x[1]):
            print(f"  {issue}: {count} ({count/len(scores)*100:.1f}%)")
    
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

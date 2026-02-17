#!/usr/bin/env python3
"""
RANSTRUCT 数据集质量验证工具

用于验证生成的数据集是否可以直接用于 SFT 训练。

使用方式:
    python validate_dataset.py --input output/ranstruct_dataset_cleaned.jsonl
    python validate_dataset.py --input output/ranstruct_dataset_cleaned.jsonl --export-sft chatml
"""

import json
import re
import argparse
from pathlib import Path
from collections import Counter
from typing import List, Dict, Tuple
import sys


# ============================================================================
# 质量检测规则
# ============================================================================

# 元认知泄漏模式（严重问题，会导致模型学到"读文档"的行为）
META_COGNITIVE_PATTERNS = [
    r'\[Document \d+\]:?\s*',
    r'\[Doc\.? ?\d+\]:?\s*',
    r'\[Source \d+\]:?\s*',
    r'^According to the (provided |given )?(context|documents?|text|information)',
    r'^Based on the (provided |given )?(context|documents?|text|information)',
    r'^From the (provided |given )?(context|documents?|text|information)',
    r'^In the (provided |given )?(context|documents?|text|information)',
    r'^The (provided |given )?(context|documents?|text|passage) (shows?|indicates?|mentions?|states?)',
    r', as (stated|mentioned|described) in the (context|documents?|text),',
    r' according to the (context|documents?|text)\b',
    r' as per the (provided |given )?(documents?|text)',
    r'</?doc\d*>',
    r'</?document\d*>',
]

# 拒答模式（会导致模型学到拒绝回答的行为）
REJECTION_PATTERNS = [
    r'^I cannot',
    r'^I can\'t',
    r'not provided in',
    r'not mentioned in',
    r'information is not available',
    r'insufficient (information|data)',
    r'INSUFFICIENT_DATA',
    r'cannot be determined',
    r'unable to (determine|answer|find)',
]

# O-RAN 技术术语（用于检测答案是否包含专业内容）
TECH_TERMS = [
    'O-RAN', 'O-CU', 'O-DU', 'O-RU', 'RIC', 'Near-RT RIC', 'Non-RT RIC',
    'F1', 'E1', 'E2', 'A1', 'O1', 'O2', 'Open Fronthaul',
    'PDCP', 'RLC', 'MAC', 'PHY', 'RRC', 'SDAP',
    'SCTP', 'SMO', 'xApp', 'rApp',
    'gNB', 'UE', 'AMF', 'UPF',
    'HARQ', 'scheduler', 'bearer',
]


def load_dataset(filepath: str) -> List[Dict]:
    """加载数据集"""
    samples = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            if line.strip():
                try:
                    samples.append(json.loads(line))
                except json.JSONDecodeError as e:
                    print(f"警告: 第 {line_num} 行 JSON 解析失败: {e}")
    return samples


def check_meta_cognitive_leak(answer: str) -> Tuple[bool, str]:
    """检查元认知泄漏"""
    for pattern in META_COGNITIVE_PATTERNS:
        match = re.search(pattern, answer, re.IGNORECASE | re.MULTILINE)
        if match:
            return True, match.group()[:50]
    return False, ""


def check_rejection(answer: str) -> Tuple[bool, str]:
    """检查拒答模式"""
    for pattern in REJECTION_PATTERNS:
        match = re.search(pattern, answer, re.IGNORECASE)
        if match:
            return True, match.group()[:50]
    return False, ""


def check_tech_terms(answer: str) -> int:
    """统计技术术语出现次数"""
    count = 0
    for term in TECH_TERMS:
        if term in answer:
            count += 1
    return count


def validate_dataset(samples: List[Dict]) -> Dict:
    """验证数据集质量"""
    results = {
        'total': len(samples),
        'issues': {
            'meta_cognitive_leak': [],
            'rejection_pattern': [],
            'no_tech_terms': [],
            'too_short': [],
            'too_long': [],
            'low_retrieval_score': [],
        },
        'stats': {
            'avg_question_length': 0,
            'avg_answer_length': 0,
            'tech_term_coverage': 0,
        }
    }
    
    question_lengths = []
    answer_lengths = []
    tech_term_counts = []
    
    for i, sample in enumerate(samples):
        question = sample.get('question', '')
        answer = sample.get('answer', '')
        metadata = sample.get('metadata', {})
        
        question_lengths.append(len(question))
        answer_lengths.append(len(answer))
        
        # 检查元认知泄漏
        has_leak, leak_text = check_meta_cognitive_leak(answer)
        if has_leak:
            results['issues']['meta_cognitive_leak'].append({
                'index': i,
                'pattern': leak_text,
                'question': question[:80]
            })
        
        # 检查拒答模式
        has_rejection, rejection_text = check_rejection(answer)
        if has_rejection:
            results['issues']['rejection_pattern'].append({
                'index': i,
                'pattern': rejection_text,
                'question': question[:80]
            })
        
        # 检查技术术语
        tech_count = check_tech_terms(answer)
        tech_term_counts.append(tech_count)
        if tech_count == 0:
            results['issues']['no_tech_terms'].append({
                'index': i,
                'question': question[:80]
            })
        
        # 检查长度
        if len(answer) < 100:
            results['issues']['too_short'].append({
                'index': i,
                'length': len(answer),
                'question': question[:80]
            })
        elif len(answer) > 3000:
            results['issues']['too_long'].append({
                'index': i,
                'length': len(answer),
                'question': question[:80]
            })
        
        # 检查检索分数
        retrieval_scores = metadata.get('retrieval_scores', [])
        if retrieval_scores and max(retrieval_scores) < 0.35:
            results['issues']['low_retrieval_score'].append({
                'index': i,
                'max_score': max(retrieval_scores),
                'question': question[:80]
            })
    
    # 计算统计信息
    if samples:
        results['stats']['avg_question_length'] = sum(question_lengths) / len(question_lengths)
        results['stats']['avg_answer_length'] = sum(answer_lengths) / len(answer_lengths)
        results['stats']['tech_term_coverage'] = sum(1 for c in tech_term_counts if c > 0) / len(samples)
    
    return results


def print_report(results: Dict):
    """打印验证报告"""
    print("\n" + "=" * 60)
    print("🔍 RANSTRUCT 数据集质量验证报告")
    print("=" * 60)
    
    total = results['total']
    print(f"\n📊 基本统计")
    print(f"  总样本数: {total}")
    print(f"  平均问题长度: {results['stats']['avg_question_length']:.1f} 字符")
    print(f"  平均答案长度: {results['stats']['avg_answer_length']:.1f} 字符")
    print(f"  技术术语覆盖率: {results['stats']['tech_term_coverage']*100:.1f}%")
    
    print(f"\n🔎 质量问题检测")
    issues = results['issues']
    
    # 关键问题（会严重影响 SFT 质量）
    critical_issues = 0
    
    if issues['meta_cognitive_leak']:
        count = len(issues['meta_cognitive_leak'])
        critical_issues += count
        print(f"  ❌ 元认知泄漏: {count} ({count/total*100:.1f}%)")
        for item in issues['meta_cognitive_leak'][:3]:
            print(f"     - [{item['index']}] {item['pattern']}")
    else:
        print(f"  ✅ 元认知泄漏: 0")
    
    if issues['rejection_pattern']:
        count = len(issues['rejection_pattern'])
        critical_issues += count
        print(f"  ❌ 拒答模式: {count} ({count/total*100:.1f}%)")
        for item in issues['rejection_pattern'][:3]:
            print(f"     - [{item['index']}] {item['pattern']}")
    else:
        print(f"  ✅ 拒答模式: 0")
    
    # 警告问题
    if issues['no_tech_terms']:
        count = len(issues['no_tech_terms'])
        print(f"  ⚠️  无技术术语: {count} ({count/total*100:.1f}%)")
    else:
        print(f"  ✅ 技术术语覆盖: 良好")
    
    if issues['too_short']:
        count = len(issues['too_short'])
        print(f"  ⚠️  答案过短(<100字): {count} ({count/total*100:.1f}%)")
    
    if issues['too_long']:
        count = len(issues['too_long'])
        print(f"  ⚠️  答案过长(>3000字): {count} ({count/total*100:.1f}%)")
    
    if issues['low_retrieval_score']:
        count = len(issues['low_retrieval_score'])
        print(f"  ⚠️  低检索置信度: {count} ({count/total*100:.1f}%)")
    
    # 总结
    print(f"\n📋 总结")
    if critical_issues == 0:
        print(f"  ✅ 数据集质量良好，可以直接用于 SFT 训练！")
        print(f"  📦 推荐使用 'chatml' 或 'conversation' 格式导出")
    else:
        print(f"  ❌ 发现 {critical_issues} 条严重问题数据")
        print(f"  💡 建议重新运行后处理: python main.py step6 --strict")
    
    print("=" * 60)


def export_sft_format(samples: List[Dict], output_path: str, format_type: str):
    """导出为 SFT 训练格式"""
    SYSTEM_PROMPT = "You are an O-RAN Technical Expert with comprehensive knowledge of Open RAN architecture, 3GPP specifications, and telecommunications systems. Provide accurate, detailed, and technically precise answers about O-RAN components, interfaces, protocols, and implementations."
    
    with open(output_path, 'w', encoding='utf-8') as f:
        for sample in samples:
            question = sample.get('question', '')
            answer = sample.get('answer', '')
            
            if format_type == 'alpaca':
                record = {
                    "instruction": question,
                    "input": "",
                    "output": answer
                }
            elif format_type == 'alpaca_system':
                record = {
                    "system": SYSTEM_PROMPT,
                    "instruction": question,
                    "input": "",
                    "output": answer
                }
            elif format_type == 'conversation':
                record = {
                    "conversations": [
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {"role": "user", "content": question},
                        {"role": "assistant", "content": answer}
                    ]
                }
            elif format_type == 'chatml':
                record = {
                    "messages": [
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {"role": "user", "content": question},
                        {"role": "assistant", "content": answer}
                    ]
                }
            else:
                raise ValueError(f"不支持的格式: {format_type}")
            
            f.write(json.dumps(record, ensure_ascii=False) + '\n')
    
    print(f"\n✅ 已导出 {len(samples)} 条数据到 {output_path} ({format_type} 格式)")


def main():
    parser = argparse.ArgumentParser(description='RANSTRUCT 数据集质量验证工具')
    parser.add_argument('--input', '-i', required=True, help='输入数据集路径 (JSONL格式)')
    parser.add_argument('--export-sft', type=str, choices=['alpaca', 'alpaca_system', 'conversation', 'chatml'],
                        help='导出为 SFT 训练格式')
    parser.add_argument('--output', '-o', type=str, help='导出文件路径 (默认: input_sft.jsonl)')
    parser.add_argument('--quiet', '-q', action='store_true', help='只输出关键信息')
    
    args = parser.parse_args()
    
    # 加载数据集
    print(f"正在加载数据集: {args.input}")
    samples = load_dataset(args.input)
    
    if not samples:
        print("错误: 数据集为空或无法读取")
        sys.exit(1)
    
    # 验证质量
    results = validate_dataset(samples)
    
    if not args.quiet:
        print_report(results)
    
    # 导出 SFT 格式
    if args.export_sft:
        output_path = args.output
        if not output_path:
            input_path = Path(args.input)
            output_path = str(input_path.parent / f"{input_path.stem}_sft_{args.export_sft}.jsonl")
        
        export_sft_format(samples, output_path, args.export_sft)
    
    # 返回状态码
    critical_count = len(results['issues']['meta_cognitive_leak']) + len(results['issues']['rejection_pattern'])
    sys.exit(0 if critical_count == 0 else 1)


if __name__ == "__main__":
    main()

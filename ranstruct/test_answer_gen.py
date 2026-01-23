#!/usr/bin/env python3
"""
测试答案生成脚本
直接从 generated_questions.jsonl 加载问题，测试答案生成
"""

import sys
import os

# 添加父目录到路径，确保可以导入 ranstruct 模块
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import json
import time
import logging
from pathlib import Path

# 设置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    from ranstruct.config import Config
    from ranstruct.faiss_manager import FAISSManager
    from ranstruct.answer_generator import AnswerGenerator, GeneratedQuestion
    
    # 配置
    config = Config()
    questions_file = config.output.output_dir / "generated_questions.jsonl"
    
    # 测试输出文件（与主进程隔离）
    test_output_file = config.output.output_dir / "test_answers_debug.jsonl"
    
    # 测试参数
    NUM_TEST_QUESTIONS = 20  # 测试问题数量
    
    print("=" * 60)
    print("答案生成测试")
    print("=" * 60)
    
    # 1. 加载问题
    print(f"\n[1/4] 加载问题文件: {questions_file}")
    questions = []
    with open(questions_file, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f):
            if i >= NUM_TEST_QUESTIONS:
                break
            data = json.loads(line)
            questions.append(GeneratedQuestion(
                question=data['question'],
                source_chunk_id=data['source_chunk_id'],
                metadata=data.get('metadata', {})
            ))
    print(f"   已加载 {len(questions)} 个问题")
    
    # 2. 初始化 FAISS
    print(f"\n[2/4] 加载 FAISS 索引...")
    start_time = time.time()
    faiss_manager = FAISSManager(config)
    faiss_manager.load_index()
    print(f"   FAISS 索引加载完成: {faiss_manager.index.ntotal} 个向量")
    print(f"   耗时: {time.time() - start_time:.2f} 秒")
    
    # 3. 初始化答案生成器
    print(f"\n[3/4] 初始化答案生成器...")
    answer_gen = AnswerGenerator(config, faiss_manager)
    
    # 4. 逐个生成答案并计时
    print(f"\n[4/4] 开始生成答案 (逐个测试)...")
    print(f"   测试结果将保存到: {test_output_file}")
    print("-" * 60)
    
    times = []
    successes = 0
    results = []  # 保存测试结果
    
    for i, question in enumerate(questions):
        start = time.time()
        
        try:
            qa_pair = answer_gen.generate_answer(question)
            elapsed = time.time() - start
            times.append(elapsed)
            
            status = "✓" if qa_pair else "✗"
            if qa_pair:
                successes += 1
                answer_preview = qa_pair.answer[:50] + "..." if len(qa_pair.answer) > 50 else qa_pair.answer
                results.append({
                    "question": qa_pair.question,
                    "answer": qa_pair.answer,
                    "elapsed_time": elapsed,
                    "status": "success"
                })
            else:
                answer_preview = "(无有效答案)"
                results.append({
                    "question": question.question,
                    "answer": None,
                    "elapsed_time": elapsed,
                    "status": "failed"
                })
            
            print(f"[{i+1:2d}/{len(questions)}] {status} {elapsed:5.2f}s | Q: {question.question[:40]}...")
            
        except Exception as e:
            elapsed = time.time() - start
            times.append(elapsed)
            results.append({
                "question": question.question,
                "answer": None,
                "elapsed_time": elapsed,
                "status": "error",
                "error": str(e)
            })
            print(f"[{i+1:2d}/{len(questions)}] ✗ {elapsed:5.2f}s | 错误: {e}")
    
    # 保存测试结果到独立文件
    with open(test_output_file, 'w', encoding='utf-8') as f:
        for r in results:
            f.write(json.dumps(r, ensure_ascii=False) + '\n')
    print(f"\n测试结果已保存到: {test_output_file}")
    
    # 统计
    print("-" * 60)
    print(f"\n统计:")
    print(f"  成功率: {successes}/{len(questions)} ({100*successes/len(questions):.1f}%)")
    print(f"  平均耗时: {sum(times)/len(times):.2f} 秒/问题")
    print(f"  最快: {min(times):.2f} 秒")
    print(f"  最慢: {max(times):.2f} 秒")
    print(f"  总耗时: {sum(times):.2f} 秒")
    
    # 检测异常慢的情况
    slow_threshold = sum(times)/len(times) * 3  # 超过平均3倍
    slow_indices = [i for i, t in enumerate(times) if t > slow_threshold]
    if slow_indices:
        print(f"\n⚠️  检测到 {len(slow_indices)} 个异常慢的请求 (>{slow_threshold:.1f}s):")
        for idx in slow_indices[:5]:
            print(f"    问题 {idx+1}: {times[idx]:.2f}s")


if __name__ == "__main__":
    main()

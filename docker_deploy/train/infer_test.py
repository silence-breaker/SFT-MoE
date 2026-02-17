#!/usr/bin/env python3
"""
infer_test.py — 使用 vLLM 批量推理测试集，计算多选题正确率。

用法 (容器内):
    python3 /app/scripts/infer_test.py \
        --model /app/model \
        --adapter /app/output/checkpoint-xxx \
        --data /app/data/oran_val_13K.jsonl \
        --output /app/output/infer_test_results.jsonl

评判逻辑:
    从模型回复中提取开头的选项编号 (1/2/3/4)，与标准答案的编号比较。
"""

import argparse
import json
import re
import time
from collections import defaultdict

from vllm import LLM, SamplingParams
from vllm.lora.request import LoRARequest


def parse_args():
    p = argparse.ArgumentParser(description="Batch inference accuracy test")
    p.add_argument("--model", required=True, help="Base model path")
    p.add_argument("--adapter", required=True, help="LoRA adapter checkpoint path")
    p.add_argument("--data", required=True, help="Test JSONL file path")
    p.add_argument("--output", default=None, help="Output results JSONL path")
    p.add_argument("--tp", type=int, default=8, help="Tensor parallel size")
    p.add_argument("--max-tokens", type=int, default=128, help="Max new tokens")
    p.add_argument("--max-lora-rank", type=int, default=64, help="Max LoRA rank")
    return p.parse_args()


def extract_option_number(text: str) -> str:
    """从回复文本中提取选项编号 (1/2/3/4)"""
    text = text.strip()
    # 匹配开头的数字: "3. O-RAN.WG1" -> "3"
    m = re.match(r"^(\d+)", text)
    if m:
        return m.group(1)
    return ""


def load_test_data(path: str):
    """加载测试集，返回 (prompts, references, difficulties)"""
    prompts = []
    references = []
    difficulties = []

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            item = json.loads(line)
            msgs = item["messages"]
            difficulty = item.get("difficulty", "Unknown")

            # 构建 system + user prompt
            system_msg = ""
            user_msg = ""
            assistant_ref = ""
            for msg in msgs:
                if msg["role"] == "system":
                    system_msg = msg["content"]
                elif msg["role"] == "user":
                    user_msg = msg["content"]
                elif msg["role"] == "assistant":
                    assistant_ref = msg["content"]

            prompts.append({"system": system_msg, "user": user_msg})
            references.append(assistant_ref)
            difficulties.append(difficulty)

    return prompts, references, difficulties


def build_chat_messages(prompts):
    """构建 vLLM chat 格式的 messages 列表"""
    conversations = []
    for p in prompts:
        msgs = []
        if p["system"]:
            msgs.append({"role": "system", "content": p["system"]})
        msgs.append({"role": "user", "content": p["user"]})
        conversations.append(msgs)
    return conversations


def main():
    args = parse_args()

    print("=" * 50)
    print("  O-RAN 微调模型正确率测试")
    print("=" * 50)
    print(f"  基座模型: {args.model}")
    print(f"  LoRA 适配器: {args.adapter}")
    print(f"  测试集: {args.data}")
    print(f"  Tensor Parallel: {args.tp}")
    print()

    # 1. 加载测试数据
    print("加载测试数据...")
    prompts, references, difficulties = load_test_data(args.data)
    total = len(prompts)
    print(f"  共 {total} 条测试数据")

    # 统计难度分布
    diff_counts = defaultdict(int)
    for d in difficulties:
        diff_counts[d] += 1
    for d, c in sorted(diff_counts.items()):
        print(f"  {d}: {c} 条")
    print()

    # 2. 初始化 vLLM
    print("初始化 vLLM 引擎...")
    llm = LLM(
        model=args.model,
        enable_lora=True,
        max_lora_rank=args.max_lora_rank,
        tensor_parallel_size=args.tp,
        trust_remote_code=True,
        max_model_len=2048,
        gpu_memory_utilization=0.90,
    )

    sampling_params = SamplingParams(
        temperature=0.0,  # greedy decoding for deterministic results
        max_tokens=args.max_tokens,
    )

    lora_req = LoRARequest("sft_adapter", 1, args.adapter)

    # 3. 构建对话并批量推理
    print("构建推理请求...")
    conversations = build_chat_messages(prompts)

    print(f"开始批量推理 ({total} 条)...")
    t0 = time.time()
    outputs = llm.chat(
        messages=conversations,
        sampling_params=sampling_params,
        lora_request=lora_req,
    )
    elapsed = time.time() - t0
    print(f"推理完成, 耗时 {elapsed:.1f}s ({total / elapsed:.1f} 条/秒)")
    print()

    # 4. 评估正确率
    correct = 0
    diff_correct = defaultdict(int)
    diff_total = defaultdict(int)
    results = []

    for i, output in enumerate(outputs):
        pred_text = output.outputs[0].text.strip()
        ref_text = references[i]
        difficulty = difficulties[i]

        pred_num = extract_option_number(pred_text)
        ref_num = extract_option_number(ref_text)

        is_correct = (pred_num == ref_num) and pred_num != ""

        if is_correct:
            correct += 1
            diff_correct[difficulty] += 1
        diff_total[difficulty] += 1

        results.append({
            "index": i,
            "difficulty": difficulty,
            "reference": ref_text,
            "prediction": pred_text,
            "ref_option": ref_num,
            "pred_option": pred_num,
            "correct": is_correct,
        })

    # 5. 输出结果
    print("=" * 50)
    print("  测试结果")
    print("=" * 50)
    print(f"  总正确率: {correct}/{total} = {correct / total * 100:.2f}%")
    print()
    print("  按难度分类:")
    for d in sorted(diff_total.keys()):
        dt = diff_total[d]
        dc = diff_correct[d]
        print(f"    {d:8s}: {dc}/{dt} = {dc / dt * 100:.2f}%")
    print()

    # 6. 保存详细结果
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            # 写入摘要行
            summary = {
                "type": "summary",
                "total": total,
                "correct": correct,
                "accuracy": round(correct / total * 100, 2),
                "by_difficulty": {
                    d: {
                        "total": diff_total[d],
                        "correct": diff_correct[d],
                        "accuracy": round(diff_correct[d] / diff_total[d] * 100, 2),
                    }
                    for d in sorted(diff_total.keys())
                },
                "elapsed_seconds": round(elapsed, 1),
            }
            f.write(json.dumps(summary, ensure_ascii=False) + "\n")
            # 写入每条详细结果
            for r in results:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        print(f"  详细结果已保存: {args.output}")

    print()
    print("✅ 测试完成")


if __name__ == "__main__":
    main()

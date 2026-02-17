#!/usr/bin/env python3
"""
infer_test_hf.py — 困惑度 (PPL) 评分法测试多选题正确率

原理:
  对每道题的 4 个选项，分别构建完整对话 (system + user + candidate_answer)，
  计算模型在 answer 部分的平均 token 负对数似然 (即 PPL)。
  PPL 最低的选项 = 模型认为"最通顺"的答案 = 预测答案。
"""

import argparse
import json
import math
import re
import time
from collections import defaultdict

import torch
from tqdm import tqdm
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--model", required=True, help="Base model path")
    p.add_argument("--adapter", default=None, help="LoRA adapter path (optional, omit to test base model)")
    p.add_argument("--data", required=True, help="Test JSONL file")
    p.add_argument("--output", default="result.jsonl", help="Output file")
    return p.parse_args()


def parse_options(user_content: str):
    """从 user content 中解析出问题文本和各选项。
    格式: "问题\n\n1. xxx\n2. xxx\n3. xxx\n4. xxx"
    返回: (question_text, [(option_num_str, option_full_text), ...])
    """
    # 用双换行分割问题和选项
    parts = user_content.split("\n\n", 1)
    question = parts[0].strip()
    options_block = parts[1].strip() if len(parts) > 1 else ""

    options = []
    for m in re.finditer(r"^(\d+)\.\s*(.+)$", options_block, re.MULTILINE):
        num = m.group(1)
        full = m.group(0)  # "1. xxx"
        options.append((num, full))

    return question, options


def compute_answer_ppl(model, tokenizer, prompt_ids, answer_ids):
    """计算 answer 部分的 PPL。
    prompt_ids: token ids of (system + user) prompt
    answer_ids: token ids of candidate answer
    返回: answer 部分的平均负对数似然 (越低越好)
    """
    input_ids = torch.cat([prompt_ids, answer_ids], dim=-1)
    # 构建 labels: prompt 部分设为 -100 (不计算 loss)，只算 answer 部分
    labels = input_ids.clone()
    labels[:, :prompt_ids.shape[1]] = -100

    with torch.no_grad():
        outputs = model(input_ids=input_ids, labels=labels)
    # outputs.loss 是 answer tokens 的平均 cross-entropy
    return outputs.loss.item()


def main():
    args = parse_args()

    print("=" * 50)
    print("  O-RAN 多选题 PPL 评分测试")
    print("=" * 50)
    print(f"  基座模型: {args.model}")
    if args.adapter:
        print(f"  LoRA 适配器: {args.adapter}")
    else:
        print("  模式: 纯基座模型 (无 LoRA)")
    print(f"  测试集: {args.data}")
    print()

    # 1. 加载模型
    print("正在加载基座模型...")
    model = AutoModelForCausalLM.from_pretrained(
        args.model,
        torch_dtype=torch.bfloat16,
        device_map="auto",
        trust_remote_code=True,
    )

    if args.adapter:
        print(f"正在加载 LoRA: {args.adapter} ...")
        model = PeftModel.from_pretrained(model, args.adapter)
    model.eval()

    tokenizer = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True)

    # 2. 加载数据
    print(f"读取数据: {args.data}")
    with open(args.data, "r", encoding="utf-8") as f:
        lines = [l for l in f if l.strip()]
    total = len(lines)
    print(f"  共 {total} 条")

    # 统计难度分布
    diff_counts = defaultdict(int)
    for l in lines:
        d = json.loads(l).get("difficulty", "Unknown")
        diff_counts[d] += 1
    for d, c in sorted(diff_counts.items()):
        print(f"  {d}: {c} 条")
    print()

    # 3. 逐题 PPL 评分
    print("开始 PPL 评分...")
    t0 = time.time()

    correct = 0
    diff_correct = defaultdict(int)
    diff_total = defaultdict(int)
    results = []

    for i, line in enumerate(tqdm(lines)):
        item = json.loads(line)
        msgs = item["messages"]
        difficulty = item.get("difficulty", "Unknown")

        # 提取 system / user / ref answer
        system_text = ""
        user_text = ""
        ref_text = ""
        for m in msgs:
            if m["role"] == "system":
                system_text = m["content"]
            elif m["role"] == "user":
                user_text = m["content"]
            elif m["role"] == "assistant":
                ref_text = m["content"]

        ref_num = re.match(r"^(\d+)", ref_text.strip())
        ref_num = ref_num.group(1) if ref_num else ""

        # 解析选项
        _, options = parse_options(user_text)
        if len(options) < 2:
            # 解析失败，跳过
            results.append({"index": i, "difficulty": difficulty, "ref": ref_text,
                            "pred": "PARSE_ERROR", "correct": False, "ppls": {}})
            diff_total[difficulty] += 1
            continue

        # 构建 prompt (system + user 部分)，用 chat template 格式
        prompt_text = (
            f"<|im_start|>system\n{system_text}<|im_end|>\n"
            f"<|im_start|>user\n{user_text}<|im_end|>\n"
            f"<|im_start|>assistant\n"
        )
        prompt_ids = tokenizer(prompt_text, return_tensors="pt").input_ids.to(model.device)

        # 对每个选项计算 PPL
        option_ppls = {}
        for opt_num, opt_text in options:
            answer_ids = tokenizer(opt_text, return_tensors="pt", add_special_tokens=False).input_ids.to(model.device)
            ppl = compute_answer_ppl(model, tokenizer, prompt_ids, answer_ids)
            option_ppls[opt_num] = ppl

        # 选 PPL 最低的
        pred_num = min(option_ppls, key=option_ppls.get)
        is_correct = (pred_num == ref_num)

        if is_correct:
            correct += 1
            diff_correct[difficulty] += 1
        diff_total[difficulty] += 1

        results.append({
            "index": i,
            "difficulty": difficulty,
            "ref": ref_text,
            "ref_option": ref_num,
            "pred_option": pred_num,
            "correct": is_correct,
            "ppls": {k: round(v, 4) for k, v in option_ppls.items()},
        })

    elapsed = time.time() - t0

    # 4. 输出结果
    print()
    print("=" * 50)
    print("  测试结果")
    print("=" * 50)
    print(f"  总正确率: {correct}/{total} = {correct / total * 100:.2f}%")
    print(f"  耗时: {elapsed:.1f}s ({total / elapsed:.1f} 条/秒)")
    print()
    print("  按难度分类:")
    for d in sorted(diff_total.keys()):
        dt = diff_total[d]
        dc = diff_correct[d]
        print(f"    {d:8s}: {dc}/{dt} = {dc / dt * 100:.2f}%")
    print()

    # 5. 保存
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            summary = {
                "type": "summary",
                "total": total,
                "correct": correct,
                "accuracy": round(correct / total * 100, 2),
                "by_difficulty": {
                    d: {"total": diff_total[d], "correct": diff_correct[d],
                        "accuracy": round(diff_correct[d] / diff_total[d] * 100, 2)}
                    for d in sorted(diff_total.keys())
                },
                "elapsed_seconds": round(elapsed, 1),
                "method": "ppl_scoring",
            }
            f.write(json.dumps(summary, ensure_ascii=False) + "\n")
            for r in results:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        print(f"  结果已保存: {args.output}")

    print()
    print("✅ 测试完成")


if __name__ == "__main__":
    main()

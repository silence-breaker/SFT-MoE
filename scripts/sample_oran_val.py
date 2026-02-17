"""
从 ORAN-Bench-13K/Benchmark 下三种难度数据集按 1:1:1 抽取共 600 条，
输出到 output/dataset/oran_val_500.jsonl (Qwen3 SFT 对话格式)
"""

import json
import random
import os

SEED = 42
TOTAL = 600
PER_LEVEL = TOTAL // 3  # 200

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BENCHMARK_DIR = os.path.join(BASE_DIR, "ORAN-Bench-13K", "Benchmark")
OUTPUT_PATH = os.path.join(BASE_DIR, "output", "dataset", "oran_val_500.jsonl")

SYSTEM_PROMPT = ("You are an O-RAN Technical Expert. Answer the following multiple-choice "
                 "question about O-RAN by selecting the correct option. Reply with only the "
                 "option number and the corresponding answer text.")

DIFFICULTY_MAP = {
    "easy": ("fin_E.json", "Easy"),
    "medium": ("fin_M.json", "Medium"),
    "hard": ("fin_H.json", "Hard"),
}

random.seed(SEED)

sampled = []
for level, (fname, diff_label) in DIFFICULTY_MAP.items():
    path = os.path.join(BENCHMARK_DIR, fname)
    with open(path, "r", encoding="utf-8") as f:
        data = [json.loads(line) for line in f if line.strip()]
    print(f"{level}: {len(data)} 条, 抽取 {PER_LEVEL} 条")
    assert len(data) >= PER_LEVEL, f"{fname} 数据不足 {PER_LEVEL} 条"
    selected = random.sample(data, PER_LEVEL)
    for item in selected:
        question, options, answer_idx = item[0], item[1], item[2]
        # 拼接选项文本: "1. xxx\n2. xxx\n..."
        options_text = "\n".join(options)
        user_content = f"{question}\n\n{options_text}"
        # 根据 answer_idx 找到对应选项作为 assistant 回复
        answer_content = options[int(answer_idx) - 1]
        sampled.append({
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_content},
                {"role": "assistant", "content": answer_content},
            ],
            "difficulty": diff_label,
        })

random.shuffle(sampled)

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    for item in sampled:
        f.write(json.dumps(item, ensure_ascii=False) + "\n")

print(f"\n完成: 共 {len(sampled)} 条, 保存到 {OUTPUT_PATH}")

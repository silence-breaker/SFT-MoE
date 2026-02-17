#!/usr/bin/env python3
"""
合并去重数据集脚本
读取 output/dataset/ 下所有 *_sft_chatml.jsonl 文件，
按 user message 内容哈希去重，按 95:5 比例切分为训练集和验证集。
"""

import json
import hashlib
import random
import glob
import os
import sys

# ============================================================================
# 配置
# ============================================================================
DATASET_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "output", "dataset")
PATTERN = os.path.join(DATASET_DIR, "*_sft_chatml.jsonl")
TRAIN_RATIO = 0.95
RANDOM_SEED = 42

OUTPUT_TRAIN = os.path.join(DATASET_DIR, "oran_train.jsonl")
OUTPUT_VAL = os.path.join(DATASET_DIR, "oran_val.jsonl")


def extract_user_content(messages):
    """提取 user 角色的消息内容用于去重"""
    for msg in messages:
        if msg.get("role") == "user":
            return msg.get("content", "")
    return ""


def md5_hash(text):
    """计算文本的 MD5 哈希"""
    return hashlib.md5(text.encode("utf-8")).hexdigest()


def main():
    # 查找所有源文件
    files = sorted(glob.glob(PATTERN))
    # 排除已经生成的输出文件
    files = [f for f in files if os.path.basename(f) not in ("oran_train.jsonl", "oran_val.jsonl")]

    if not files:
        print(f"❌ 未找到匹配的文件: {PATTERN}")
        sys.exit(1)

    print("=" * 60)
    print("  合并去重数据集")
    print("=" * 60)
    print(f"\n找到 {len(files)} 个源文件:")
    for f in files:
        print(f"  - {os.path.basename(f)}")

    # 读取所有数据并去重
    seen_hashes = set()
    unique_samples = []
    total_count = 0
    duplicate_count = 0

    for filepath in files:
        file_count = 0
        file_dup = 0
        with open(filepath, "r", encoding="utf-8") as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                total_count += 1
                file_count += 1

                try:
                    data = json.loads(line)
                except json.JSONDecodeError:
                    print(f"  ⚠️ JSON 解析错误: {os.path.basename(filepath)} 第 {line_num} 行，跳过")
                    continue

                messages = data.get("messages", [])
                user_content = extract_user_content(messages)
                content_hash = md5_hash(user_content)

                if content_hash in seen_hashes:
                    duplicate_count += 1
                    file_dup += 1
                    continue

                seen_hashes.add(content_hash)
                unique_samples.append(data)

        print(f"  📄 {os.path.basename(filepath)}: {file_count} 条，去重 {file_dup} 条")

    print(f"\n📊 统计:")
    print(f"  总条数: {total_count}")
    print(f"  重复条数: {duplicate_count}")
    print(f"  去重后条数: {len(unique_samples)}")
    print(f"  去重率: {duplicate_count / total_count * 100:.1f}%")

    # 随机 shuffle
    random.seed(RANDOM_SEED)
    random.shuffle(unique_samples)

    # 按比例切分
    split_idx = int(len(unique_samples) * TRAIN_RATIO)
    train_data = unique_samples[:split_idx]
    val_data = unique_samples[split_idx:]

    print(f"\n📦 切分结果:")
    print(f"  训练集: {len(train_data)} 条 ({TRAIN_RATIO * 100:.0f}%)")
    print(f"  验证集: {len(val_data)} 条 ({(1 - TRAIN_RATIO) * 100:.0f}%)")

    # 写出文件
    with open(OUTPUT_TRAIN, "w", encoding="utf-8") as f:
        for sample in train_data:
            f.write(json.dumps(sample, ensure_ascii=False) + "\n")
    print(f"\n✅ 训练集已保存: {OUTPUT_TRAIN}")

    with open(OUTPUT_VAL, "w", encoding="utf-8") as f:
        for sample in val_data:
            f.write(json.dumps(sample, ensure_ascii=False) + "\n")
    print(f"✅ 验证集已保存: {OUTPUT_VAL}")

    # 验证输出
    train_size = os.path.getsize(OUTPUT_TRAIN) / (1024 * 1024)
    val_size = os.path.getsize(OUTPUT_VAL) / (1024 * 1024)
    print(f"\n📏 文件大小:")
    print(f"  训练集: {train_size:.1f} MB")
    print(f"  验证集: {val_size:.1f} MB")
    print(f"  合计: {train_size + val_size:.1f} MB")


if __name__ == "__main__":
    main()

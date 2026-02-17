#!/bin/bash
# ============================================================================
# 快速数据集生成脚本
# 用于在容器内直接生成 Qwen3-30B-A3B 格式的训练数据集
# ============================================================================

set -e

echo "=============================================="
echo "  RANSTRUCT 快速数据集生成"
echo "  输出格式: ChatML (Qwen3-30B-A3B)"
echo "=============================================="

# 默认参数
MAX_CHUNKS=${MAX_CHUNKS:-100}
QUESTIONS_PER_CHUNK=${QUESTIONS_PER_CHUNK:-3}
TOP_K=${TOP_K:-3}
OUTPUT_FORMAT="chatml"

# 解析命令行参数
while [[ $# -gt 0 ]]; do
    case $1 in
        --max-chunks)
            MAX_CHUNKS="$2"
            shift 2
            ;;
        --questions)
            QUESTIONS_PER_CHUNK="$2"
            shift 2
            ;;
        --top-k)
            TOP_K="$2"
            shift 2
            ;;
        --test)
            MAX_CHUNKS=10
            shift
            ;;
        *)
            echo "未知参数: $1"
            exit 1
            ;;
    esac
done

echo ""
echo "配置:"
echo "  - 最大 Chunks: $MAX_CHUNKS"
echo "  - 每 Chunk 问题数: $QUESTIONS_PER_CHUNK"
echo "  - RAG Top-K: $TOP_K"
echo "  - 输出格式: $OUTPUT_FORMAT"
echo ""

# 运行数据集生成
python ranstruct/main.py run \
    --max-chunks $MAX_CHUNKS \
    --questions-per-chunk $QUESTIONS_PER_CHUNK \
    --top-k $TOP_K \
    --format $OUTPUT_FORMAT \
    --timestamp

# 找到最新生成的数据集
LATEST_DATASET=$(ls -t /app/output/ranstruct_dataset_cleaned_*.jsonl 2>/dev/null | head -1)

if [ -n "$LATEST_DATASET" ]; then
    echo ""
    echo "=============================================="
    echo "验证并导出数据集..."
    echo "=============================================="
    
    # 验证数据集质量
    python ranstruct/validate_dataset.py --input "$LATEST_DATASET" --export-sft chatml
    
    echo ""
    echo "=============================================="
    echo "生成完成！"
    echo "=============================================="
    echo "原始数据集: $LATEST_DATASET"
    echo "ChatML 格式: ${LATEST_DATASET%.jsonl}_sft_chatml.jsonl"
    echo ""
    echo "数据集可直接用于 Qwen3-30B-A3B SFT 微调"
else
    echo "错误: 未找到生成的数据集"
    exit 1
fi

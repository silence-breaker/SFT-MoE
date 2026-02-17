#!/bin/bash
# ============================================================================
# 8卡 A100 并行运行脚本
# 每个 GPU 运行一个容器，处理 1/8 的数据
# ============================================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
IMAGE_NAME="ranstruct:latest"
OUTPUT_DIR="$(pwd)/output"
DATA_DIR="$(pwd)/datasource"
MODELS_DIR="$(pwd)/models"
RANSTRUCT_DIR="$(pwd)/ranstruct"
LOGS_DIR="$(pwd)/logs"
HF_CACHE_DIR="$(pwd)/hf_cache"

# 确保目录存在
mkdir -p "$OUTPUT_DIR" "$LOGS_DIR" "$HF_CACHE_DIR"

# 清理之前的容器
echo "清理之前的容器..."
for i in {0..7}; do
    docker rm -f ranstruct_shard_$i 2>/dev/null || true
done

echo "=============================================="
echo "  RANSTRUCT 8卡并行数据集生成"
echo "=============================================="
echo ""
echo "配置:"
echo "  - 数据源: $DATA_DIR"
echo "  - 输出目录: $OUTPUT_DIR"
echo "  - 模型目录: $MODELS_DIR"
echo ""

# 检查必要目录
if [ ! -d "$MODELS_DIR/bge-small-en-v1.5" ]; then
    echo "错误: 未找到嵌入模型 $MODELS_DIR/bge-small-en-v1.5"
    echo "请先下载模型"
    exit 1
fi

echo "开始启动 8 个并发任务..."

for i in {0..7}; do
    echo "启动分片 $i (GPU $i)..."
    
    # 每个容器绑定一个 GPU
    docker run -d \
        --name ranstruct_shard_$i \
        --gpus "device=$i" \
        -v "$SCRIPT_DIR/entrypoint.sh:/app/entrypoint.sh" \
        -v "$OUTPUT_DIR:/app/output" \
        -v "$DATA_DIR:/app/datasource" \
        -v "$MODELS_DIR:/app/models" \
        -v "$RANSTRUCT_DIR:/app/ranstruct" \
        -v "$LOGS_DIR:/app/logs" \
        -v "$HF_CACHE_DIR:/root/.cache/huggingface" \
        -v ranstruct_ollama:/root/.ollama \
        -e OLLAMA_NUM_PARALLEL=4 \
        -e FAISS_NO_GPU=1 \
        $IMAGE_NAME run --shard-id $i --num-shards 8 --format chatml --timestamp
        
    echo "  分片 $i 已后台启动"
    
    # 稍微错开启动时间，避免同时加载模型
    sleep 5
done

echo ""
echo "=============================================="
echo "所有任务已启动！"
echo ""
echo "查看状态:"
echo "  docker ps | grep ranstruct"
echo ""
echo "查看日志:"
echo "  docker logs -f ranstruct_shard_0"
echo ""
echo "查看资源:"
echo "  docker stats"
echo ""
echo "停止所有:"
echo "  for i in {0..7}; do docker stop ranstruct_shard_\$i; done"
echo "=============================================="

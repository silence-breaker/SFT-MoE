#!/bin/bash
# ============================================================================
# 上传训练相关文件到远程服务器
# 包括: 数据集 + Docker 训练配置 + 训练脚本
# ============================================================================

set -e

# ============================================================================
# 配置区域 - 与 upload_to_server.sh 保持一致
# ============================================================================
REMOTE_USER="lijindong"
REMOTE_HOST="210.75.240.12"
REMOTE_DIR="ranstruct_workplace"

# ============================================================================
# 本地路径
# ============================================================================
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

echo "=============================================="
echo "  上传训练文件到远程服务器"
echo "=============================================="
echo ""
echo "本地项目目录: $PROJECT_ROOT"
echo "远程服务器: $REMOTE_USER@$REMOTE_HOST"
echo "远程目录: ~/$REMOTE_DIR"
echo ""

# 检查必要文件是否存在
if [ ! -f "$PROJECT_ROOT/output/dataset/oran_train.jsonl" ]; then
    echo "❌ 错误: 未找到 output/dataset/oran_train.jsonl"
    echo "请先运行: python3 scripts/merge_dataset.py"
    exit 1
fi

if [ ! -f "$PROJECT_ROOT/output/dataset/oran_val.jsonl" ]; then
    echo "❌ 错误: 未找到 output/dataset/oran_val.jsonl"
    echo "请先运行: python3 scripts/merge_dataset.py"
    exit 1
fi

TRAIN_COUNT=$(wc -l < "$PROJECT_ROOT/output/dataset/oran_train.jsonl")
VAL_COUNT=$(wc -l < "$PROJECT_ROOT/output/dataset/oran_val.jsonl")
echo "📊 数据集统计:"
echo "  训练集: ${TRAIN_COUNT} 条"
echo "  验证集: ${VAL_COUNT} 条"
echo ""

# 确认继续
read -p "确认上传? (y/n): " confirm
if [ "$confirm" != "y" ] && [ "$confirm" != "Y" ]; then
    echo "已取消"
    exit 0
fi

echo ""
echo "[1/4] 在远程服务器创建目录结构..."
ssh "$REMOTE_USER@$REMOTE_HOST" "mkdir -p ~/$REMOTE_DIR/{train/output,models,output/dataset,hf_cache}"

echo ""
echo "[2/4] 上传合并后的数据集..."
rsync -avz --progress \
    "$PROJECT_ROOT/output/dataset/oran_train.jsonl" \
    "$PROJECT_ROOT/output/dataset/oran_val.jsonl" \
    "$REMOTE_USER@$REMOTE_HOST:~/$REMOTE_DIR/output/dataset/"

echo ""
echo "[3/4] 上传训练 Docker 配置和脚本..."
rsync -avz --progress \
    "$SCRIPT_DIR/train/" \
    "$REMOTE_USER@$REMOTE_HOST:~/$REMOTE_DIR/train/"

# 确保脚本有执行权限
ssh "$REMOTE_USER@$REMOTE_HOST" "chmod +x ~/$REMOTE_DIR/train/train.sh"

echo ""
echo "[4/4] 验证远程文件..."
ssh "$REMOTE_USER@$REMOTE_HOST" "echo '--- 目录结构 ---' && find ~/$REMOTE_DIR/train -type f && echo '' && echo '--- 数据集 ---' && ls -lh ~/$REMOTE_DIR/output/dataset/oran_*.jsonl"

echo ""
echo "=============================================="
echo "✅ 上传完成！"
echo "=============================================="
echo ""
echo "下一步，在服务器上执行:"
echo ""
echo "  ssh $REMOTE_USER@$REMOTE_HOST"
echo "  cd ~/$REMOTE_DIR/train"
echo ""
echo "  # 1. 构建训练镜像 (约 20-40 分钟)"
echo "  docker build -t sft-train:latest -f Dockerfile.train ."
echo ""
echo "  # 2. 下载模型 (~61GB, 使用 HF 镜像加速)"
echo "  docker run --rm -it \\"
echo "      -v ~/ranstruct_workplace/models:/app/models \\"
echo "      -v ~/ranstruct_workplace/hf_cache:/root/.cache/huggingface \\"
echo "      -e HF_ENDPOINT=https://hf-mirror.com \\"
echo "      sft-train:latest \\"
echo "      huggingface-cli download Qwen/Qwen3-30B-A3B --local-dir /app/models/Qwen3-30B-A3B"
echo ""
echo "  # 3. 启动训练 (在 tmux 中运行)"
echo "  tmux new -s train"
echo "  docker compose -f docker-compose.train.yml run --rm train bash /app/scripts/train.sh"
echo ""
echo "  # 4. 训练完成后合并 LoRA"
echo "  docker compose -f docker-compose.train.yml run --rm train \\"
echo "      swift export --adapters /app/output/<checkpoint_dir> --merge_lora true"
echo ""

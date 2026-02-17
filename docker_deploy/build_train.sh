#!/bin/bash
# ============================================================================
# 本地构建脚本
# 在你的本地机器上运行此脚本，构建 Docker 镜像并导出
# ============================================================================

# 设置脚本执行模式：遇到错误立即退出，输出执行过程
set -euo pipefail

# 定义颜色输出（可选，增强可读性）
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

# 定义关键变量（方便维护）
TARGET_DIR="/home/silence_breaker/git/SFT-MoE/docker_deploy/train"
IMAGE_NAME="sft-train:latest"
OUTPUT_FILE="sft-train.tar.gz"

# 检查目标目录是否存在
if [ ! -d "$TARGET_DIR" ]; then
    echo -e "${RED}错误：目标目录不存在 - $TARGET_DIR${NC}"
    exit 1
fi

# 进入构建目录
echo -e "${GREEN}进入构建目录：$TARGET_DIR${NC}"
cd "$TARGET_DIR"

# 构建Docker镜像
echo -e "${GREEN}开始构建Docker镜像：$IMAGE_NAME${NC}"
docker build -t "$IMAGE_NAME" -f Dockerfile.train .

# 导出镜像为tar.gz文件
echo -e "${GREEN}开始导出镜像到文件：$OUTPUT_FILE${NC}"
docker save "$IMAGE_NAME" | gzip > "$OUTPUT_FILE"

# 验证导出结果
if [ -f "$OUTPUT_FILE" ]; then
    echo -e "${GREEN}✅ 操作完成！镜像已成功导出到：$(pwd)/$OUTPUT_FILE${NC}"
else
    echo -e "${RED}❌ 导出失败！未找到 $OUTPUT_FILE 文件${NC}"
    exit 1
fi
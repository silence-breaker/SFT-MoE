#!/bin/bash
# ============================================================================
# 本地构建脚本
# 在你的本地机器上运行此脚本，构建 Docker 镜像并导出
# ============================================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

echo "=============================================="
echo "  RANSTRUCT Docker 镜像构建"
echo "=============================================="
echo ""
echo "项目目录: $PROJECT_ROOT"
echo ""

cd "$PROJECT_ROOT"

# 1. 构建镜像
echo "[1/3] 构建 Docker 镜像..."
docker build -t ranstruct:latest -f docker_deploy/Dockerfile .

# 2. 显示镜像信息
echo ""
echo "[2/3] 镜像构建完成"
docker images ranstruct:latest

# 3. 导出镜像（用于传输到服务器）
echo ""
echo "[3/3] 导出镜像为 tar 文件..."

# 导出为未压缩的 tar（Apptainer 需要这种格式）
OUTPUT_FILE="ranstruct_docker.tar"
docker save ranstruct:latest > "$OUTPUT_FILE"

# 同时生成压缩版本（传输更快）
OUTPUT_FILE_GZ="${OUTPUT_FILE}.gz"
gzip -k "$OUTPUT_FILE"

echo ""
echo "=============================================="
echo "构建完成！"
echo "=============================================="
echo ""
echo "镜像文件:"
echo "  - $OUTPUT_FILE (未压缩，Apptainer 直接使用)"
echo "  - $OUTPUT_FILE_GZ (压缩版，传输更快)"
echo ""
echo "文件大小:"
echo "  - $(du -h "$OUTPUT_FILE" | cut -f1) (未压缩)"
echo "  - $(du -h "$OUTPUT_FILE_GZ" | cut -f1) (压缩)"
echo ""
echo "下一步:"
echo "  1. 将文件上传到服务器（推荐上传压缩版）"
echo "  2. Docker 使用: docker load < ranstruct_docker.tar.gz"
echo "  3. Apptainer 使用:"
echo "     - 如果上传了 .tar:    apptainer build ranstruct.sif docker-archive://ranstruct_docker.tar"
echo "     - 如果上传了 .tar.gz: gunzip ranstruct_docker.tar.gz && apptainer build ranstruct.sif docker-archive://ranstruct_docker.tar"
echo ""

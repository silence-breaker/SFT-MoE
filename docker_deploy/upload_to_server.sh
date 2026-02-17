#!/bin/bash
# ============================================================================
# 上传所需文件到远程服务器 (Docker 版)
# ============================================================================

set -e

# ============================================================================
# 配置区域 - 请根据你的服务器信息修改
# ============================================================================
REMOTE_USER="lijindong"              # 你的用户名
REMOTE_HOST="210.75.240.12"          # 服务器 IP
REMOTE_DIR="ranstruct_workplace"     # 远程工作目录

# ============================================================================
# 本地路径（自动检测）
# ============================================================================
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

echo "=============================================="
echo "  上传文件到远程服务器 (Docker 方案)"
echo "=============================================="
echo ""
echo "本地项目目录: $PROJECT_ROOT"
echo "远程服务器: $REMOTE_USER@$REMOTE_HOST"
echo "远程目录: ~/$REMOTE_DIR"
echo ""

# 确认继续
read -p "确认上传? (y/n): " confirm
if [ "$confirm" != "y" ] && [ "$confirm" != "Y" ]; then
    echo "已取消"
    exit 0
fi

echo ""
echo "[1/5] 在远程服务器创建目录结构..."
ssh "$REMOTE_USER@$REMOTE_HOST" "mkdir -p ~/$REMOTE_DIR/{datasource,output,logs}"

echo ""
echo "[2/5] 上传 Docker 镜像 (这需要一些时间)..."
if [ -f "$PROJECT_ROOT/ranstruct_docker.tar.gz" ]; then
    rsync -avz --progress "$PROJECT_ROOT/ranstruct_docker.tar.gz" \
        "$REMOTE_USER@$REMOTE_HOST:~/$REMOTE_DIR/"
elif [ -f "$PROJECT_ROOT/ranstruct_docker.tar" ]; then
    echo "  发现未压缩的 tar 文件，先压缩再上传..."
    gzip -k "$PROJECT_ROOT/ranstruct_docker.tar"
    rsync -avz --progress "$PROJECT_ROOT/ranstruct_docker.tar.gz" \
        "$REMOTE_USER@$REMOTE_HOST:~/$REMOTE_DIR/"
else
    echo "❌ 错误: 未找到 ranstruct_docker.tar 或 ranstruct_docker.tar.gz"
    echo "请先运行: ./docker_deploy/build_local.sh"
    exit 1
fi

echo ""
echo "[3/5] 上传运行脚本..."
scp "$SCRIPT_DIR/run_docker.sh" "$REMOTE_USER@$REMOTE_HOST:~/$REMOTE_DIR/"
ssh "$REMOTE_USER@$REMOTE_HOST" "chmod +x ~/$REMOTE_DIR/run_docker.sh"

echo ""
echo "[4/5] 上传数据源..."
echo "  - ORAN_Specification/"
rsync -avz --progress "$PROJECT_ROOT/datasource/ORAN_Specification/" \
    "$REMOTE_USER@$REMOTE_HOST:~/$REMOTE_DIR/datasource/ORAN_Specification/"

echo ""
echo "  - codeset/"
rsync -avz --progress "$PROJECT_ROOT/datasource/codeset/" \
    "$REMOTE_USER@$REMOTE_HOST:~/$REMOTE_DIR/datasource/codeset/"

echo ""
echo "  - FAISS-v2.0/ (预构建索引)"
rsync -avz --progress "$PROJECT_ROOT/datasource/FAISS-v2.0/" \
    "$REMOTE_USER@$REMOTE_HOST:~/$REMOTE_DIR/datasource/FAISS-v2.0/"

echo ""
echo "[5/5] 在远程服务器加载 Docker 镜像..."
ssh "$REMOTE_USER@$REMOTE_HOST" "cd ~/$REMOTE_DIR && docker load < ranstruct_docker.tar.gz"

echo ""
echo "验证远程目录结构..."
ssh "$REMOTE_USER@$REMOTE_HOST" "ls -la ~/$REMOTE_DIR/"

echo ""
echo "=============================================="
echo "✅ 上传完成！"
echo "=============================================="
echo ""
echo "下一步，在服务器上执行:"
echo ""
echo "  ssh $REMOTE_USER@$REMOTE_HOST"
echo "  cd ~/$REMOTE_DIR"
echo "  ./run_docker.sh test    # 测试模式"
echo "  ./run_docker.sh run     # 完整运行"
echo ""

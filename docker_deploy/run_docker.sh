#!/bin/bash
# ============================================================================
# 服务器端运行脚本 (Docker 版)
# 在有 Docker 权限的服务器上使用
# ============================================================================

set -e

echo "=============================================="
echo "  RANSTRUCT 数据集生成 (Docker)"
echo "=============================================="

# 获取脚本所在目录
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# 默认参数
MODE=${1:-"run"}
EXTRA_ARGS="${@:2}"

# 检查镜像是否存在
if ! docker images ranstruct:latest --format "{{.Repository}}" | grep -q ranstruct; then
    echo "错误: 未找到 ranstruct:latest 镜像"
    echo "请先运行: docker load < ranstruct_docker.tar.gz"
    exit 1
fi

# 创建必要的目录
mkdir -p output logs hf_cache

case "$MODE" in
    run)
        echo "运行完整数据集生成流程..."
        docker run --rm -it \
            --gpus all \
            -v "$SCRIPT_DIR/entrypoint.sh:/app/entrypoint.sh" \
            -v "$(pwd)/datasource:/app/datasource" \
            -v "$(pwd)/output:/app/output" \
            -v "$(pwd)/logs:/app/logs" \
            -v "$(pwd)/models:/app/models" \
            -v "$(pwd)/ranstruct:/app/ranstruct" \
            -v "$(pwd)/hf_cache:/root/.cache/huggingface" \
            -v ranstruct_ollama:/root/.ollama \
            ranstruct:latest \
            run --format chatml --timestamp $EXTRA_ARGS
        ;;
    
    test)
        echo "运行测试模式 (10 chunks)..."
        docker run --rm -it \
            --gpus all \
            -v "$SCRIPT_DIR/entrypoint.sh:/app/entrypoint.sh" \
            -v "$(pwd)/datasource:/app/datasource" \
            -v "$(pwd)/output:/app/output" \
            -v "$(pwd)/logs:/app/logs" \
            -v "$(pwd)/models:/app/models" \
            -v "$(pwd)/ranstruct:/app/ranstruct" \
            -v "$(pwd)/hf_cache:/root/.cache/huggingface" \
            -v ranstruct_ollama:/root/.ollama \
            ranstruct:latest \
            run --format chatml --timestamp --test $EXTRA_ARGS
        ;;
    
    shell)
        echo "进入交互式 Shell..."
        docker run --rm -it \
            --gpus all \
            -v "$SCRIPT_DIR/entrypoint.sh:/app/entrypoint.sh" \
            -v "$(pwd)/datasource:/app/datasource" \
            -v "$(pwd)/output:/app/output" \
            -v "$(pwd)/logs:/app/logs" \
            -v "$(pwd)/models:/app/models" \
            -v "$(pwd)/ranstruct:/app/ranstruct" \
            -v "$(pwd)/hf_cache:/root/.cache/huggingface" \
            -v ranstruct_ollama:/root/.ollama \
            ranstruct:latest \
            bash
        ;;
    
    validate)
        echo "验证数据集..."
        INPUT_FILE=${2:-"output/ranstruct_dataset_cleaned.jsonl"}
        docker run --rm -it \
            --gpus all \
            -v "$SCRIPT_DIR/entrypoint.sh:/app/entrypoint.sh" \
            -v "$(pwd)/output:/app/output" \
            ranstruct:latest \
            validate --input "/app/$INPUT_FILE" --export-sft chatml
        ;;
    
    *)
        echo "用法: $0 {run|test|shell|validate} [额外参数]"
        echo ""
        echo "模式说明:"
        echo "  run      - 运行完整数据集生成流程"
        echo "  test     - 测试模式（仅处理 10 个 chunks）"
        echo "  shell    - 进入交互式 Shell"
        echo "  validate - 验证并导出数据集"
        exit 1
        ;;
esac

echo ""
echo "=============================================="
echo "完成！输出文件在 output/ 目录"
echo "=============================================="

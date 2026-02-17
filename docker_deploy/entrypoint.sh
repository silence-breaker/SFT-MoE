#!/bin/bash
# ============================================================================
# RANSTRUCT Docker 入口脚本
# 功能：启动 Ollama 服务 → 拉取模型 → 执行数据集生成
# ============================================================================

set -e

# 颜色输出
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

log_info() {
    echo -e "${BLUE}[INFO]${NC} $(date '+%Y-%m-%d %H:%M:%S') $1"
}

log_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $(date '+%Y-%m-%d %H:%M:%S') $1"
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $(date '+%Y-%m-%d %H:%M:%S') $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $(date '+%Y-%m-%d %H:%M:%S') $1"
}

# ============================================================================
# 0. 修复 NumPy 版本兼容性 (faiss 不支持 NumPy 2.x)
# ============================================================================
fix_numpy() {
    log_info "检查 NumPy 版本兼容性..."
    NUMPY_VERSION=$(python -c "import numpy; print(numpy.__version__)" 2>/dev/null || echo "0")
    if [[ "$NUMPY_VERSION" == 2.* ]]; then
        log_warn "检测到 NumPy $NUMPY_VERSION，降级到兼容版本..."
        pip install 'numpy<2.0' --force-reinstall
        log_success "NumPy 已降级"
    else
        log_success "NumPy 版本 $NUMPY_VERSION 兼容"
    fi
}

# ============================================================================
# 0.5. 检查嵌入模型 (使用本地离线模型)
# ============================================================================
predownload_embedding_model() {
    log_info "检查嵌入模型..."
    
    if [ -d "/app/models/bge-small-en-v1.5" ]; then
        log_success "发现本地嵌入模型: /app/models/bge-small-en-v1.5"
    else
        log_warn "未找到本地嵌入模型，将尝试在线下载..."
        log_warn "如果下载失败，请在本地运行以下命令下载模型后上传到服务器:"
        log_warn "  python -c \"from sentence_transformers import SentenceTransformer; m=SentenceTransformer('BAAI/bge-small-en-v1.5'); m.save('models/bge-small-en-v1.5')\""
    fi
}

# ============================================================================
# 1. 检查 GPU 可用性
# ============================================================================
check_gpu() {
    log_info "检查 GPU 可用性..."
    if command -v nvidia-smi &> /dev/null; then
        GPU_COUNT=$(nvidia-smi --query-gpu=count --format=csv,noheader | head -1)
        log_success "检测到 ${GPU_COUNT} 张 GPU"
        nvidia-smi --query-gpu=index,name,memory.total --format=csv
    else
        log_warn "未检测到 nvidia-smi，将使用 CPU 模式"
    fi
}

# ============================================================================
# 2. 启动 Ollama 服务
# ============================================================================
start_ollama() {
    log_info "启动 Ollama 服务..."
    
    # 设置 Ollama 环境变量
    export OLLAMA_HOST=${OLLAMA_HOST:-"0.0.0.0:11434"}
    export OLLAMA_NUM_PARALLEL=${OLLAMA_NUM_PARALLEL:-32}
    export OLLAMA_MAX_LOADED_MODELS=${OLLAMA_MAX_LOADED_MODELS:-2}
    export OLLAMA_FLASH_ATTENTION=${OLLAMA_FLASH_ATTENTION:-1}
    
    # 支持自定义模型路径 (Singularity 兼容)
    if [ -n "$OLLAMA_MODELS" ]; then
        log_info "使用自定义模型路径: $OLLAMA_MODELS"
        mkdir -p "$OLLAMA_MODELS"
    fi
    
    log_info "Ollama 配置:"
    log_info "  - OLLAMA_HOST: $OLLAMA_HOST"
    log_info "  - OLLAMA_NUM_PARALLEL: $OLLAMA_NUM_PARALLEL"
    log_info "  - OLLAMA_MAX_LOADED_MODELS: $OLLAMA_MAX_LOADED_MODELS"
    log_info "  - OLLAMA_FLASH_ATTENTION: $OLLAMA_FLASH_ATTENTION"
    [ -n "$OLLAMA_MODELS" ] && log_info "  - OLLAMA_MODELS: $OLLAMA_MODELS"
    
    # 启动 Ollama 后台服务
    mkdir -p /app/logs
    nohup ollama serve > /app/logs/ollama.log 2>&1 &
    OLLAMA_PID=$!
    echo $OLLAMA_PID > /app/logs/ollama.pid
    
    # 等待 Ollama 启动
    log_info "等待 Ollama 服务就绪..."
    MAX_RETRIES=60
    count=0
    until curl -s http://localhost:11434/api/tags > /dev/null 2>&1; do
        sleep 2
        count=$((count+1))
        if [ $count -ge $MAX_RETRIES ]; then
            log_error "Ollama 启动超时，请检查 /app/logs/ollama.log"
            cat /app/logs/ollama.log
            exit 1
        fi
        echo -n "."
    done
    echo ""
    log_success "Ollama 服务已就绪 (PID: $OLLAMA_PID)"
}

# ============================================================================
# 3. 拉取所需模型
# ============================================================================
pull_models() {
    # 默认模型列表（可通过环境变量覆盖）
    MODELS=${MODELS_TO_PULL:-"mistral:latest qwen2.5:1.5b"}
    
    log_info "拉取所需模型: $MODELS"
    
    for model in $MODELS; do
        log_info "正在拉取模型: $model"
        if ollama pull "$model"; then
            log_success "模型 $model 拉取成功"
        else
            log_error "模型 $model 拉取失败"
            exit 1
        fi
    done
    
    log_info "已安装的模型:"
    ollama list
}

# ============================================================================
# 4. 准备数据源
# ============================================================================
prepare_datasource() {
    log_info "检查数据源目录..."
    
    if [ -z "$(ls -A /app/datasource 2>/dev/null)" ]; then
        log_warn "/app/datasource 为空，复制模板数据..."
        cp -r /app/datasource_template/* /app/datasource/ 2>/dev/null || true
    fi
    
    # 显示数据源统计
    if [ -d "/app/datasource/ORAN_Specification" ]; then
        SPEC_COUNT=$(find /app/datasource/ORAN_Specification -name "*.md" | wc -l)
        log_info "O-RAN 规范文档数量: $SPEC_COUNT"
    fi
    
    if [ -d "/app/datasource/codeset" ]; then
        CODE_COUNT=$(find /app/datasource/codeset -name "*.cpp" -o -name "*.h" | wc -l)
        log_info "srsRAN 代码文件数量: $CODE_COUNT"
    fi
    
    if [ -f "/app/datasource/FAISS-v2.0/index.faiss" ]; then
        log_success "检测到预构建的 FAISS 索引"
    else
        log_warn "未检测到 FAISS 索引，将在运行时构建"
    fi
}

# ============================================================================
# 5. 运行主程序
# ============================================================================
run_main() {
    log_info "=========================================="
    log_info "开始执行 RANSTRUCT 数据集生成"
    log_info "=========================================="
    
    cd /app
    
    # 根据参数执行不同命令
    if [ $# -eq 0 ]; then
        # 默认：运行完整流程
        log_info "运行完整数据集生成流程..."
        python ranstruct/main.py run --format chatml --timestamp
    elif [ "$1" = "bash" ] || [ "$1" = "shell" ]; then
        # 进入交互式 shell
        log_info "进入交互式 Shell..."
        exec /bin/bash
    elif [ "$1" = "generate" ]; then
        # 快速生成（跳过数据加载，使用现有 FAISS）
        shift
        log_info "快速生成模式..."
        python ranstruct/main.py run --skip-data --format chatml --timestamp "$@"
    elif [ "$1" = "validate" ]; then
        # 验证数据集
        shift
        log_info "验证数据集..."
        python ranstruct/validate_dataset.py "$@"
    elif [ "$1" = "export" ]; then
        # 导出为 SFT 格式
        shift
        INPUT_FILE=${1:-"/app/output/ranstruct_dataset_cleaned.jsonl"}
        log_info "导出数据集为 ChatML 格式..."
        python ranstruct/validate_dataset.py --input "$INPUT_FILE" --export-sft chatml
    else
        # 传递给 main.py
        log_info "执行: python ranstruct/main.py $@"
        python ranstruct/main.py "$@"
    fi
}

# ============================================================================
# 主流程
# ============================================================================
main() {
    echo ""
    echo "=============================================="
    echo "  RANSTRUCT - O-RAN SFT 数据集生成器"
    echo "  目标模型: Qwen3-30B-A3B"
    echo "  输出格式: ChatML"
    echo "=============================================="
    echo ""
    
    # 创建日志目录
    mkdir -p /app/logs /app/output
    
    # 修复 NumPy 版本
    fix_numpy
    
    # 预下载嵌入模型
    predownload_embedding_model
    
    # 检查 GPU
    check_gpu
    
    # 启动 Ollama
    start_ollama
    
    # 拉取模型
    pull_models
    
    # 准备数据源
    prepare_datasource
    
    # 运行主程序
    run_main "$@"
    
    log_success "=========================================="
    log_success "数据集生成完成！"
    log_success "输出目录: /app/output/"
    log_success "=========================================="
}

# 执行主函数
main "$@"

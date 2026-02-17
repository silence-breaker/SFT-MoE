#!/bin/bash
# ============================================================================
# Qwen3-30B-A3B SFT 训练管理脚本 (LLaMA-Factory 版)
#
# 宿主机子命令: download, train, merge, infer, infer_test, shell, status, all
# 容器内子命令: _train (由 train 子命令自动调用，无需手动执行)
#
# 用法: ./run_train_test.sh <command> [args]
# ============================================================================


set -e

# ============================================================================
# 路径配置
# ============================================================================
WORK_DIR="$HOME/ranstruct_workplace"
TRAIN_DIR="$WORK_DIR/train"
MODEL_DIR="$WORK_DIR/models/Qwen3-30B-A3B-Instruct-2507"
DATASET_DIR="$WORK_DIR/output/dataset"
HF_CACHE="$WORK_DIR/hf_cache"
OUTPUT_DIR="$TRAIN_DIR/output"

# 容器内路径
C_MODEL="/app/model"
C_DATA="/app/data"
C_OUTPUT="/app/output"
C_CONFIG="/app/config"
C_SCRIPT="/app/scripts/run_train_test.sh"

# Docker
IMAGE="sft-train:latest"
COMPOSE_FILE="docker-compose.train.yml"

# ============================================================================
# 辅助函数
# ============================================================================
header() {
    echo ""
    echo "=============================================="
    echo "  $1"
    echo "=============================================="
}

check_image() {
    if ! sudo docker image inspect "$IMAGE" &>/dev/null; then
        echo "❌ 镜像 $IMAGE 不存在，请先构建: sudo docker build -t sft-train -f Dockerfile.train ."
        exit 1
    fi
}

check_model() {
    if [ ! -d "$MODEL_DIR" ] || [ -z "$(ls -A "$MODEL_DIR" 2>/dev/null)" ]; then
        echo "❌ 模型目录为空: $MODEL_DIR"
        echo "请先运行: $0 download"
        exit 1
    fi
}

check_dataset() {
    if [ ! -f "$DATASET_DIR/oran_train.jsonl" ]; then
        echo "❌ 未找到训练集: $DATASET_DIR/oran_train.jsonl"
        exit 1
    fi
    if [ ! -f "$DATASET_DIR/oran_val.jsonl" ]; then
        echo "❌ 未找到验证集: $DATASET_DIR/oran_val.jsonl"
        exit 1
    fi
}

# 获取最新 checkpoint 路径
latest_checkpoint() {
    find "$OUTPUT_DIR" -name "checkpoint-*" -type d 2>/dev/null | sort -V | tail -1
}

docker_run() {
    # 通用 docker run，挂载所有必要卷
    local SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
    sudo docker run --gpus all --shm-size 64g --rm -it \
        --ipc=host --network=host \
        -v "$DATASET_DIR":"$C_DATA" \
        -v "$MODEL_DIR":"$C_MODEL" \
        -v "$OUTPUT_DIR":"$C_OUTPUT" \
        -v "$HF_CACHE":/root/.cache/huggingface \
        -v "$SCRIPT_DIR/run_train_test.sh":"$C_SCRIPT" \
        -v "$SCRIPT_DIR/train_config.yaml":"$C_CONFIG/train_config.yaml" \
        -v "$SCRIPT_DIR/ds_z3_config.json":"$C_CONFIG/ds_z3_config.json" \
        -v "$SCRIPT_DIR/dataset_info.json":"$C_DATA/dataset_info.json" \
        -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \
        -e NVIDIA_VISIBLE_DEVICES=all \
        -e NCCL_P2P_DISABLE=0 \
        -e NCCL_IB_DISABLE=1 \
        -e HF_ENDPOINT="${HF_ENDPOINT:-https://huggingface.co}" \
        -w /app \
        "$IMAGE" \
        "$@"
}

# ============================================================================
# 宿主机子命令
# ============================================================================

# ---- download: 下载模型 ----
cmd_download() {
    header "下载 Qwen3-30B-A3B-Instruct-2507"  # 更新标题
    check_image
    mkdir -p "$MODEL_DIR" "$HF_CACHE"

    sudo docker run --rm -it \
        -v "$WORK_DIR/models":/app/models \
        -v "$HF_CACHE":/root/.cache/huggingface \
        -e HF_ENDPOINT="${HF_ENDPOINT:-https://hf-mirror.com}" \
        "$IMAGE" \
        huggingface-cli download Qwen/Qwen3-30B-A3B-Instruct-2507 \
            --local-dir /app/models/Qwen3-30B-A3B-Instruct-2507

    echo ""
    echo "✅ 模型下载完成"
    echo "模型大小: $(du -sh "$MODEL_DIR" | cut -f1)"
}

# ---- train: 启动训练 ----
cmd_train() {
    header "启动 LoRA SFT 训练 (LLaMA-Factory)"
    check_image
    check_model
    check_dataset
    mkdir -p "$OUTPUT_DIR"
    local TRAIN_COUNT=$(wc -l < "$DATASET_DIR/oran_train.jsonl")
    local VAL_COUNT=$(wc -l < "$DATASET_DIR/oran_val.jsonl")
    echo "训练集: ${TRAIN_COUNT} 条 | 验证集: ${VAL_COUNT} 条"
    echo "模型: $MODEL_DIR"
    echo "输出: $OUTPUT_DIR"
    echo ""
    echo "💡 建议在 tmux 中运行: tmux new -s train"
    echo ""

    docker_run bash "$C_SCRIPT" _train
}

# ---- merge: 合并 LoRA ----
cmd_merge() {
    local CKPT="$1"
    header "合并 LoRA 权重"
    check_image

    if [ -z "$CKPT" ]; then
        echo "可用的 checkpoint:"
        find "$OUTPUT_DIR" -name "checkpoint-*" -type d 2>/dev/null | sort -V | \
            sed "s|$OUTPUT_DIR/||"
        echo ""
        echo "用法: $0 merge <relative_checkpoint_path>"
        echo "示例: $0 merge checkpoint-500"
        exit 1
    fi

    local MERGE_OUTPUT="$C_OUTPUT/merged_${CKPT##*/}"
    docker_run llamafactory-cli export \
        --model_name_or_path "$C_MODEL" \
        --adapter_name_or_path "$C_OUTPUT/$CKPT" \
        --template qwen3 \
        --finetuning_type lora \
        --export_dir "$MERGE_OUTPUT" \
        --export_size 5 \
        --export_legacy_format false \
        --export_device auto  # <--- 新增：让 HF 自动规划设备，避免单卡显存溢出
    echo ""
    echo "✅ LoRA 合并完成 → $MERGE_OUTPUT"
}

# ---- infer: 推理验证 ----
cmd_infer() {
    local CKPT="$1"
    header "推理验证"
    check_image

    if [ -z "$CKPT" ]; then
        echo "用法: $0 infer <relative_checkpoint_path>"
        exit 1
    fi

    docker_run llamafactory-cli chat \
        --model_name_or_path "$C_MODEL" \
        --adapter_name_or_path "$C_OUTPUT/$CKPT" \
        --template qwen3 \
        --finetuning_type lora \
        --infer_backend vllm \
        --vllm_config '{"tensor_parallel_size": 8}'
}

# ---- infer_test: 批量推理测试正确率 ----
cmd_infer_test() {
    local CKPT="$1"
    header "批量推理正确率测试 (oran_val_600)"
    check_image
    check_model

    if [ ! -f "$DATASET_DIR/oran_val_600.jsonl" ]; then
        echo "❌ 未找到测试集: $DATASET_DIR/oran_val_600.jsonl"
        exit 1
    fi

    local TEST_COUNT=$(wc -l < "$DATASET_DIR/oran_val_600.jsonl")
    echo "测试集: ${TEST_COUNT} 条"

    # 构建 adapter 参数和输出文件名
    local ADAPTER_ARG=""
    local RESULT_SUFFIX="base"
    if [ -n "$CKPT" ]; then
        ADAPTER_ARG="--adapter $C_OUTPUT/$CKPT"
        RESULT_SUFFIX="${CKPT##*/}"
        echo "Checkpoint: $CKPT"
    else
        echo "模式: 纯基座模型 (无 LoRA)"
    fi
    echo ""

    local SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
    sudo docker run --gpus all --shm-size 64g --rm -it \
        --ipc=host --network=host \
        -v "$DATASET_DIR":"$C_DATA" \
        -v "$MODEL_DIR":"$C_MODEL" \
        -v "$OUTPUT_DIR":"$C_OUTPUT" \
        -v "$HF_CACHE":/root/.cache/huggingface \
        -v "$WORK_DIR/train/infer_test_hf.py":/app/scripts/infer_test_hf.py \
        -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \
        -w /app \
        "$IMAGE" \
        bash -c "python3 /app/scripts/infer_test_hf.py \
            --model $C_MODEL \
            $ADAPTER_ARG \
            --data $C_DATA/oran_val_600.jsonl \
            --output $C_OUTPUT/infer_test_results_${RESULT_SUFFIX}.jsonl"

    echo ""
    echo "📊 结果文件: $OUTPUT_DIR/infer_PLLtest_results_${RESULT_SUFFIX}.jsonl"
}

# ---- shell: 进入容器交互 ----
cmd_shell() {
    header "进入训练容器 Shell"
    check_image
    mkdir -p "$OUTPUT_DIR"
    docker_run bash
}

# ---- status: 查看训练状态 ----
cmd_status() {
    header "训练状态"

    echo "📦 镜像:"
    if sudo docker image inspect "$IMAGE" &>/dev/null; then
        echo "  ✅ $IMAGE 已构建"
    else
        echo "  ❌ $IMAGE 未构建"
    fi

    echo ""
    echo "🧠 模型:"
    if [ -d "$MODEL_DIR" ] && [ -n "$(ls -A "$MODEL_DIR" 2>/dev/null)" ]; then
        echo "  ✅ $(du -sh "$MODEL_DIR" | cut -f1) - $MODEL_DIR"
    else
        echo "  ❌ 未下载"
    fi

    echo ""
    echo "📊 数据集:"
    if [ -f "$DATASET_DIR/oran_train.jsonl" ]; then
        local TC=$(wc -l < "$DATASET_DIR/oran_train.jsonl")
        local VC=$(wc -l < "$DATASET_DIR/oran_val.jsonl" 2>/dev/null || echo 0)
        echo "  ✅ 训练集: ${TC} 条 | 验证集: ${VC} 条"
    else
        echo "  ❌ 未上传"
    fi

    echo ""
    echo "📁 Checkpoint:"
    if [ -d "$OUTPUT_DIR" ]; then
        local CKPTS=$(find "$OUTPUT_DIR" -name "checkpoint-*" -type d 2>/dev/null | sort -V)
        if [ -n "$CKPTS" ]; then
            echo "$CKPTS" | sed "s|$OUTPUT_DIR/|  📌 |"
        else
            echo "  (无)"
        fi
    else
        echo "  (无)"
    fi
}

# ---- all: 全流程 ----
cmd_all() {
    cmd_download
    cmd_train
}

# ============================================================================
# 容器内子命令 (_train) — 由 cmd_train 自动调用
# ============================================================================
cmd__train() {
    echo "=============================================="
    echo "  Qwen3-30B-A3B LoRA SFT (LLaMA-Factory)"
    echo "=============================================="
    echo ""

    # 安装 TensorBoard（如果尚未安装）
    pip install tensorboard --quiet 2>/dev/null && echo "  ✅ tensorboard 已就绪"


    # ==========================================================
    # 修复 PyTorch 2.4 与新版 transformers 的 DTensor 兼容性问题
    # 方案：直接修改 transformers/__init__.py 源码
    # ==========================================================
    echo "正在应用 DTensor 兼容性补丁..."
    python3 -c "
import os
import transformers

# 找到 transformers 库的安装路径
tf_path = os.path.dirname(transformers.__file__)
init_file = os.path.join(tf_path, '__init__.py')

# 定义补丁代码
patch_code = \"\"\"
# [PATCH START] Compatibility for PyTorch 2.4 + Transformers 4.51
try:
    import torch
    import torch.distributed
    # 尝试从 PyTorch 2.4 的私有位置导入 DTensor
    from torch.distributed._tensor import DTensor, Replicate, Shard
    
    # 如果 torch.distributed.tensor 模块存在（PyTorch 2.4 有这个空壳模块）
    if hasattr(torch.distributed, 'tensor'):
        # 强制注入 DTensor 到 transformers 期望的位置
        torch.distributed.tensor.DTensor = DTensor
        torch.distributed.tensor.Replicate = Replicate
        torch.distributed.tensor.Shard = Shard
except (ImportError, AttributeError):
    pass
# [PATCH END]
\"\"\"

# 读取当前文件内容
with open(init_file, 'r') as f:
    content = f.read()

# 如果尚未打补丁，则写入
if '[PATCH START]' not in content:
    print(f'  📝 正在修改: {init_file}')
    with open(init_file, 'w') as f:
        # 将补丁放在文件最开头，确保最先执行
        f.write(patch_code + '\\n' + content)
    print('  ✅ 补丁已应用')
else:
    print('  ✅ 补丁已存在，跳过')
"
    echo ""

# ... (后续代码保持不变，如 容器内检查 等) ...
    # 容器内检查
    if [ ! -f "$C_DATA/oran_train.jsonl" ]; then
        echo "❌ 容器内未找到训练集 $C_DATA/oran_train.jsonl"
        exit 1
    fi
    if [ ! -d "$C_MODEL" ] || [ -z "$(ls -A "$C_MODEL" 2>/dev/null)" ]; then
        echo "❌ 容器内模型目录为空 $C_MODEL"
        exit 1
    fi
    if [ ! -f "$C_CONFIG/train_config.yaml" ]; then
        echo "❌ 容器内未找到训练配置 $C_CONFIG/train_config.yaml"
        exit 1
    fi

    # 环境信息
    echo "环境信息:"
    python3 -c "import torch; print(f'  PyTorch: {torch.__version__}, CUDA: {torch.version.cuda}')" 2>/dev/null || true
    python3 -c "import flash_attn; print(f'  FlashAttn: {flash_attn.__version__}')" 2>/dev/null || true
    python3 -c "import llamafactory; print(f'  LLaMA-Factory OK')" 2>/dev/null || true
    deepspeed --version 2>/dev/null || true
    echo ""

    # 数据集信息
    local TRAIN_COUNT=$(wc -l < "$C_DATA/oran_train.jsonl")
    local VAL_COUNT=$(wc -l < "$C_DATA/oran_val.jsonl")
    echo "训练集: ${TRAIN_COUNT} 条 | 验证集: ${VAL_COUNT} 条"
    echo ""

    # GPU 信息
    echo "GPU 信息:"
    nvidia-smi --query-gpu=index,name,memory.total --format=csv,noheader
    echo ""

    echo "开始训练..."
    echo "=============================================="

    # LLaMA-Factory 多卡训练
    FORCE_TORCHRUN=1 \
    NNODES=1 \
    NPROC_PER_NODE=8 \
    llamafactory-cli train "$C_CONFIG/train_config.yaml"

    echo ""
    echo "=============================================="
    echo "✅ 训练完成！"
    echo "=============================================="
    echo ""
    echo "下一步 (在宿主机执行):"
    echo "  ./run_train_test.sh merge <checkpoint_dir>"
    echo "  ./run_train_test.sh infer <checkpoint_dir>"
    echo ""
    echo "📊 查看 TensorBoard 日志 (从本地机器执行):"
    echo "  ssh -L 6006:localhost:6006 lijindong@210.75.240.12"
    echo "  然后在服务器上: cd ~/ranstruct_workplace/train && tensorboard --logdir output"
    echo "  本地浏览器打开: http://localhost:6006"
}

# ============================================================================
# 入口
# ============================================================================
case "${1:-help}" in
    download)       cmd_download ;;
    train)          cmd_train ;;
    merge)          cmd_merge "$2" ;;
    infer)          cmd_infer "$2" ;;
    infer_test)     cmd_infer_test "$2" ;;
    shell)          cmd_shell ;;
    status)         cmd_status ;;
    all)            cmd_all ;;
    _train)         cmd__train ;;
    help|*)
        echo "Qwen3-30B-A3B SFT 训练管理工具 (LLaMA-Factory)"
        echo ""
        echo "用法: $0 <command> [args]"
        echo ""
        echo "命令:"
        echo "  download        下载 Qwen3-30B-A3B 模型 (~61GB)"
        echo "  train           启动 LoRA SFT 训练"
        echo "  merge <ckpt>    合并 LoRA 权重到基座模型"
        echo "  infer <ckpt>    用微调后的模型进行推理"
        echo "  infer_test [ckpt] 批量推理测试集并计算正确率 (不传ckpt则测基座模型)"
        echo "  shell           进入训练容器的交互式 Shell"
        echo "  status          查看当前状态 (镜像/模型/数据/checkpoint)"
        echo "  all             一键执行: download → train"
        echo ""
        echo "推荐流程:"
        echo "  $0 download           # 1. 下载模型"
        echo "  $0 status             # 2. 确认一切就绪"
        echo "  tmux new -s train     # 3. 进入 tmux"
        echo "  $0 train              # 4. 开始训练"
        echo "  $0 merge <ckpt>       # 5. 合并 LoRA"
        echo "  $0 infer <ckpt>       # 6. 推理验证"
        echo "  $0 infer_test [ckpt]  # 7. 批量测试正确率 (可选ckpt，不传测基座)"
        ;;
esac

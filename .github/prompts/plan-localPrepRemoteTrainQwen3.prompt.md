# Plan: 本地整理数据 + 远程服务器 Docker 训练 Qwen3-30B-A3B

在本地合并去重 8 个数据集文件，上传到远程服务器 `lijindong@210.75.240.12`。在服务器上新建 ms-swift 训练专用 Docker 镜像，下载 Qwen3-30B-A3B 模型，使用 LoRA + DeepSpeed ZeRO-3 在 8×A100 40GB 上完成微调。整体沿用现有 `ranstruct_workplace` 目录结构和 rsync/ssh 上传模式。

**Steps**

## 阶段一：本地操作

### 1. 合并去重数据集（本地）

在项目根目录创建 `scripts/merge_dataset.py`，读取 `output/dataset/` 下全部 8 个 `*_sft_chatml.jsonl` 文件，按 user message 内容哈希去重，输出：
- `output/dataset/oran_train.jsonl`（95% 训练集）
- `output/dataset/oran_val.jsonl`（5% 验证集）

逻辑：遍历所有文件 → 逐行解析 JSON → 提取 `messages[1]["content"]`（user 问题）做 MD5 去重 → 随机 shuffle → 按比例切分 → 写出两个文件。脚本最后打印总条数、去重后条数、训练/验证集条数。

### 2. 上传数据集到服务器（本地）

参照现有 `docker_deploy/upload_to_server.sh` 的模式（`rsync` 到 `lijindong@210.75.240.12:~/ranstruct_workplace/`）：

```bash
rsync -avz --progress output/dataset/oran_train.jsonl output/dataset/oran_val.jsonl \
    lijindong@210.75.240.12:~/ranstruct_workplace/output/dataset/
```

### 3. 上传训练相关文件到服务器（本地）

将后续步骤中创建的 Dockerfile、训练脚本等一起上传：

```bash
rsync -avz --progress docker_deploy/train/ \
    lijindong@210.75.240.12:~/ranstruct_workplace/train/
```

## 阶段二：构建训练 Docker 镜像

### 4. 创建训练专用 Dockerfile（本地创建，上传到服务器构建）

在 `docker_deploy/train/` 目录下创建 `Dockerfile.train`，基于 `nvidia/cuda:12.4.1-devel-ubuntu20.04`，安装：
- Python 3.10 + pip
- `ms-swift[all]`（含 transformers, peft, accelerate 等）
- `deepspeed >= 0.17`
- `flash-attn`（需 `--no-build-isolation`，编译较久）
- `liger-kernel`
- `transformers >= 4.51.0`

同时创建 `docker-compose.train.yml`，挂载卷：

| 宿主机路径 | 容器路径 | 用途 |
|---|---|---|
| `~/ranstruct_workplace/output/dataset` | `/app/data` | 训练/验证数据集 |
| `~/ranstruct_workplace/models/Qwen3-30B-A3B` | `/app/model` | 模型权重 |
| `~/ranstruct_workplace/train/output` | `/app/output` | 训练输出（checkpoint、日志） |
| `~/ranstruct_workplace/hf_cache` | `/root/.cache/huggingface` | HF 缓存 |

GPU 配置：`--gpus all --shm-size 64G`（DeepSpeed 多卡通信需要大 shared memory）。

### 5. 在服务器上构建镜像

```bash
ssh lijindong@210.75.240.12
cd ~/ranstruct_workplace/train
docker build -t sft-train:latest -f Dockerfile.train .
```

构建时间约 20-40 分钟（主要是编译 flash-attn）。

## 阶段三：下载模型

### 6. 在服务器上下载 Qwen3-30B-A3B（~61GB）

可以在构建好的容器内下载（利用容器内的 Python 环境），也可以在宿主机安装 `huggingface-cli`：

```bash
# 方案 A：在容器内下载（推荐，环境干净）
docker run --rm -it \
    -v ~/ranstruct_workplace/models:/app/models \
    -v ~/ranstruct_workplace/hf_cache:/root/.cache/huggingface \
    sft-train:latest \
    huggingface-cli download Qwen/Qwen3-30B-A3B \
        --local-dir /app/models/Qwen3-30B-A3B
```
如果服务器访问 HuggingFace 受限，可设置镜像：`export HF_ENDPOINT=https://hf-mirror.com`

## 阶段四：启动训练

### 7. 创建训练启动脚本 `train.sh`

在 `docker_deploy/train/` 下创建 `train.sh`，容器内执行：

```bash
#!/bin/bash
CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \
NPROC_PER_NODE=8 \
swift sft \
    --model /app/model \
    --tuner_type lora \
    --dataset /app/data/oran_train.jsonl \
    --val_dataset /app/data/oran_val.jsonl \
    --torch_dtype bfloat16 \
    --num_train_epochs 2 \
    --per_device_train_batch_size 1 \
    --per_device_eval_batch_size 1 \
    --learning_rate 1e-4 \
    --lora_rank 8 \
    --lora_alpha 32 \
    --target_modules all-linear \
    --gradient_accumulation_steps 2 \
    --eval_steps 100 \
    --save_steps 100 \
    --save_total_limit 3 \
    --logging_steps 5 \
    --max_length 2048 \
    --output_dir /app/output \
    --system "You are an O-RAN Technical Expert with comprehensive knowledge of Open RAN architecture, 3GPP specifications, and telecommunications systems. Provide accurate, detailed, and technically precise answers about O-RAN components, interfaces, protocols, and implementations." \
    --warmup_ratio 0.05 \
    --dataloader_num_workers 4 \
    --deepspeed zero3 \
    --use_liger_kernel true \
    --attn_impl flash_attn \
    --loss_scale ignore_empty_think
```

### 8. 启动训练容器

```bash
docker run --gpus all --shm-size 64G --rm -it \
    -v ~/ranstruct_workplace/output/dataset:/app/data \
    -v ~/ranstruct_workplace/models/Qwen3-30B-A3B:/app/model \
    -v ~/ranstruct_workplace/train/output:/app/output \
    -v ~/ranstruct_workplace/hf_cache:/root/.cache/huggingface \
    -w /app \
    sft-train:latest \
    bash /app/train.sh
```

建议在 `tmux` 或 `screen` 中运行，防止 SSH 断连中断训练。预估训练时间：~4000 条数据、2 epoch、batch_size 16，约 2-4 小时。

## 阶段五：合并与推理

### 9. 合并 LoRA 权重

训练完成后，checkpoint 保存在 `~/ranstruct_workplace/train/output/` 下：

```bash
docker run --gpus all --rm -it \
    -v ~/ranstruct_workplace/models/Qwen3-30B-A3B:/app/model \
    -v ~/ranstruct_workplace/train/output:/app/output \
    -v ~/ranstruct_workplace/hf_cache:/root/.cache/huggingface \
    sft-train:latest \
    swift export \
        --adapters /app/output/vx-xxx/checkpoint-xxx \
        --merge_lora true
```

合并后模型保存在 checkpoint 同级的 `-merged` 目录。

### 10. 推理验证

```bash
docker run --gpus all --rm -it \
    -v ~/ranstruct_workplace/train/output:/app/output \
    -v ~/ranstruct_workplace/hf_cache:/root/.cache/huggingface \
    sft-train:latest \
    swift infer \
        --adapters /app/output/vx-xxx/checkpoint-xxx \
        --stream true \
        --temperature 0.6 \
        --max_new_tokens 2048
```

## Verification

1. **数据合并**：运行 `merge_dataset.py` 后确认打印的去重条数合理（预期 ~4000-30000 条，取决于 8 个文件间重复率）
2. **Docker 构建**：`docker run --rm sft-train:latest swift --version` 验证 ms-swift 安装成功
3. **模型下载**：`ls -lh ~/ranstruct_workplace/models/Qwen3-30B-A3B/` 确认文件完整（~61GB，多个 safetensors 分片）
4. **训练监控**：训练启动后 `nvidia-smi` 确认 8 卡均有占用且峰值 < 40GB；观察 loss 稳定下降
5. **推理测试**：合并后用 O-RAN 领域问题手动测试回复质量

## Decisions

- **新建 Docker 镜像而非复用 ranstruct 容器**：训练需要 ms-swift + DeepSpeed + flash-attn，与数据生成环境（Ollama）完全不同，隔离更清晰
- **DeepSpeed ZeRO-3**：30.5B 参数 × 2 bytes = ~61GB BF16，单卡 40GB 放不下，必须用 ZeRO-3 分片
- **`--shm-size 64G`**：DeepSpeed 多卡通信依赖 shared memory，默认 64MB 远远不够
- **模型在服务器上下载**：~61GB 权重走网络传输到服务器效率更高，直接在服务器/容器内用 `huggingface-cli` 下载
- **服务器目录复用 `~/ranstruct_workplace/`**：与现有数据生成流程统一管理，新增 `train/` 和 `models/` 子目录

## 远程服务器最终目录结构

```
~/ranstruct_workplace/
├── datasource/                    # 已有 - 数据生成用
├── output/
│   └── dataset/
│       ├── oran_train.jsonl       # 新增 - 合并去重后的训练集
│       ├── oran_val.jsonl         # 新增 - 验证集
│       └── *_sft_chatml.jsonl     # 已有 - 原始生成文件
├── models/
│   ├── bge-small-en-v1.5/        # 已有 - embedding 模型
│   └── Qwen3-30B-A3B/            # 新增 - 基座模型 (~61GB)
├── train/
│   ├── Dockerfile.train           # 新增 - 训练镜像
│   ├── train.sh                   # 新增 - 训练启动脚本
│   └── output/                    # 新增 - checkpoint 输出
├── hf_cache/                      # 已有 - HuggingFace 缓存
└── ...
```

# RANSTRUCT 部署与操作指南

## 📋 目标

在 **8卡 A100 服务器**上生成用于 **Qwen3-30B-A3B** SFT 微调的训练数据集。

输出格式：**ChatML** (Qwen 系列模型原生支持)

---

## ⚠️ 重要：关于 Docker vs Apptainer

**如果你在远程服务器上没有 sudo 权限，那么只能使用 Apptainer！**

| 场景 | 推荐方案 |
|------|---------|
| 有 sudo / 在 docker 组中 | Docker |
| 没有 sudo 权限（HPC/共享服务器） | **Apptainer** |
| 本地开发测试 | Docker |

> **原因**：Docker 守护进程需要 root 权限才能运行。即使使用 `docker run`，也需要用户在 `docker` 组中（需要管理员添加）。
> Apptainer（原 Singularity）专为 HPC 环境设计，**不需要 root 权限**即可运行容器。

---

## 🏗️ 架构概览

```
┌─────────────────────────────────────────────────────────────┐
│                    本地机器 (有 Docker)                       │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐      │
│  │ 构建镜像    │ -> │ 导出 tar    │ -> │ 上传服务器  │      │
│  └─────────────┘    └─────────────┘    └─────────────┘      │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                 A100 服务器 (无 sudo 权限)                    │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐      │
│  │ 转换 SIF    │ -> │ 运行容器    │ -> │ 生成数据集  │      │
│  └─────────────┘    └─────────────┘    └─────────────┘      │
│                              │                               │
│                              ▼                               │
│                    output/xxx_sft_chatml.jsonl               │
│                    (可直接用于 Qwen3 SFT)                     │
└─────────────────────────────────────────────────────────────┘
```

---

## 🚀 快速开始

### 第一步：本地构建 Docker 镜像

在你的**本地机器**（有 Docker 权限）上执行：

```bash
cd /path/to/SFT-MoE

# 方法 1：使用构建脚本（推荐）
chmod +x docker_deploy/build_local.sh
./docker_deploy/build_local.sh

# 方法 2：手动构建
docker build -t ranstruct:latest -f docker_deploy/Dockerfile .
docker save ranstruct:latest | gzip > ranstruct_docker.tar.gz
```

构建完成后，你会得到一个 `ranstruct_docker.tar.gz` 文件（约 5-8GB）。

### 第二步：上传到服务器

```bash
# 上传镜像文件
scp ranstruct_docker.tar.gz user@server:/home/user/ranstruct/

# 上传数据源（如果服务器上没有）
scp -r datasource user@server:/home/user/ranstruct/
```

### 第三步：服务器端运行

登录服务器后：

```bash
ssh user@server
cd /home/user/ranstruct
```

#### 方案 A：如果你在 docker 组中（有 Docker 权限）

```bash
# 检查是否有 Docker 权限
docker ps  # 如果报错 "permission denied"，说明没有权限，请用方案 B

# 加载镜像
docker load < ranstruct_docker.tar.gz

# 运行数据集生成
chmod +x docker_deploy/run_docker.sh
./docker_deploy/run_docker.sh run

# 或者使用 docker-compose
cd docker_deploy
docker-compose up
```


---

## 📖 详细命令说明

### 运行模式

| 命令 | 说明 |
|------|------|
| `./run_*.sh run` | 完整数据集生成流程 |
| `./run_*.sh test` | 测试模式（仅 10 个 chunks） |
| `./run_*.sh shell` | 进入交互式 Shell |
| `./run_*.sh validate` | 验证数据集并导出 ChatML |

### 自定义参数

```bash
# 限制处理的 chunks 数量
./run_docker.sh run --max-chunks 500

# 每个 chunk 生成更多问题
./run_docker.sh run --questions-per-chunk 5

# 增加 RAG 检索数量
./run_docker.sh run --top-k 5
```

### 验证数据集

```bash
# 验证最新生成的数据集
./run_docker.sh validate output/ranstruct_dataset_cleaned_*.jsonl

# 验证并导出为 ChatML 格式
./run_docker.sh validate output/ranstruct_dataset_cleaned_*.jsonl --export-sft chatml
```

---

## 📁 输出文件说明

生成完成后，`output/` 目录下会有以下文件：

```
output/
├── ranstruct_dataset_20260204_143022.jsonl          # 原始数据集（含元数据）
├── ranstruct_dataset_cleaned_20260204_143022.jsonl  # 清洗后数据集
└── ranstruct_dataset_cleaned_20260204_143022_sft_chatml.jsonl  # ⭐ SFT 训练格式
```

### ChatML 格式示例

```json
{
  "messages": [
    {
      "role": "system",
      "content": "You are an O-RAN Technical Expert..."
    },
    {
      "role": "user", 
      "content": "What is the purpose of the E1 interface in O-RAN architecture?"
    },
    {
      "role": "assistant",
      "content": "The E1 interface connects the O-CU-CP and O-CU-UP..."
    }
  ]
}
```

此格式可直接用于 Qwen3-30B-A3B 的 SFT 微调。

---

## ⚙️ 环境变量配置

可通过环境变量自定义行为：

| 变量 | 默认值 | 说明 |
|------|--------|------|
| `MODELS_TO_PULL` | `mistral:latest qwen2.5:1.5b` | 要拉取的 Ollama 模型 |
| `OLLAMA_NUM_PARALLEL` | `32` | Ollama 并发数 |
| `OLLAMA_MAX_LOADED_MODELS` | `2` | 同时加载的模型数 |
| `CUDA_VISIBLE_DEVICES` | `0,1,2,3,4,5,6,7` | 可见 GPU |

示例：

```bash
export MODELS_TO_PULL="qwen2.5:7b mistral:7b"
./run_apptainer.sh run
```

---

## 🔧 故障排除

### 1. Ollama 启动超时

```bash
# 查看 Ollama 日志
cat logs/ollama.log

# 常见原因：GPU 驱动问题
nvidia-smi  # 检查 GPU 状态
```

### 2. 显存不足

```bash
# 减少并发数
export OLLAMA_NUM_PARALLEL=8
export OLLAMA_MAX_LOADED_MODELS=1
```

### 3. Apptainer 权限问题

```bash
# 如果遇到 fakeroot 问题，在本地转换 SIF 后再上传
# 本地执行：
apptainer build ranstruct.sif docker-archive://ranstruct_docker.tar.gz
scp ranstruct.sif user@server:/home/user/ranstruct/
```

### 4. 数据源为空

确保 `datasource/` 目录结构正确：

```
datasource/
├── ORAN_Specification/    # O-RAN 规范文档 (.md)
├── codeset/               # srsRAN 代码 (.cpp, .h)
└── FAISS-v2.0/           # 预构建索引（可选）
    └── index.faiss
```

---

## 📊 预期输出

在 8 卡 A100 上的典型性能：

| 阶段 | 耗时估计 |
|------|---------|
| Ollama 启动 + 模型下载 | 5-10 分钟（首次） |
| 数据加载 + FAISS 构建 | 10-30 分钟 |
| 问题生成 (1000 chunks) | 2-4 小时 |
| 答案生成 (3000 questions) | 4-8 小时 |
| 后处理 + 导出 | 5 分钟 |

**总计**：约 8-12 小时生成 ~3000 条高质量 QA 对

---

## 🎯 后续：用于 Qwen3 微调

生成的 `*_sft_chatml.jsonl` 文件可直接用于以下框架：

- **LLaMA-Factory**: 支持 ChatML 格式
- **swift (modelscope)**: Qwen 官方推荐
- **axolotl**: 支持自定义格式

示例（LLaMA-Factory）：

```yaml
# dataset_info.yaml
oran_sft:
  file_name: ranstruct_dataset_cleaned_sft_chatml.jsonl
  formatting: sharegpt
  columns:
    messages: messages
```

---

## 📞 常用命令速查

```bash
# 本地构建
./docker_deploy/build_local.sh

# 服务器运行（Docker）
./docker_deploy/run_docker.sh run

# 服务器运行（Apptainer）
./docker_deploy/run_apptainer.sh run

# 测试模式
./docker_deploy/run_*.sh test

# 进入 Shell 调试
./docker_deploy/run_*.sh shell

# 验证数据集
./docker_deploy/run_*.sh validate output/xxx.jsonl
```

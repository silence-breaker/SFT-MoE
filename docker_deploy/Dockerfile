# ============================================================================
# RANSTRUCT 数据集生成 Docker 镜像
# 目标：生成用于 Qwen3-30B-A3B SFT 微调的训练数据集
# 服务器环境：8x A100 (40GB), CUDA 12.4, Ubuntu 20.04
# ============================================================================

FROM nvidia/cuda:12.4.1-devel-ubuntu22.04

LABEL maintainer="RANSTRUCT"
LABEL description="O-RAN SFT Dataset Generator for Qwen3-30B-A3B"

# ============================================================================
# 环境变量
# ============================================================================
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1
ENV PYTHONIOENCODING=utf-8
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8

# Ollama 配置
ENV OLLAMA_HOST=0.0.0.0:11434
ENV OLLAMA_NUM_PARALLEL=32
ENV OLLAMA_MAX_LOADED_MODELS=2
ENV OLLAMA_FLASH_ATTENTION=1

# CUDA 配置
ENV CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7

# ============================================================================
# 1. 安装系统依赖
# ============================================================================
RUN apt-get update && apt-get install -y \
    python3.10 \
    python3-pip \
    python3.10-dev \
    python3.10-venv \
    curl \
    git \
    wget \
    procps \
    vim \
    htop \
    tmux \
    zstd \
    && rm -rf /var/lib/apt/lists/*

# 设置 python3 为默认 python
RUN ln -sf /usr/bin/python3.10 /usr/bin/python && \
    ln -sf /usr/bin/pip3 /usr/bin/pip

# 升级 pip
RUN pip install --upgrade pip setuptools wheel

# ============================================================================
# 2. 安装 Ollama (用于 LLM 推理)
# ============================================================================
RUN curl -fsSL https://ollama.com/install.sh | sh

# ============================================================================
# 3. 设置工作目录
# ============================================================================
WORKDIR /app

# ============================================================================
# 4. 安装 Python 依赖
# ============================================================================
COPY ranstruct/requirements.txt /app/requirements.txt

# 安装 PyTorch (CUDA 12.4)
RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124

# 安装项目依赖
RUN pip install --no-cache-dir -r requirements.txt

# 安装额外的工具包
RUN pip install --no-cache-dir \
    jsonlines \
    rich \
    typer

# ============================================================================
# 5. 复制项目代码
# ============================================================================
COPY ranstruct /app/ranstruct
COPY datasource /app/datasource_template

# ============================================================================
# 6. 创建目录结构
# ============================================================================
RUN mkdir -p /app/output \
    /app/datasource \
    /app/logs \
    /root/.ollama/models

# ============================================================================
# 7. 复制启动脚本
# ============================================================================
COPY docker_deploy/entrypoint.sh /app/entrypoint.sh
COPY docker_deploy/generate_dataset.sh /app/generate_dataset.sh
RUN chmod +x /app/entrypoint.sh /app/generate_dataset.sh

# ============================================================================
# 8. 健康检查
# ============================================================================
HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \
    CMD curl -f http://localhost:11434/api/tags || exit 1

# ============================================================================
# 9. 暴露端口
# ============================================================================
EXPOSE 11434

# ============================================================================
# 10. 入口点
# ============================================================================
ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["run"]


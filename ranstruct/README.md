# RANSTRUCT - O-RAN 领域数据集生成框架

基于 RAG（检索增强生成）原理的 O-RAN 领域微调数据集生成框架。

## 概述

RANSTRUCT 框架使用两个 LLM 代理生成高质量的问答数据集：
- **Mistral-7B-Instruct-0.3**: 用于问题生成
- **Qwen-2.5-Instruct-1.5B**: 用于答案生成

## 架构

```
ranstruct/
├── __init__.py          # 包初始化
├── config.py            # 配置管理
├── config.yaml          # 默认配置文件
├── data_processor.py    # 数据处理与分块
├── faiss_manager.py     # FAISS 向量索引管理
├── question_generator.py # 问题生成模块
├── answer_generator.py  # 答案生成模块
├── pipeline.py          # 主管道模块
├── main.py              # 命令行入口
├── utils.py             # 工具函数
└── requirements.txt     # 依赖列表
quality_improvements.py    # 质量检测与改进辅助函数
post_processor.py         # 数据集后处理与清洗工具
config_optimizations.py   # 优化后的配置和 prompt
```

## 工作流程

### 1. 数据输入处理 (Input Processing)

处理两个主要数据源：
- **O-RAN 规范文档**: 116+ 个文档，约 253 万词
- **srsRAN 代码文件**: 4,980+ 个 C++ 源文件，约 468 万词

数据分块策略：
- **RAG Chunks (1,024 tokens)**: 用于 FAISS 检索
- **LTG Chunks (4,096 tokens)**: 用于问题生成

### 2. FAISS 数据库构建 (FAISS Construction)

- 使用 BGE-Small-EN-1.5 嵌入模型
- 将 RAG Chunks 编码为密集向量
- 建立 FAISS 索引进行高速相似性搜索

### 3. 问题生成 (Question Generation)

- 使用 Mistral-7B-Instruct-0.3 模型
- 针对每个 LTG Chunk 生成多个问题
- 自动去重和清洗

### 4. 答案生成 (Answer Generation)

- 使用 Qwen-2.5-Instruct-1.5B 模型
- 基于 RAG 检索相关上下文
- 生成准确、有依据的答案

## 快速开始

### 安装依赖

```bash
cd ranstruct
pip install -r requirements.txt
```

### 确保 Ollama 服务运行

```bash
# 检查 Ollama 状态
ollama list

# 确保模型已下载
ollama pull mistral:7b-instruct-v0.3
ollama pull qwen2.5:1.5b-instruct
```

### 运行管道

```bash
# 运行完整管道
python main.py run

# 测试模式（限制数量）
python main.py run --max-chunks 10

# 显示配置信息
python main.py info

# 运行测试
python main.py test
```

### 分步执行

```bash
# 步骤 1: 数据加载
python main.py step1

# 步骤 2: FAISS 构建
python main.py step2

# 步骤 3: 问题生成
python main.py step3 --max-chunks 100

# 步骤 4: 答案生成
python main.py step4

# 步骤 5: 保存数据集
python main.py step5 --format jsonl
```

## 编程接口

```python
from ranstruct import Config, RANSTRUCTPipeline

# 创建配置
config = Config()

# 或从 YAML 文件加载
# config = Config.from_yaml("config.yaml")

# 创建管道
pipeline = RANSTRUCTPipeline(config)

# 运行完整管道
results = pipeline.run(
    max_chunks=100,          # 限制处理的 chunks 数量
    questions_per_chunk=5,   # 每个 chunk 生成的问题数
    top_k=3,                 # RAG 检索 Top-K
    output_format="jsonl"    # 输出格式
)

# 获取生成的问答对
qa_pairs = pipeline.get_qa_pairs()
for qa in qa_pairs[:3]:
    print(f"Q: {qa.question}")
    print(f"A: {qa.answer[:200]}...")
    print()
```

## 输出格式

### JSONL 格式 (默认)

```json
{"question": "What is O-RAN?", "answer": "O-RAN is...", "source_chunk_id": "...", "metadata": {...}}
```

### 训练格式 (Alpaca style)

```json
{"instruction": "What is O-RAN?", "input": "", "output": "O-RAN is..."}
```

### 对话格式

```json
{"conversations": [{"role": "user", "content": "What is O-RAN?"}, {"role": "assistant", "content": "O-RAN is..."}]}
```

## 配置说明

参见 `config.yaml` 文件，主要配置项：

| 配置项 | 说明 | 默认值 |
|--------|------|--------|
| `model.question_model` | 问题生成模型 | mistral:7b-instruct-v0.3 |
| `model.answer_model` | 答案生成模型 | qwen2.5:1.5b-instruct |
| `chunk.rag_chunk_size` | RAG Chunk 大小 | 1024 |
| `chunk.ltg_chunk_size` | LTG Chunk 大小 | 4096 |
| `faiss.top_k` | RAG 检索数量 | 3 |
| `generation.questions_per_chunk` | 每 Chunk 问题数 | 5 |

## 数据源

确保以下数据源位于正确位置：

```
datasource/
├── ORAN_Specification/    # O-RAN 规范文档 (.md)
├── codeset/               # 代码集
│   ├── cu_cp/
│   ├── cu_up/
│   ├── du/
│   └── ...
└── FAISS-v2.0/           # 预构建的 FAISS 索引（可选）
    ├── index.faiss
    └── index.pkl
```

## 输出目录

生成的数据集默认保存在 `output/` 目录：

```
output/
├── ranstruct_dataset.jsonl      # 最终数据集
├── generated_questions.jsonl    # 中间结果：生成的问题
└── ranstruct.log                # 运行日志
```

可通过 `config.yaml` 修改输出路径：
```yaml
output:
  output_dir: "output"
  dataset_filename: "ranstruct_dataset.jsonl"
```

## 许可证

MIT License

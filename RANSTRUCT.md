# RANSTRUCT 数据集生成过程

RANSTRUCT 框架生成数据集的过程被称为“指令生成”（Instruction Generation），其核心利用了两个大语言模型（LLM）代理：一个用于生成问题，另一个用于生成答案。该过程基于 RAG（检索增强生成）原理，主要分为以下四个步骤：

1. 输入处理 (Input Processing)
首先，框架处理两个主要的 O-RAN 数据源：

数据源：

O-RAN 规范文档：包含 116 个文档，共约 253 万词。

srsRAN 代码文件：包含 4,980 个 C++ 源文件，共约 468 万词。

数据分块与准备：

使用递归分割器（Recursive Splitter）将文档切分为具有语义意义的块。

针对 O-RAN 规范，创建了两种类型的块：

RAG Chunks（1,024 tokens）：用于 RAG 管道中的高效文档检索。

LTG Chunks（4,096 tokens）：即“长文本生成块”，用于生成高质量的问答对。

针对 srsRAN 代码，不进行分块，而是使用整个代码文件以保留语义上下文。

1. FAISS 数据库构建 (FAISS Construction)
这一步是为了建立检索机制：

使用 BGE-Small-EN-1.5 嵌入模型对 RAG Chunks 进行编码，生成密集向量表示。

将这些向量索引到 FAISS（Facebook AI Similarity Search）数据库中，以便进行高速相似性搜索。

1. 问题生成 (Question Generation)
这一阶段旨在生成指令（问题）：

模型选择：使用 Mistral-7B-Instruct-0.3 模型。

生成过程：针对每个 LTG Chunk（4,096 tokens），提示模型生成多个独特的问题。这些问题必须严格限定在该块的范围内，并确保如果有该块作为上下文，问题是可以被准确回答的。

数据清洗：

去重：将问题列表转换为字典（以问题为键），利用字典键的唯一性自动去除重复问题。

解析：过滤掉截断的、格式错误的或无效的问题，以保证数据集的完整性。

1. 答案生成 (Answer Generation)
最后阶段是生成对应的响应：

模型选择：使用 Qwen-2.5-Instruct-1.5B 模型。

生成过程：

将生成的每个唯一问题输入嵌入生成器，获取其语义表示。

在 FAISS 数据库中检索与问题最相关的 Top 3 个 RAG Chunks。

将“问题”和“检索到的文档”作为上下文提供给 Qwen 模型，使其生成准确且基于上下文的回答。

最终输出：生成的答案与原始问题被组合在一起，追加到微调（fine-tuning）数据集中


Ollama 模型存储路径为:'D:\Ollama\Models'，目前已经下载了Mistral-7B-Instruct-0.3和Qwen-2.5-Instruct-1.5B

数据来源已经存在datasource文件夹中，包含O-RAN规范文档，srsRAN代码文件和FAISS数据库文件，但可能还需要清洗和处理


---

## 幻觉抑制机制 
为了减少 RAG 系统中的幻觉问题，框架实现了以下三层防御机制：

### 1. 置信度阈值过滤 

- **配置项**: `min_retrieval_score` (默认 0.35)
- **原理**: 如果 FAISS 检索结果的最高分数低于阈值，说明知识库中没有高相关性的文档，此时生成的答案很可能是幻觉
- **行为**: 过滤掉低置信度的问题-答案对

```python
# config.py
@dataclass
class FAISSConfig:
    min_retrieval_score: float = 0.35
    enable_confidence_threshold: bool = True
```

### 2. 实体一致性检查 

- **原理**: O-RAN 领域有严格的接口归属关系（如 F1 只能在 CU-DU 之间，E1 只能在 CU-CP 和 CU-UP 之间）
- **实现**: 定义 `ENTITY_CONSISTENCY_RULES` 规则表，在答案生成前后进行实体关系验证
- **行为**: 拒绝违反实体约束的问题或答案

**示例规则**:
```python
ENTITY_CONSISTENCY_RULES = {
    "F1": {"must_contain_any": ["CU", "DU", "gNB"], "must_not_contain": ["SMO", "O2"]},
    "E1": {"must_contain_any": ["CU-CP", "CU-UP", "control plane", "user plane"]},
    "O2ims": {"must_contain_any": ["SMO", "O-Cloud", "Infrastructure"], "must_not_contain": ["F1", "E1"]},
    # ...
}
```

### 3. Cross-Encoder 重排序  🆕

**问题背景**: Bi-Encoder (FAISS) 虽然检索速度快，但对语义相似的不同概念区分度不够（如 "F1 interface" vs "E1 interface" 向量可能非常接近）

**解决方案**: 引入 Cross-Encoder 进行二阶段检索
1. **第一阶段 (粗筛)**: FAISS 返回 Top-10 候选
2. **第二阶段 (精排)**: Cross-Encoder 对每个 (query, document) 对进行交叉编码，计算精确相关性分数
3. **输出**: 返回 Top-3 最相关文档

**配置项**:
```python
# config.py FAISSConfig
enable_reranker: bool = True                      # 启用/禁用 Reranker
reranker_model: str = "BAAI/bge-reranker-base"   # Reranker 模型
reranker_top_k: int = 10                          # FAISS 初筛数量
reranker_final_top_k: int = 3                     # 最终返回数量
reranker_min_score: float = 0.1                   # 最低分数阈值
```

**支持的 Reranker 模型**:
| 模型 | 大小 | 推荐场景 |
|------|------|---------|
| `BAAI/bge-reranker-base` | ~278M | 平衡精度与速度 (默认) |
| `BAAI/bge-reranker-large` | ~560M | 高精度，速度较慢 |
| `cross-encoder/ms-marco-MiniLM-L-6-v2` | ~23M | 轻量级，速度最快 |

**测试 Reranker**:
```bash
cd ranstruct
python test_reranker.py       # 基础测试
python test_reranker.py --full # 包含实体区分测试
```

**API 使用**:
```python
from ranstruct.faiss_manager import RAGRetriever, FAISSManager

# 启用 Reranker
retriever = RAGRetriever(
    faiss_manager,
    enable_reranker=True,
    reranker_model="BAAI/bge-reranker-base"
)

# 检索 (自动使用两阶段检索)
results = retriever.retrieve("What is F1 interface?", top_k=3)

# 比较有无 Reranker 的结果
comparison = retriever.compare_retrieval("What is F1 interface?", top_k=3)
```

---

## 质量问题修复总结

| 问题类型 | 原始发生率 | 修复方案 | 状态 |
|---------|-----------|---------|------|
| 元认知泄漏 | 38.1% | Prompt 重构 + 验证 + 清洗 | ✅ |
| 文档结构问题 | - | 问题过滤 + 后处理检测 | ✅ |
| 负面样本污染 | - | 拒绝模式检测 | ✅ |
| 首字母缩写幻觉 | 69% | 实体一致性检查 | ✅ |
| 代码解释浅显 | 76.4% | 深度提示词 + RAG 增强 | ✅ |
| RAG 检索不精确 | - | Cross-Encoder Reranker | ✅ |

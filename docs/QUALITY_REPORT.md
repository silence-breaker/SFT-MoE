# RANSTRUCT 数据集质量分析报告

## 📊 问题汇总

基于对 55,063 条问答对的深度分析，发现以下质量问题：

| 问题类型 | 影响数量 | 占比 | 严重程度 | 可修复性 |
|---------|---------|------|---------|---------|
| **元认知泄漏** | 20,953 | 38.1% | 🔴 高 | ✅ 可修复 |
| **缩写幻觉** | ~4,044 | 69% of acronym Q | 🔴 高 | ⚠️ 部分可修复 |
| **代码浅层解释** | ~4,781 | 76.4% of code Q | 🟡 中 | ❌ 难修复 |
| **同义反复** | 2 | <0.01% | 🔴 高 | ❌ 应丢弃 |

---

## 🔴 问题一：元认知泄漏 (Meta-Cognitive Leakage)

### 问题描述
答案中包含对"上下文"、"文档"的直接引用，暴露了RAG管道的存在。这是**最普遍也最容易修复**的问题。

### 典型案例
```
❌ "[Document 1]: The O-RU handles the lower PHY functions..."
❌ "Based on the provided context, PT-RS is used for..."
❌ "According to the documents, the scheduler manages..."
```

### 问题模式分布
| 模式类型 | 数量 |
|---------|------|
| `[Document N]` 引用 | 8,248 |
| `Based on the provided...` | 4,371 |
| `In the context...` | 4,111 |
| `According to...` | 94 |

### 修复方案
**已在 `post_processor.py` 中实现正则替换：**
```python
META_COGNITIVE_PATTERNS = [
    (r'\[Document \d+\]:?\s*', ''),
    (r'Based on the (provided |given )?(context|documents?)[,\s]*', ''),
    # ... 更多模式
]
```

### 根因分析
Answer Generator 的 System Prompt 没有明确禁止引用上下文：
```python
# 当前 prompt (有问题)
"Answer based on the following context documents..."

# 优化后的 prompt
"You are an O-RAN expert. Answer directly without referencing any documents or context. Never use phrases like 'According to the context' or '[Document N]'."
```

---

## 🔴 问题二：缩写猜谜型幻觉 (Acronym Hallucination)

### 问题描述
Qwen2.5:1.5b 对 O-RAN 专业缩写不熟悉，经常给出错误或模糊的解释。

### 典型案例
```
Q: What does PT-RS stand for in the context of 5G NR?
A: ❌ "PT-RS is a type of reference signal used in the physical layer..."
   (正确答案应明确指出: Phase Tracking Reference Signal)

Q: What is O-RU?
A: ❌ "The O-RU is a component in the O-RAN architecture that handles radio functions..."
   (正确答案应包含: O-RAN Radio Unit)
```

### 统计数据
- 缩写定义类问题: 5,864 条
- 包含正确展开: 1,820 (31%)
- **可能存在幻觉: 4,044 (69%)**

### 修复方案

#### 方案A: 后处理注入 (已实现)
```python
ORAN_ACRONYM_GLOSSARY = {
    "PT-RS": "Phase Tracking Reference Signal",
    "O-RU": "O-RAN Radio Unit",
    "RIC": "RAN Intelligent Controller",
    # ... 100+ 术语
}

# 对检测到幻觉的答案，在开头注入正确定义
fixed = f"{acronym} stands for {expansion}. " + original_answer
```

#### 方案B: RAG增强 (推荐长期方案)
1. 创建 `oran_glossary.json` 术语表
2. 在 `_retrieve()` 时，对缩写问题优先检索术语表
3. 将术语定义作为第一个 context document

#### 方案C: 模型升级
考虑使用更大的模型 (如 `qwen2.5:7b`) 来回答术语解释类问题。

---

## 🟡 问题三：代码废话文学 (Shallow Code Explanation)

### 问题描述
对代码的解释停留在语法层面，缺乏对设计意图、架构决策、性能考量的深入分析。

### 典型案例
```
Q: Why does the function return ofdm_symbol_range instead of a single number?

❌ 浅层回答:
"The function returns ofdm_symbol_range because it is designed to return a range. 
The return type is ofdm_symbol_range because the function needs to specify multiple symbols."

✅ 理想回答:
"Returning ofdm_symbol_range instead of a single number is a design decision that enables:
1. **Flexible slot configuration**: TDD patterns can have variable DL/UL symbol boundaries
2. **Zero-copy iteration**: Callers can iterate over symbols without allocation
3. **Boundary checking**: The range type encapsulates start/end validation
4. **API consistency**: Aligns with other PHY timing APIs that use ranges"
```

### 统计数据
- 代码类问答: 6,256 条
- 缺乏设计意图: 4,781 (76.4%)
- 含浅层解释模式: 2,141 (34.2%)

### 修复方案

#### 优化 Question Generator Prompt
```python
CODE_QUESTION_PROMPT = """
Generate questions that probe deeper understanding:
- Why was this design pattern chosen over alternatives?
- What are the performance implications?
- How does this fit into the larger architecture?
- What trade-offs were considered?

AVOID questions like:
- "What does this function return?"
- "What parameters does this function take?"
"""
```

#### 优化 Answer Generator Prompt
```python
CODE_ANSWER_PROMPT = """
When explaining code:
1. Start with the design rationale (WHY)
2. Explain architectural context (WHERE it fits)
3. Discuss trade-offs and alternatives
4. Only then explain implementation details (HOW)

Never give superficial explanations like "The function returns X because it's designed to return X".
"""
```

#### 增加代码上下文
当前 `CodeSplitter` 可能将代码切得太碎，丢失了类/模块级别的上下文。建议：
- 增加 `chunk_size` 到 3000-4000
- 保留完整函数/类定义
- 在 chunk 中包含相关注释和文档字符串

---

## 🛠️ 修复工具使用指南

### 1. 分析现有数据集
```bash
cd /home/silence_breaker/git/SFT-MoE

# 仅分析，查看问题分布
python ranstruct/post_processor.py \
    --input "output/ranstruct_dataset_*.jsonl" \
    --analyze-only
```

### 2. 清洗数据集 (宽松模式)
```bash
# 尝试修复可修复的问题，保留尽可能多的数据
python ranstruct/post_processor.py \
    --input "output/ranstruct_dataset_*.jsonl" \
    --output output/ranstruct_cleaned.jsonl
```

### 3. 清洗数据集 (严格模式)
```bash
# 丢弃所有有问题的数据，只保留干净数据
python ranstruct/post_processor.py \
    --input "output/ranstruct_dataset_*.jsonl" \
    --output output/ranstruct_strict.jsonl \
    --strict
```

### 4. 预估清洗后数据量

| 模式 | 预计保留 | 说明 |
|-----|---------|------|
| 宽松模式 | ~52,000 (94%) | 修复元认知泄漏，丢弃严重幻觉 |
| 严格模式 | ~30,000 (55%) | 只保留完全干净的数据 |

---

## 📋 长期优化建议

### Phase 1: 数据清洗 (立即可做)
- [x] 运行 `post_processor.py` 清洗现有数据
- [ ] 检查清洗后数据的质量抽样

### Phase 2: Prompt 优化 (中期)
- [ ] 重写 `ANSWER_SYSTEM_PROMPT`，明确禁止元认知表达
- [ ] 为代码问题使用专门的深度分析 prompt
- [ ] 为术语问题注入词典作为首要上下文

### Phase 3: 架构优化 (长期)
- [ ] 实现问题类型分类器，对不同类型使用不同生成策略
- [ ] 考虑对术语类问题使用更大模型
- [ ] 实现 self-consistency 验证，对低置信度答案重新生成

---

## 📁 新增文件

| 文件 | 用途 |
|-----|------|
| `ranstruct/post_processor.py` | 数据集后处理与清洗工具 |
| `ranstruct/quality_improvements.py` | 质量检测辅助函数 |
| `ranstruct/config_optimizations.py` | 优化后的配置和 prompt |
| `docs/QUALITY_REPORT.md` | 本文档 |

---

*生成时间: 基于 55,063 条问答对的分析*

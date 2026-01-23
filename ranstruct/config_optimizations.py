"""
RANSTRUCT 配置优化补丁

本文件包含建议的配置和代码优化，供未来版本使用。
不会自动应用，需要手动集成。

优化目标：
1. 减少术语解释幻觉
2. 改善 RAG chunk 切分质量
3. 提高数据集整体质量
"""

# ===================== 优化后的配置 =====================

OPTIMIZED_CHUNK_CONFIG = {
    # RAG Chunks - 增加最小长度限制
    "rag_chunk_size": 1024,
    "rag_chunk_overlap": 200,  # 增加重叠以保持上下文连贯
    "rag_min_chunk_size": 200,  # 新增：最小 chunk 大小
    
    # LTG Chunks
    "ltg_chunk_size": 4096,
    "ltg_chunk_overlap": 512,  # 增加重叠
    
    # 代码专用配置
    "code_chunk_size": 2048,  # 代码文件使用更大的 chunk
    "code_preserve_functions": True,  # 尽量保持函数完整性
    
    # 分隔符优先级调整
    "separators": [
        "\n\n\n",  # 三空行（章节分隔）
        "\n\n",     # 双空行（段落）
        "\n## ",    # Markdown 二级标题
        "\n### ",   # Markdown 三级标题
        "\n",       # 单行
        ". ",       # 句子
        " ",        # 词
        ""          # 字符
    ],
    
    # 代码分隔符
    "code_separators": [
        "\n\n",            # 空行（函数间）
        "\nclass ",        # 类定义
        "\ndef ",          # Python 函数
        "\nvoid ",         # C/C++ void 函数
        "\nint ",          # C/C++ int 函数
        "\nstatic ",       # 静态函数
        "\n{",             # 代码块开始
        "\n",              # 单行
    ]
}


# ===================== 改进的 System Prompt =====================

IMPROVED_SYSTEM_PROMPT_V2 = """You are a precise O-RAN technical documentation assistant.

ABSOLUTE RULES - NEVER VIOLATE:
1. Use ONLY information explicitly written in the provided context
2. NEVER use: "probably", "might", "could be", "I think", "it seems", "possibly", "likely"
3. NEVER speculate or make assumptions beyond the context
4. If information is missing, say: "This information is not provided in the context."

RESPONSE FORMAT:
- Be direct and factual
- Quote exact text when possible (use "..." for direct quotes)
- Include specific references (clause numbers, function names, etc.)
- Keep answers focused and avoid unnecessary elaboration

You are answering questions for AI training data. Accuracy is paramount."""


# ===================== 改进的验证规则 =====================

ENHANCED_INVALID_PATTERNS = [
    # 原有模式
    "i don't know",
    "i cannot",
    "i'm not sure",
    "insufficient information",
    "no relevant",
    "i'm unable to",
    "cannot provide",
    "not enough information",
    "context does not contain",
    "context doesn't contain",
    
    # 新增：不确定性表述
    "i believe",
    "i think",
    "probably",
    "might be",
    "could be",
    "possibly",
    "presumably",
    "it seems",
    "appears to be",
    "i assume",
    "we would need to",
    "additional.*would be needed",
    
    # 新增：推测性表述
    "this might mean",
    "this could indicate",
    "this may suggest",
    "it is possible that",
]


# ===================== 改进的代码分块器 =====================

class ImprovedCodeSplitter:
    """改进的代码分块器 - 保持函数/类完整性"""
    
    FUNCTION_PATTERNS = [
        r'^(void|int|bool|auto|static|virtual|inline)\s+\w+\s*\([^)]*\)\s*\{?',  # C/C++ 函数
        r'^class\s+\w+',  # C++ 类
        r'^struct\s+\w+',  # C++ 结构体
        r'^template\s*<',  # C++ 模板
        r'^namespace\s+\w+',  # C++ 命名空间
    ]
    
    def __init__(self, max_chunk_size: int = 2048, min_chunk_size: int = 200):
        self.max_chunk_size = max_chunk_size
        self.min_chunk_size = min_chunk_size
    
    def split_code(self, code: str) -> list:
        """智能分割代码，尽量保持函数完整"""
        import re
        
        lines = code.split('\n')
        chunks = []
        current_chunk = []
        current_size = 0
        brace_count = 0
        in_function = False
        
        for line in lines:
            line_size = len(line) + 1  # +1 for newline
            
            # 检测函数/类开始
            for pattern in self.FUNCTION_PATTERNS:
                if re.match(pattern, line.strip()):
                    # 如果当前 chunk 不为空且不在函数内，先保存
                    if current_chunk and not in_function and current_size >= self.min_chunk_size:
                        chunks.append('\n'.join(current_chunk))
                        current_chunk = []
                        current_size = 0
                    in_function = True
                    break
            
            # 跟踪花括号
            brace_count += line.count('{') - line.count('}')
            
            # 检测函数/类结束
            if in_function and brace_count <= 0:
                current_chunk.append(line)
                current_size += line_size
                
                # 函数结束，保存 chunk
                if current_size >= self.min_chunk_size:
                    chunks.append('\n'.join(current_chunk))
                    current_chunk = []
                    current_size = 0
                
                in_function = False
                brace_count = 0
                continue
            
            # 添加到当前 chunk
            current_chunk.append(line)
            current_size += line_size
            
            # 如果超过最大大小且不在函数内，强制分割
            if current_size >= self.max_chunk_size and not in_function:
                chunks.append('\n'.join(current_chunk))
                current_chunk = []
                current_size = 0
        
        # 保存剩余内容
        if current_chunk:
            chunks.append('\n'.join(current_chunk))
        
        return chunks


# ===================== 低价值内容过滤器 =====================

LOW_VALUE_CONTENT_PATTERNS = [
    r'copyright.*all rights reserved',
    r'register of associations',
    r'vat id\s*:?\s*\w+',
    r'the copying or incorporation',
    r'prior written permission',
    r'o-ran alliance e\.v\.',
    r'buschkauler weg',  # O-RAN 总部地址
    r'bonn vr \d+',  # 注册号
]

def is_low_value_content(text: str) -> bool:
    """检查是否是低价值内容（版权声明、法律文本等）"""
    import re
    text_lower = text.lower()
    
    # 计算匹配的模式数
    matches = sum(1 for p in LOW_VALUE_CONTENT_PATTERNS if re.search(p, text_lower))
    
    # 如果匹配多个模式，认为是低价值内容
    return matches >= 2


# ===================== 使用说明 =====================
"""
如何应用这些优化：

1. 数据集后处理过滤：
   python ranstruct/quality_improvements.py filter input.jsonl output_filtered.jsonl

2. 分析现有数据质量：
   python ranstruct/quality_improvements.py analyze input.jsonl --sample 500

3. 在新生成数据时使用改进的 prompt：  ✅ 已完成
   - 将 IMPROVED_SYSTEM_PROMPT_V2 替换 answer_generator.py 中的 SYSTEM_PROMPT
   - 将 ENHANCED_INVALID_PATTERNS 合并到 _validate_answer 方法

4. 改进代码分块（需要重建索引，谨慎操作）：  ✅ 已完成
   - 使用 ImprovedCodeSplitter 替换现有的代码分块逻辑  ✅
   - 增加 rag_min_chunk_size 配置防止过短 chunk  ✅
   - 添加低价值内容过滤 (is_low_value_content)  ✅

5. 优化配置已集成到 config.py:  ✅ 已完成
   - rag_chunk_overlap: 128 -> 200
   - ltg_chunk_overlap: 256 -> 512
   - rag_min_chunk_size: 200 (新增)
   - code_chunk_size: 2048 (新增)
   - code_preserve_functions: True (新增)
   - filter_low_value_content: True (新增)
   - separators: 优化优先级 (新增 Markdown 标题分隔符)
   - code_separators: 新增代码专用分隔符

注意：以上优化不会自动应用到已有索引，需要重建索引才能生效。
重建索引是破坏性操作，请先备份现有数据。
"""

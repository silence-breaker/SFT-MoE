"""
RANSTRUCT 数据处理模块

实现数据加载和递归分块功能：
- 加载 O-RAN 规范文档
- 加载 srsRAN 代码文件
- 递归文本分割器
- 生成 RAG Chunks 和 LTG Chunks
"""

import re
import hashlib
from pathlib import Path
from typing import List, Dict, Optional, Generator, Tuple, Any
from dataclasses import dataclass, field
import logging

from .config import Config, ChunkConfig, DataSourceConfig

logger = logging.getLogger(__name__)


@dataclass
class Document:
    """文档数据类"""
    content: str
    metadata: Dict[str, Any] = field(default_factory=dict)
    doc_id: str = ""
    
    def __post_init__(self):
        if not self.doc_id:
            self.doc_id = hashlib.md5(self.content[:500].encode()).hexdigest()[:12]


@dataclass
class Chunk:
    """文本块数据类"""
    content: str
    chunk_type: str  # "rag" or "ltg"
    source_doc_id: str
    chunk_index: int
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    @property
    def chunk_id(self) -> str:
        """生成唯一的 chunk ID"""
        return f"{self.source_doc_id}_{self.chunk_type}_{self.chunk_index}"
    
    @property
    def token_count(self) -> int:
        """估算 token 数量（粗略估计）"""
        # 英文约 4 字符 = 1 token，中文约 1.5 字符 = 1 token
        cn_chars = len(re.findall(r'[\u4e00-\u9fff]', self.content))
        en_chars = len(self.content) - cn_chars
        return int(cn_chars / 1.5 + en_chars / 4)


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
    text_lower = text.lower()
    
    # 计算匹配的模式数
    matches = sum(1 for p in LOW_VALUE_CONTENT_PATTERNS if re.search(p, text_lower))
    
    # 如果匹配多个模式，认为是低价值内容
    return matches >= 2


# ===================== 改进的代码分块器 =====================

class ImprovedCodeSplitter:
    """改进的代码分块器 - 保持函数/类完整性"""
    
    FUNCTION_PATTERNS = [
        r'^(void|int|bool|auto|static|virtual|inline|unsigned|const)\s+\w+\s*\([^)]*\)\s*\{?',  # C/C++ 函数
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
            chunk_text = '\n'.join(current_chunk)
            if len(chunk_text) >= self.min_chunk_size:
                chunks.append(chunk_text)
            elif chunks:  # 合并到上一个 chunk
                chunks[-1] = chunks[-1] + '\n' + chunk_text
            else:
                chunks.append(chunk_text)
        
        return chunks


class RecursiveSplitter:
    """递归文本分割器
    
    将文档按层级分隔符递归分割，确保每个块不超过指定大小。
    """
    
    def __init__(
        self,
        chunk_size: int = 1024,
        chunk_overlap: int = 128,
        separators: Optional[List[str]] = None,
        length_function: Optional[callable] = None
    ):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.separators = separators or ["\n\n", "\n", "。", ".", " ", ""]
        self.length_function = length_function or len
    
    def split_text(self, text: str) -> List[str]:
        """分割文本为多个块"""
        return self._split_recursive(text, self.separators)
    
    def _split_recursive(self, text: str, separators: List[str]) -> List[str]:
        """递归分割"""
        final_chunks = []
        
        # 找到合适的分隔符
        separator = separators[-1]  # 默认使用最后一个（空字符串）
        new_separators = []
        
        for i, sep in enumerate(separators):
            if sep == "":
                separator = sep
                break
            if sep in text:
                separator = sep
                new_separators = separators[i + 1:]
                break
        
        # 按分隔符分割
        if separator:
            splits = text.split(separator)
        else:
            splits = list(text)
        
        # 合并小块
        good_splits = []
        current_chunk = []
        current_length = 0
        
        for split in splits:
            split_length = self.length_function(split)
            
            if current_length + split_length + len(separator) <= self.chunk_size:
                current_chunk.append(split)
                current_length += split_length + len(separator)
            else:
                if current_chunk:
                    merged = separator.join(current_chunk)
                    if merged.strip():
                        good_splits.append(merged)
                
                # 如果单个分割仍然太大，递归分割
                if split_length > self.chunk_size and new_separators:
                    sub_chunks = self._split_recursive(split, new_separators)
                    good_splits.extend(sub_chunks)
                    current_chunk = []
                    current_length = 0
                else:
                    current_chunk = [split]
                    current_length = split_length
        
        # 处理剩余内容
        if current_chunk:
            merged = separator.join(current_chunk)
            if merged.strip():
                good_splits.append(merged)
        
        # 添加重叠
        final_chunks = self._add_overlap(good_splits, separator)
        
        return final_chunks
    
    def _add_overlap(self, chunks: List[str], separator: str) -> List[str]:
        """添加块间重叠"""
        if not chunks or self.chunk_overlap == 0:
            return chunks
        
        result = []
        for i, chunk in enumerate(chunks):
            if i == 0:
                result.append(chunk)
            else:
                # 从前一个块末尾取重叠内容
                prev_chunk = chunks[i - 1]
                overlap_text = self._get_overlap_text(prev_chunk, separator)
                new_chunk = overlap_text + separator + chunk if overlap_text else chunk
                
                # 确保不超过最大大小
                if self.length_function(new_chunk) > self.chunk_size * 1.2:
                    result.append(chunk)
                else:
                    result.append(new_chunk)
        
        return result
    
    def _get_overlap_text(self, text: str, separator: str) -> str:
        """获取重叠文本"""
        if self.length_function(text) <= self.chunk_overlap:
            return text
        
        # 尝试在分隔符处截断
        parts = text.split(separator)
        overlap_parts = []
        current_length = 0
        
        for part in reversed(parts):
            part_length = self.length_function(part)
            if current_length + part_length <= self.chunk_overlap:
                overlap_parts.insert(0, part)
                current_length += part_length
            else:
                break
        
        return separator.join(overlap_parts) if overlap_parts else text[-self.chunk_overlap:]


class DataProcessor:
    """数据处理器
    
    负责加载和处理 O-RAN 规范文档与 srsRAN 代码文件。
    """
    
    def __init__(self, config: Config):
        self.config = config
        self.chunk_config = config.chunk
        self.data_source_config = config.data_source
        
        # 创建分割器
        self.rag_splitter = RecursiveSplitter(
            chunk_size=self.chunk_config.rag_chunk_size,
            chunk_overlap=self.chunk_config.rag_chunk_overlap,
            separators=self.chunk_config.separators
        )
        
        self.ltg_splitter = RecursiveSplitter(
            chunk_size=self.chunk_config.ltg_chunk_size,
            chunk_overlap=self.chunk_config.ltg_chunk_overlap,
            separators=self.chunk_config.separators
        )
        
        # 代码专用分割器 (保持函数完整性)
        self.code_splitter = ImprovedCodeSplitter(
            max_chunk_size=self.chunk_config.code_chunk_size,
            min_chunk_size=self.chunk_config.rag_min_chunk_size
        )
    
    def load_oran_specifications(self) -> List[Document]:
        """加载 O-RAN 规范文档"""
        documents = []
        spec_path = self.data_source_config.oran_spec_path
        
        if not spec_path or not spec_path.exists():
            logger.warning(f"O-RAN 规范路径不存在: {spec_path}")
            return documents
        
        logger.info(f"正在从 {spec_path} 加载 O-RAN 规范文档...")
        
        for ext in self.data_source_config.spec_extensions:
            for file_path in spec_path.glob(f"**/*{ext}"):
                # 跳过 Zone.Identifier 文件
                if "Zone.Identifier" in str(file_path):
                    continue
                    
                try:
                    content = self._read_file(file_path)
                    if content:
                        doc = Document(
                            content=content,
                            metadata={
                                "source": str(file_path),
                                "filename": file_path.name,
                                "type": "oran_specification",
                                "extension": ext
                            }
                        )
                        documents.append(doc)
                        logger.debug(f"已加载: {file_path.name}")
                except Exception as e:
                    logger.error(f"加载文件失败 {file_path}: {e}")
        
        logger.info(f"已加载 {len(documents)} 个 O-RAN 规范文档")
        return documents
    
    def load_srsran_code(self) -> List[Document]:
        """加载 srsRAN 代码文件"""
        documents = []
        code_path = self.data_source_config.srsran_code_path
        
        if not code_path or not code_path.exists():
            logger.warning(f"srsRAN 代码路径不存在: {code_path}")
            return documents
        
        logger.info(f"正在从 {code_path} 加载 srsRAN 代码文件...")
        
        for ext in self.data_source_config.code_extensions:
            for file_path in code_path.glob(f"**/*{ext}"):
                # 跳过测试和外部依赖
                relative_path = str(file_path.relative_to(code_path))
                if any(skip in relative_path for skip in ['test', 'external', 'build', '.git']):
                    continue
                    
                try:
                    content = self._read_file(file_path)
                    if content:
                        doc = Document(
                            content=content,
                            metadata={
                                "source": str(file_path),
                                "filename": file_path.name,
                                "type": "srsran_code",
                                "extension": ext,
                                "relative_path": relative_path
                            }
                        )
                        documents.append(doc)
                        logger.debug(f"已加载: {file_path.name}")
                except Exception as e:
                    logger.error(f"加载文件失败 {file_path}: {e}")
        
        logger.info(f"已加载 {len(documents)} 个 srsRAN 代码文件")
        return documents
    
    def load_codeset(self) -> List[Document]:
        """加载代码集文件"""
        documents = []
        codeset_path = self.data_source_config.codeset_path
        
        if not codeset_path or not codeset_path.exists():
            logger.warning(f"代码集路径不存在: {codeset_path}")
            return documents
        
        logger.info(f"正在从 {codeset_path} 加载代码集...")
        
        for ext in self.data_source_config.code_extensions:
            for file_path in codeset_path.glob(f"**/*{ext}"):
                # 跳过 Zone.Identifier 文件
                if "Zone.Identifier" in str(file_path):
                    continue
                    
                try:
                    content = self._read_file(file_path)
                    if content:
                        # 提取模块名
                        relative_path = file_path.relative_to(codeset_path)
                        module_name = relative_path.parts[0] if relative_path.parts else "unknown"
                        
                        doc = Document(
                            content=content,
                            metadata={
                                "source": str(file_path),
                                "filename": file_path.name,
                                "type": "codeset",
                                "module": module_name,
                                "extension": ext
                            }
                        )
                        documents.append(doc)
                        logger.debug(f"已加载: {file_path.name} (模块: {module_name})")
                except Exception as e:
                    logger.error(f"加载文件失败 {file_path}: {e}")
        
        logger.info(f"已加载 {len(documents)} 个代码集文件")
        return documents
    
    def _read_file(self, file_path: Path) -> Optional[str]:
        """读取文件内容"""
        encodings = ['utf-8', 'utf-8-sig', 'latin-1', 'gbk']
        
        for encoding in encodings:
            try:
                with open(file_path, 'r', encoding=encoding) as f:
                    return f.read()
            except UnicodeDecodeError:
                continue
        
        logger.warning(f"无法解码文件: {file_path}")
        return None
    
    def create_rag_chunks(self, documents: List[Document]) -> List[Chunk]:
        """为文档创建 RAG Chunks (1024 tokens)
        
        优化:
        - 过滤低价值内容（版权声明等）
        - 过滤过短的 chunk
        - 代码文件使用专用分割器
        """
        chunks = []
        filtered_low_value = 0
        filtered_too_short = 0
        
        min_size = self.chunk_config.rag_min_chunk_size
        filter_low_value = self.chunk_config.filter_low_value_content
        
        for doc in documents:
            doc_type = doc.metadata.get("type", "")
            
            # 代码文件使用专用分割器
            if doc_type in ["srsran_code", "codeset"] and self.chunk_config.code_preserve_functions:
                text_chunks = self.code_splitter.split_code(doc.content)
            else:
                text_chunks = self.rag_splitter.split_text(doc.content)
            
            for idx, text in enumerate(text_chunks):
                # 过滤低价值内容
                if filter_low_value and is_low_value_content(text):
                    filtered_low_value += 1
                    continue
                
                # 过滤过短的 chunk
                if len(text) < min_size:
                    filtered_too_short += 1
                    continue
                
                chunk = Chunk(
                    content=text,
                    chunk_type="rag",
                    source_doc_id=doc.doc_id,
                    chunk_index=idx,
                    metadata={
                        **doc.metadata,
                        "chunk_size": len(text)
                    }
                )
                chunks.append(chunk)
        
        logger.info(f"已创建 {len(chunks)} 个 RAG Chunks (过滤: 低价值={filtered_low_value}, 过短={filtered_too_short})")
        return chunks
    
    def create_ltg_chunks(self, documents: List[Document]) -> List[Chunk]:
        """为文档创建 LTG Chunks (4096 tokens)"""
        chunks = []
        
        for doc in documents:
            # 对于代码文件，使用完整文件而不分块
            if doc.metadata.get("type") in ["srsran_code", "codeset"]:
                chunk = Chunk(
                    content=doc.content,
                    chunk_type="ltg",
                    source_doc_id=doc.doc_id,
                    chunk_index=0,
                    metadata={
                        **doc.metadata,
                        "chunk_size": len(doc.content),
                        "is_full_file": True
                    }
                )
                chunks.append(chunk)
            else:
                # 对于规范文档，分块处理
                text_chunks = self.ltg_splitter.split_text(doc.content)
                
                for idx, text in enumerate(text_chunks):
                    chunk = Chunk(
                        content=text,
                        chunk_type="ltg",
                        source_doc_id=doc.doc_id,
                        chunk_index=idx,
                        metadata={
                            **doc.metadata,
                            "chunk_size": len(text),
                            "is_full_file": False
                        }
                    )
                    chunks.append(chunk)
        
        logger.info(f"已创建 {len(chunks)} 个 LTG Chunks")
        return chunks
    
    def process_all(self) -> Tuple[List[Chunk], List[Chunk]]:
        """处理所有数据源，返回 (RAG Chunks, LTG Chunks)"""
        # 加载所有文档
        oran_docs = self.load_oran_specifications()
        srsran_docs = self.load_srsran_code()
        codeset_docs = self.load_codeset()
        
        all_documents = oran_docs + srsran_docs + codeset_docs
        
        logger.info(f"总共加载 {len(all_documents)} 个文档")
        
        # 创建 chunks
        rag_chunks = self.create_rag_chunks(all_documents)
        ltg_chunks = self.create_ltg_chunks(all_documents)
        
        return rag_chunks, ltg_chunks
    
    def get_statistics(self, documents: List[Document]) -> Dict:
        """获取数据统计信息"""
        stats = {
            "total_documents": len(documents),
            "total_characters": sum(len(doc.content) for doc in documents),
            "by_type": {}
        }
        
        for doc in documents:
            doc_type = doc.metadata.get("type", "unknown")
            if doc_type not in stats["by_type"]:
                stats["by_type"][doc_type] = {
                    "count": 0,
                    "characters": 0
                }
            stats["by_type"][doc_type]["count"] += 1
            stats["by_type"][doc_type]["characters"] += len(doc.content)
        
        # 估算词数（英文约5字符/词，中文约1.5字符/词）
        stats["estimated_words"] = int(stats["total_characters"] / 4)
        
        return stats


if __name__ == "__main__":
    # 测试数据处理器
    logging.basicConfig(level=logging.INFO)
    
    config = Config()
    processor = DataProcessor(config)
    
    # 测试加载
    oran_docs = processor.load_oran_specifications()
    
    if oran_docs:
        print(f"\n加载了 {len(oran_docs)} 个 O-RAN 文档")
        
        # 测试分块
        rag_chunks = processor.create_rag_chunks(oran_docs[:3])
        ltg_chunks = processor.create_ltg_chunks(oran_docs[:3])
        
        print(f"RAG Chunks: {len(rag_chunks)}")
        print(f"LTG Chunks: {len(ltg_chunks)}")
        
        if rag_chunks:
            print(f"\n第一个 RAG Chunk 示例:")
            print(f"  ID: {rag_chunks[0].chunk_id}")
            print(f"  长度: {len(rag_chunks[0].content)} 字符")
            print(f"  内容预览: {rag_chunks[0].content[:200]}...")

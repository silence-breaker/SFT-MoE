"""
RANSTRUCT - O-RAN 领域数据集生成框架

基于RAG（检索增强生成）原理，使用两个LLM代理生成问答数据集：
- Mistral-7B-Instruct-0.3: 问题生成
- Qwen-2.5-Instruct-1.5B: 答案生成

主要模块：
- config: 配置管理
- data_processor: 数据处理与分块
- faiss_manager: FAISS向量数据库管理
- question_generator: 问题生成
- answer_generator: 答案生成
- pipeline: 完整流程管道
"""

__version__ = "1.0.0"
__author__ = "RANSTRUCT Team"

from .config import Config
from .pipeline import RANSTRUCTPipeline

__all__ = ["Config", "RANSTRUCTPipeline"]

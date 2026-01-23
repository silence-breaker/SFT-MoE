"""
RANSTRUCT 工具函数模块

提供通用工具函数：
- 文本处理
- 进度显示
- 文件操作
"""

import os
import re
import time
import hashlib
from pathlib import Path
from typing import List, Dict, Optional, Any, Iterator, Callable
from functools import wraps
import logging

logger = logging.getLogger(__name__)


def timer(func: Callable) -> Callable:
    """计时装饰器"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        logger.debug(f"{func.__name__} 耗时: {elapsed:.2f}秒")
        return result
    return wrapper


def retry(max_retries: int = 3, delay: float = 1.0):
    """重试装饰器"""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt < max_retries - 1:
                        time.sleep(delay * (attempt + 1))
                        logger.warning(f"{func.__name__} 失败，第 {attempt + 2} 次重试...")
            raise last_exception
        return wrapper
    return decorator


def generate_hash(text: str, length: int = 12) -> str:
    """生成文本的哈希值"""
    return hashlib.md5(text.encode()).hexdigest()[:length]


def clean_text(text: str) -> str:
    """清洗文本"""
    # 移除多余空白
    text = re.sub(r'\s+', ' ', text)
    # 移除特殊字符
    text = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\x9f]', '', text)
    return text.strip()


def truncate_text(text: str, max_length: int, suffix: str = "...") -> str:
    """截断文本"""
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix


def count_tokens_estimate(text: str) -> int:
    """
    估算 token 数量
    
    英文约 4 字符 = 1 token
    中文约 1.5 字符 = 1 token
    """
    cn_chars = len(re.findall(r'[\u4e00-\u9fff]', text))
    other_chars = len(text) - cn_chars
    return int(cn_chars / 1.5 + other_chars / 4)


def batch_iterator(items: List[Any], batch_size: int) -> Iterator[List[Any]]:
    """批次迭代器"""
    for i in range(0, len(items), batch_size):
        yield items[i:i + batch_size]


def ensure_dir(path: Path) -> Path:
    """确保目录存在"""
    path = Path(path)
    path.mkdir(parents=True, exist_ok=True)
    return path


def find_files(
    directory: Path, 
    extensions: List[str],
    exclude_patterns: Optional[List[str]] = None
) -> List[Path]:
    """
    查找目录下指定扩展名的文件
    
    Args:
        directory: 目录路径
        extensions: 扩展名列表
        exclude_patterns: 排除的路径模式
        
    Returns:
        文件路径列表
    """
    files = []
    exclude_patterns = exclude_patterns or []
    
    for ext in extensions:
        for file_path in directory.glob(f"**/*{ext}"):
            # 检查排除模式
            relative_path = str(file_path.relative_to(directory))
            if any(pattern in relative_path for pattern in exclude_patterns):
                continue
            # 跳过 Zone.Identifier 文件
            if "Zone.Identifier" in str(file_path):
                continue
            files.append(file_path)
    
    return sorted(files)


def format_size(size_bytes: int) -> str:
    """格式化文件大小"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.2f} TB"


def format_time(seconds: float) -> str:
    """格式化时间"""
    if seconds < 60:
        return f"{seconds:.1f}秒"
    elif seconds < 3600:
        minutes = int(seconds // 60)
        secs = seconds % 60
        return f"{minutes}分{secs:.0f}秒"
    else:
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        return f"{hours}时{minutes}分"


class ProgressTracker:
    """进度追踪器"""
    
    def __init__(self, total: int, description: str = "Processing"):
        self.total = total
        self.current = 0
        self.description = description
        self.start_time = time.time()
        self._last_print = 0
    
    def update(self, n: int = 1):
        """更新进度"""
        self.current += n
        
        # 每秒最多打印一次
        now = time.time()
        if now - self._last_print >= 1.0 or self.current >= self.total:
            self._print_progress()
            self._last_print = now
    
    def _print_progress(self):
        """打印进度"""
        percentage = self.current / self.total * 100
        elapsed = time.time() - self.start_time
        
        if self.current > 0:
            eta = elapsed / self.current * (self.total - self.current)
            eta_str = format_time(eta)
        else:
            eta_str = "计算中..."
        
        logger.info(
            f"{self.description}: {self.current}/{self.total} "
            f"({percentage:.1f}%) - ETA: {eta_str}"
        )
    
    def finish(self):
        """完成"""
        elapsed = time.time() - self.start_time
        logger.info(f"{self.description} 完成，耗时: {format_time(elapsed)}")


def extract_code_blocks(text: str) -> List[Dict[str, str]]:
    """
    从 markdown 文本中提取代码块
    
    Returns:
        [{"language": "python", "code": "..."}]
    """
    pattern = r'```(\w*)\n([\s\S]*?)```'
    matches = re.findall(pattern, text)
    
    return [
        {"language": lang or "text", "code": code.strip()}
        for lang, code in matches
    ]


def merge_dicts(base: Dict, override: Dict) -> Dict:
    """递归合并字典"""
    result = base.copy()
    
    for key, value in override.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = merge_dicts(result[key], value)
        else:
            result[key] = value
    
    return result


def sanitize_filename(filename: str) -> str:
    """清理文件名"""
    # 移除或替换不安全字符
    filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
    # 限制长度
    if len(filename) > 200:
        name, ext = os.path.splitext(filename)
        filename = name[:200-len(ext)] + ext
    return filename


if __name__ == "__main__":
    # 测试工具函数
    print(f"Token 估算 (Hello World): {count_tokens_estimate('Hello World')}")
    print(f"Token 估算 (你好世界): {count_tokens_estimate('你好世界')}")
    print(f"格式化大小: {format_size(1234567890)}")
    print(f"格式化时间: {format_time(3723.5)}")
    print(f"哈希值: {generate_hash('test content')}")

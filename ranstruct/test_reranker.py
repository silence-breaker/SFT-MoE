#!/usr/bin/env python3
"""
Cross-Encoder Reranker 测试脚本

用于验证 Reranker 功能是否正常工作，并比较 FAISS-only 和 Reranked 检索结果
"""

import logging
import sys
from pathlib import Path

# 添加父目录到路径，支持直接运行脚本
sys.path.insert(0, str(Path(__file__).parent.parent))

# 设置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def test_reranker():
    """测试 Reranker 功能"""
    from ranstruct.config import Config
    from ranstruct.faiss_manager import FAISSManager, RAGRetriever, CrossEncoderReranker
    
    print("\n" + "=" * 70)
    print("Cross-Encoder Reranker 测试")
    print("=" * 70)
    
    # 使用更小的模型进行测试（下载更快）
    # 可选: "BAAI/bge-reranker-base" (1.11GB) 或 "cross-encoder/ms-marco-MiniLM-L-6-v2" (23MB)
    TEST_MODEL = "cross-encoder/ms-marco-MiniLM-L-6-v2"
    
    # 1. 测试 CrossEncoderReranker 单独功能
    print(f"\n[1] 测试 CrossEncoderReranker 加载 ({TEST_MODEL})...")
    try:
        reranker = CrossEncoderReranker(TEST_MODEL)
        print("   ✓ Reranker 模型加载成功")
        
        # 测试单次评分
        score = reranker.get_score(
            "What is F1 interface in O-RAN?",
            "The F1 interface connects CU and DU in O-RAN architecture."
        )
        print(f"   ✓ 单次评分测试: {score:.4f}")
        
        # 测试不相关文档评分
        score_irrelevant = reranker.get_score(
            "What is F1 interface in O-RAN?",
            "Python is a programming language used for web development."
        )
        print(f"   ✓ 不相关文档评分: {score_irrelevant:.4f}")
        
        if score > score_irrelevant:
            print("   ✓ 相关性区分正确 (相关 > 不相关)")
        else:
            print("   ✗ 相关性区分异常!")
            
    except Exception as e:
        print(f"   ✗ Reranker 加载失败: {e}")
        return False
    
    # 2. 测试与 FAISS 集成
    print("\n[2] 测试 FAISS + Reranker 集成...")
    try:
        config = Config()
        manager = FAISSManager(config)
        
        # 检查是否有现有索引
        index_path = config.data_source.faiss_index_path
        if index_path and (index_path / "index.faiss").exists():
            print(f"   发现现有索引: {index_path}")
            manager.load_index()
            print(f"   ✓ 索引加载成功 ({manager.index.ntotal} 向量)")
        else:
            print("   ✗ 未发现现有索引，需要先构建索引")
            return False
        
        # 创建 Retriever (启用 Reranker)
        retriever = RAGRetriever(
            manager,
            enable_reranker=True,
            reranker_model=TEST_MODEL
        )
        
        # 测试查询
        test_queries = [
            "What is F1 interface between CU and DU?",
            "How does O2ims interface work in O-RAN SMO?",
            "Explain the E1 interface for user plane",
            "What are the NGAP procedures?",
        ]
        
        print("\n[3] 比较检索结果...")
        for query in test_queries:
            print(f"\n   Query: {query}")
            
            # 比较结果
            comparison = retriever.compare_retrieval(query, top_k=3)
            
            print("   FAISS-only Top-3:")
            for i, r in enumerate(comparison["faiss_only"], 1):
                source = r["metadata"].get("filename", "Unknown")[:30]
                print(f"      {i}. [{r['score']:.4f}] {source}")
            
            print("   Reranked Top-3:")
            for i, r in enumerate(comparison["reranked"], 1):
                source = r["metadata"].get("filename", "Unknown")[:30]
                print(f"      {i}. [{r['score']:.4f}] {source}")
            
            if comparison["order_changed"]:
                print("   → 顺序改变: 是 (Reranker 起作用)")
            else:
                print("   → 顺序改变: 否")
        
    except Exception as e:
        print(f"   ✗ 集成测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    print("\n" + "=" * 70)
    print("测试完成!")
    print("=" * 70)
    return True


def test_entity_discrimination():
    """
    测试 Reranker 区分类似概念的能力
    
    这是一个关键测试，验证 Reranker 能否区分:
    - F1 vs E1 interface
    - O2ims vs O1 interface
    - NGAP vs PDCP protocol
    """
    from ranstruct.config import Config
    from ranstruct.faiss_manager import FAISSManager, RAGRetriever
    
    print("\n" + "=" * 70)
    print("实体区分能力测试 (Entity Discrimination)")
    print("=" * 70)
    
    config = Config()
    manager = FAISSManager(config)
    
    index_path = config.data_source.faiss_index_path
    if not (index_path and (index_path / "index.faiss").exists()):
        print("需要现有索引进行测试")
        return
    
    manager.load_index()
    
    # 创建两个 retriever: 一个有 reranker，一个没有
    retriever_with_reranker = RAGRetriever(
        manager,
        enable_reranker=True,
        reranker_model="BAAI/bge-reranker-base"
    )
    
    retriever_no_reranker = RAGRetriever(
        manager,
        enable_reranker=False
    )
    
    # 容易混淆的查询对
    confusing_pairs = [
        ("F1 interface", "E1 interface"),
        ("O2ims interface", "O1 interface"),
        ("NGAP protocol", "PDCP protocol"),
        ("CU-UP", "CU-CP"),
    ]
    
    print("\n测试容易混淆的概念对...")
    for concept_a, concept_b in confusing_pairs:
        print(f"\n--- {concept_a} vs {concept_b} ---")
        
        query_a = f"What is {concept_a}?"
        query_b = f"What is {concept_b}?"
        
        # 检索 concept_a
        results_faiss = retriever_no_reranker.retrieve(query_a, top_k=1)
        results_rerank = retriever_with_reranker.retrieve(query_a, top_k=1)
        
        if results_faiss and results_rerank:
            faiss_content = results_faiss[0]["content"][:100]
            rerank_content = results_rerank[0]["content"][:100]
            
            # 简单检查: 结果是否包含正确的关键词
            concept_key = concept_a.split()[0].upper()  # 如 "F1"
            
            faiss_correct = concept_key.lower() in faiss_content.lower()
            rerank_correct = concept_key.lower() in rerank_content.lower()
            
            print(f"  Query: {query_a}")
            print(f"  FAISS-only: {'✓' if faiss_correct else '✗'} (Score: {results_faiss[0]['score']:.4f})")
            print(f"  Reranked:   {'✓' if rerank_correct else '✗'} (Score: {results_rerank[0]['score']:.4f})")


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Cross-Encoder Reranker 测试")
    parser.add_argument("--full", action="store_true", help="运行完整测试包括实体区分测试")
    args = parser.parse_args()
    
    success = test_reranker()
    
    if args.full and success:
        test_entity_discrimination()

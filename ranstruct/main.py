#!/usr/bin/env python3
"""
RANSTRUCT - O-RAN 领域数据集生成框架

入口脚本，提供命令行接口运行数据集生成管道。

使用方式:
    # 运行完整管道
    python main.py run
    
    # 只运行特定步骤
    python main.py step1  # 数据加载
    python main.py step2  # FAISS 构建
    python main.py step3  # 问题生成
    python main.py step4  # 答案生成
    python main.py step5  # 保存数据集
    python main.py step6  # 质量后处理
    
    # 分析数据集质量
    python main.py analyze --input dataset.jsonl
    
    # 使用自定义配置
    python main.py run --config config.yaml
    
    # 测试模式（限制数量）
    python main.py run --test
    
    # 使用时间戳文件名（防止覆盖）
    python main.py run --timestamp
    
    # 禁用后处理 / 严格模式
    python main.py run --no-post-process
    python main.py run --strict
"""

import argparse
import logging
import sys
from pathlib import Path

# 添加项目路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from ranstruct.config import Config
from ranstruct.pipeline import RANSTRUCTPipeline, create_pipeline


def setup_logging(level: str = "INFO"):
    """设置日志"""
    logging.basicConfig(
        level=getattr(logging, level.upper(), logging.INFO),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),
        ]
    )


def cmd_run(args):
    """运行完整管道"""
    pipeline = create_pipeline(args.config)
    
    # 处理 --test 快捷方式
    max_chunks = args.max_chunks
    if args.test and max_chunks is None:
        max_chunks = 10
        print("[测试模式] 限制最大 chunks 数量为 10")
    
    # 处理 --timestamp 选项
    if args.timestamp:
        pipeline.config.output.use_timestamp_filename = True
        print("[时间戳模式] 输出文件将使用时间戳命名")
    
    results = pipeline.run(
        skip_data_loading=args.skip_data,
        use_existing_faiss=not args.rebuild_faiss,
        max_chunks=max_chunks,
        questions_per_chunk=args.questions_per_chunk,
        top_k=args.top_k,
        output_format=args.format,
        enable_post_process=not args.no_post_process,
        strict_mode=args.strict,
        shard_id=args.shard_id,
        num_shards=args.num_shards
    )
    
    print("\n" + "=" * 50)
    print("执行结果摘要:")
    print("=" * 50)
    
    if "final_statistics" in results:
        stats = results["final_statistics"]
        print(f"总耗时: {stats['total_time_seconds']:.2f} 秒")
        print(f"生成问答对: {stats['total_qa_pairs']}")
        print(f"成功率: {stats['success_rate']:.2%}")
        
        if 'post_process' in stats:
            pp = stats['post_process']
            print(f"\n后处理结果:")
            print(f"  干净数据: {pp['clean']}")
            print(f"  已修复: {pp['fixed']}")
            print(f"  已丢弃: {pp['discarded']}")


def cmd_step1(args):
    """步骤1: 数据加载"""
    pipeline = create_pipeline(args.config)
    result = pipeline.step1_load_data()
    print(f"\n结果: {result}")


def cmd_step2(args):
    """步骤2: FAISS 构建"""
    pipeline = create_pipeline(args.config)
    
    # 需要先加载数据
    if not args.use_existing:
        pipeline.step1_load_data()
    
    result = pipeline.step2_build_faiss(use_existing=args.use_existing)
    print(f"\n结果: {result}")


def cmd_step3(args):
    """步骤3: 问题生成"""
    pipeline = create_pipeline(args.config)
    
    # 加载数据
    pipeline.step1_load_data()
    pipeline.step2_build_faiss(use_existing=True)
    
    result = pipeline.step3_generate_questions(
        max_chunks=args.max_chunks,
        questions_per_chunk=args.questions_per_chunk
    )
    print(f"\n结果: {result}")


def cmd_step4(args):
    """步骤4: 答案生成"""
    pipeline = create_pipeline(args.config)
    
    # 加载 FAISS 索引
    pipeline.step2_build_faiss(use_existing=True)
    
    # 加载问题
    if args.questions_file:
        pipeline.load_intermediate_questions(args.questions_file)
    else:
        # 需要先生成问题
        pipeline.step1_load_data()
        pipeline.step3_generate_questions(max_chunks=args.max_chunks)
    
    result = pipeline.step4_generate_answers(top_k=args.top_k)
    print(f"\n结果: {result}")


def cmd_step5(args):
    """步骤5: 保存数据集"""
    pipeline = create_pipeline(args.config)
    
    # 加载已有数据
    if args.qa_file:
        from ranstruct.answer_generator import DatasetBuilder
        qa_pairs = DatasetBuilder.load_dataset(args.qa_file)
        pipeline._qa_pairs = qa_pairs
    
    if not pipeline._qa_pairs:
        print("错误: 没有可保存的数据，请先生成问答对")
        return
    
    result = pipeline.step5_save_dataset(format=args.format, filepath=args.output)
    print(f"\n结果: {result}")


def cmd_step6(args):
    """步骤6: 质量后处理"""
    pipeline = create_pipeline(args.config)
    
    # 加载已有数据
    if args.input:
        from ranstruct.answer_generator import DatasetBuilder
        qa_pairs = DatasetBuilder.load_dataset(args.input)
        pipeline._qa_pairs = qa_pairs
    
    if not pipeline._qa_pairs:
        print("错误: 没有可处理的数据，请指定 --input 参数")
        return
    
    result = pipeline.step6_post_process(
        strict_mode=args.strict,
        save_cleaned=True,
        filepath=args.output
    )
    
    print("\n" + "=" * 50)
    print("后处理结果:")
    print("=" * 50)
    print(f"原始数据: {result['original_count']}")
    print(f"清洗后保留: {result['cleaned_count']}")
    print(f"  干净数据: {result['clean_data']}")
    print(f"  已修复: {result['fixed_data']}")
    print(f"  已丢弃: {result['discarded_data']}")
    if result['issues_by_type']:
        print(f"\n问题类型分布:")
        for issue, count in result['issues_by_type'].items():
            print(f"  {issue}: {count}")


def cmd_analyze(args):
    """分析数据集质量"""
    pipeline = create_pipeline(args.config)
    
    # 加载已有数据
    if args.input:
        from ranstruct.answer_generator import DatasetBuilder
        qa_pairs = DatasetBuilder.load_dataset(args.input)
        pipeline._qa_pairs = qa_pairs
    
    if not pipeline._qa_pairs:
        print("错误: 没有可分析的数据，请指定 --input 参数")
        return
    
    result = pipeline.analyze_quality()
    
    print("\n" + "=" * 50)
    print("数据集质量分析报告")
    print("=" * 50)
    print(f"总问答对: {result['total_qa_pairs']}")
    print(f"干净数据: {result['clean_data']} ({result['clean_rate']:.1%})")
    print(f"平均置信度: {result['avg_confidence']:.2f}")
    
    if result['issues_by_type']:
        print(f"\n问题类型分布:")
        for issue, count in result['issues_by_type'].items():
            pct = count / result['total_qa_pairs'] * 100
            print(f"  {issue}: {count} ({pct:.1f}%)")
    
    if result.get('examples'):
        print(f"\n问题示例:")
        for issue, example in result['examples'].items():
            print(f"\n  【{issue}】")
            print(f"  Q: {example['question']}...")
            print(f"  A: {example['answer_preview']}...")


def cmd_info(args):
    """显示配置信息"""
    config = Config.from_yaml(args.config) if args.config else Config()
    
    print("=" * 50)
    print("RANSTRUCT 配置信息")
    print("=" * 50)
    
    print("\n模型配置:")
    print(f"  问题生成模型: {config.model.question_model}")
    print(f"  答案生成模型: {config.model.answer_model}")
    print(f"  嵌入模型: {config.model.embedding_model}")
    
    print("\n分块配置:")
    print(f"  RAG Chunk 大小: {config.chunk.rag_chunk_size}")
    print(f"  LTG Chunk 大小: {config.chunk.ltg_chunk_size}")
    
    print("\n数据源配置:")
    print(f"  O-RAN 规范路径: {config.data_source.oran_spec_path}")
    print(f"  srsRAN 代码路径: {config.data_source.srsran_code_path}")
    print(f"  代码集路径: {config.data_source.codeset_path}")
    print(f"  FAISS 索引路径: {config.data_source.faiss_index_path}")
    
    print("\n生成配置:")
    print(f"  每 chunk 问题数: {config.generation.questions_per_chunk}")
    print(f"  FAISS Top-K: {config.faiss.top_k}")
    
    print("\n输出配置:")
    print(f"  输出目录: {config.output.output_dir}")
    print(f"  数据集文件: {config.output.dataset_filename}")


def cmd_test(args):
    """测试模式"""
    print("=" * 50)
    print("RANSTRUCT 测试模式")
    print("=" * 50)
    
    pipeline = create_pipeline(args.config)
    
    # 测试数据加载
    print("\n1. 测试数据加载...")
    try:
        oran_docs = pipeline.data_processor.load_oran_specifications()
        print(f"   ✓ 加载了 {len(oran_docs)} 个 O-RAN 文档")
    except Exception as e:
        print(f"   ✗ 加载失败: {e}")
    
    # 测试 FAISS
    print("\n2. 测试 FAISS 索引...")
    try:
        index_path = pipeline.config.data_source.faiss_index_path
        if index_path and (index_path / "index.faiss").exists():
            pipeline.faiss_manager.load_index()
            stats = pipeline.faiss_manager.get_statistics()
            print(f"   ✓ FAISS 索引包含 {stats['total_vectors']} 个向量")
            
            # 测试搜索
            results = pipeline.faiss_manager.search("O-RAN architecture", top_k=3)
            print(f"   ✓ 搜索测试返回 {len(results)} 个结果")
        else:
            print("   ! FAISS 索引不存在")
    except Exception as e:
        print(f"   ✗ FAISS 测试失败: {e}")
    
    # 测试 Ollama 连接
    print("\n3. 测试 Ollama 连接...")
    try:
        import ollama
        models = ollama.list()
        # 兼容不同版本的 API 响应格式
        model_list = models.get('models', [])
        model_names = []
        for m in model_list:
            # 尝试不同的字段名
            name = m.get('name') or m.get('model') or str(m)
            model_names.append(name)
        print(f"   ✓ Ollama 可用，已安装模型: {', '.join(model_names[:5])}")
    except Exception as e:
        print(f"   ✗ Ollama 连接失败: {e}")
    
    print("\n测试完成!")


def main():
    parser = argparse.ArgumentParser(
        description='RANSTRUCT - O-RAN 领域数据集生成框架',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s run                        # 运行完整管道（含质量后处理）
  %(prog)s run --max-chunks 10        # 测试模式，限制 chunks 数量
  %(prog)s run --rebuild-faiss        # 重建 FAISS 索引
  %(prog)s run --no-post-process      # 禁用质量后处理
  %(prog)s run --strict               # 严格模式（丢弃而非修复问题数据）
  %(prog)s step6 -i data.jsonl        # 单独执行质量后处理
  %(prog)s analyze -i data.jsonl      # 分析数据集质量
  %(prog)s info                       # 显示配置信息
  %(prog)s test                       # 运行测试
        """
    )
    
    parser.add_argument(
        '--config', '-c',
        help='配置文件路径 (YAML)'
    )
    parser.add_argument(
        '--log-level', '-l',
        default='INFO',
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'],
        help='日志级别'
    )
    
    subparsers = parser.add_subparsers(dest='command', help='子命令')
    
    # run 命令
    run_parser = subparsers.add_parser('run', help='运行完整管道')
    run_parser.add_argument('--skip-data', action='store_true', help='跳过数据加载')
    run_parser.add_argument('--rebuild-faiss', action='store_true', help='重建 FAISS 索引')
    run_parser.add_argument('--max-chunks', type=int, help='最大 chunks 数量')
    run_parser.add_argument('--questions-per-chunk', type=int, help='每 chunk 问题数')
    run_parser.add_argument('--top-k', type=int, help='RAG Top-K')
    run_parser.add_argument('--format', default='jsonl', 
                           choices=['jsonl', 'json', 'training', 'training_system', 'conversation', 'chatml'],
                           help='输出格式 (推荐 chatml 用于 Qwen SFT)')
    run_parser.add_argument('--no-post-process', action='store_true', 
                           help='禁用质量后处理')
    run_parser.add_argument('--strict', action='store_true',
                           help='严格模式：丢弃有问题的数据而非修复')
    run_parser.add_argument('--test', action='store_true',
                           help='测试模式：等效于 --max-chunks 10')
    run_parser.add_argument('--timestamp', action='store_true',
                           help='使用时间戳文件名（防止覆盖）')
    run_parser.add_argument('--shard-id', type=int, help='当前分片ID (0-N)')
    run_parser.add_argument('--num-shards', type=int, help='总分片数')
    run_parser.set_defaults(func=cmd_run)
    
    # step1 命令
    step1_parser = subparsers.add_parser('step1', help='步骤1: 数据加载')
    step1_parser.set_defaults(func=cmd_step1)
    
    # step2 命令
    step2_parser = subparsers.add_parser('step2', help='步骤2: FAISS 构建')
    step2_parser.add_argument('--use-existing', action='store_true', help='使用已有索引')
    step2_parser.set_defaults(func=cmd_step2)
    
    # step3 命令
    step3_parser = subparsers.add_parser('step3', help='步骤3: 问题生成')
    step3_parser.add_argument('--max-chunks', type=int, help='最大 chunks 数量')
    step3_parser.add_argument('--questions-per-chunk', type=int, help='每 chunk 问题数')
    step3_parser.set_defaults(func=cmd_step3)
    
    # step4 命令
    step4_parser = subparsers.add_parser('step4', help='步骤4: 答案生成')
    step4_parser.add_argument('--questions-file', help='问题文件路径')
    step4_parser.add_argument('--max-chunks', type=int, help='最大 chunks 数量')
    step4_parser.add_argument('--top-k', type=int, help='RAG Top-K')
    step4_parser.set_defaults(func=cmd_step4)
    
    # step5 命令
    step5_parser = subparsers.add_parser('step5', help='步骤5: 保存数据集')
    step5_parser.add_argument('--qa-file', help='问答对文件路径')
    step5_parser.add_argument('--output', '-o', help='输出文件路径')
    step5_parser.add_argument('--format', default='jsonl',
                             choices=['jsonl', 'json', 'training', 'training_system', 'conversation', 'chatml'],
                             help='输出格式 (推荐 chatml 用于 Qwen SFT)')
    step5_parser.set_defaults(func=cmd_step5)
    
    # step6 命令
    step6_parser = subparsers.add_parser('step6', help='步骤6: 质量后处理')
    step6_parser.add_argument('--input', '-i', help='输入数据集文件路径')
    step6_parser.add_argument('--output', '-o', help='输出文件路径')
    step6_parser.add_argument('--strict', action='store_true',
                             help='严格模式：丢弃有问题的数据而非修复')
    step6_parser.set_defaults(func=cmd_step6)
    
    # analyze 命令
    analyze_parser = subparsers.add_parser('analyze', help='分析数据集质量')
    analyze_parser.add_argument('--input', '-i', help='输入数据集文件路径')
    analyze_parser.set_defaults(func=cmd_analyze)
    
    # info 命令
    info_parser = subparsers.add_parser('info', help='显示配置信息')
    info_parser.set_defaults(func=cmd_info)
    
    # test 命令
    test_parser = subparsers.add_parser('test', help='运行测试')
    test_parser.set_defaults(func=cmd_test)
    
    args = parser.parse_args()
    
    setup_logging(args.log_level)
    
    if args.command:
        args.func(args)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()

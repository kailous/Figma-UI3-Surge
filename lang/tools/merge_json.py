#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
JSON 合并脚本

功能:
    该脚本用于合并指定目录中所有以特定前缀开头的 JSON 文件，并将结果写入到一个输出文件中。
    合并后的 JSON 文件将包含所有源文件中的键值对。如果存在相同的键，后加载的文件会覆盖之前的值。

用法:
    python merge_json.py <input_directory> <output_file> <file_prefix>

参数:
    input_directory      输入文件所在的目录（必需）
    output_file          合并后的输出文件路径（必需）
    file_prefix          需要合并的文件前缀（必需）

可选参数:
    --verbose, -v        是否显示详细的处理信息（可选）
                        使用 `--verbose` 或 `-v` 可以显示每个文件的处理状态

示例:
    python merge_json.py jp_split zh.json part_
    python merge_json.py ./data merged.json part_ --verbose
"""

import json
import os
import sys
import argparse

def merge_json_files(input_directory, output_file, file_prefix, verbose=False):
    """
    合并指定目录中的所有 JSON 文件，并将结果写入到一个输出文件中。

    参数：
        input_directory (str): 输入文件所在的目录
        output_file (str): 合并后的输出文件路径
        file_prefix (str): 需要合并的文件前缀
        verbose (bool): 是否显示详细的处理信息
    """
    merged_data = {}  # 用于存储合并后的数据

    # 检查输入目录是否存在
    if not os.path.isdir(input_directory):
        print(f"错误: 输入目录 '{input_directory}' 不存在。")
        sys.exit(1)

    # 获取目录下所有以指定前缀开头且以 '.json' 结尾的文件列表
    file_list = [f for f in os.listdir(input_directory) 
                if f.startswith(file_prefix) and f.endswith('.json')]
    file_list.sort()  # 确保文件按顺序合并

    # 找不到文件时报错
    if not file_list:
        print("错误: 未找到符合条件的文件。")
        sys.exit(1)

    if verbose:
        print(f"找到 {len(file_list)} 个符合条件的文件。")

    # 逐个处理文件
    for input_file in file_list:
        filepath = os.path.join(input_directory, input_file)  # 获取文件的完整路径
        if verbose:
            print(f"正在处理文件: {filepath}")
        try:
            # 读取并解析 JSON 文件
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
            if verbose:
                print(f"已从 {input_file} 加载数据: {len(data)} 个键值对")
            if isinstance(data, dict):
                merged_data.update(data)  # 更新合并数据字典
            else:
                print(f"警告: 文件 '{input_file}' 的 JSON 结构不是对象，已跳过。")
        except json.JSONDecodeError as e:
            print(f"错误: 读取 '{input_file}' 时无法解析 JSON。{e}")
        except Exception as e:
            print(f"错误: 处理 '{input_file}' 时发生问题。{e}")

    try:
        # 将合并后的数据写入输出文件
        with open(output_file, 'w', encoding='utf-8') as out_file:
            json.dump(merged_data, out_file, ensure_ascii=False, indent=4)
        if verbose:
            print(f"成功: 数据已合并到 '{output_file}'。")
        else:
            print(f"数据已合并到 '{output_file}'。")
    except Exception as e:
        print(f"错误: 写入输出文件 '{output_file}' 时出错。{e}")
        sys.exit(1)

def parse_arguments():
    """
    解析命令行参数。

    返回:
        args: 解析后的命令行参数
    """
    parser = argparse.ArgumentParser(
        description="合并指定目录中所有以特定前缀开头的 JSON 文件，并将结果写入到一个输出文件中。",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="""
示例:
    python merge_json.py jp_split zh.json part_
    python merge_json.py ./data merged.json part_ --verbose
"""
    )
    parser.add_argument("input_directory", help="输入文件所在的目录")
    parser.add_argument("output_file", help="合并后的输出文件路径")
    parser.add_argument("file_prefix", help="需要合并的文件前缀")
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="是否显示详细的处理信息"
    )

    # 如果没有提供任何参数，则显示帮助并退出
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    return parser.parse_args()

def main():
    args = parse_arguments()
    merge_json_files(
        input_directory=args.input_directory,
        output_file=args.output_file,
        file_prefix=args.file_prefix,
        verbose=args.verbose
    )

if __name__ == "__main__":
    main()
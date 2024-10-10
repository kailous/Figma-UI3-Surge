#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
JSON 最小化脚本

功能:
    该脚本用于最小化指定的 JSON 文件，通过移除所有不必要的空格和换行符来减小文件大小。
    最小化后的 JSON 会被保存为一个新的文件，文件名在原文件名后添加 `.br` 后缀。

用法:
    python zip_json.py <input_file> [--output <output_file>]

参数:
    input_file        输入的 JSON 文件路径（必需）
    --output, -o      输出文件路径（可选）
                      如果未指定，默认在原文件名后添加 `.br` 后缀

示例:
    python minify_json.py data.json
    python minify_json.py data.json --output minified_data.json.br
"""

import sys
import os
import json
import argparse

def minify_json(input_path, output_path):
    """
    最小化 JSON 文件。

    参数：
        input_path (str): 输入的 JSON 文件路径
        output_path (str): 输出的最小化 JSON 文件路径
    """
    if not os.path.isfile(input_path):
        print(f"错误: 文件 '{input_path}' 不存在。")
        sys.exit(1)
    
    try:
        with open(input_path, 'r', encoding='utf-8') as f_in:
            data = json.load(f_in)
        
        # 最小化 JSON，移除所有不必要的空格和换行符
        minified_json = json.dumps(data, separators=(',', ':'), ensure_ascii=False)
        
        with open(output_path, 'w', encoding='utf-8') as f_out:
            f_out.write(minified_json)
        
        print(f"成功: 文件已最小化并保存为 '{output_path}'。")
    except json.JSONDecodeError as e:
        print(f"错误: 无法解析 JSON 文件。{e}")
        sys.exit(1)
    except Exception as e:
        print(f"处理文件时出错: {e}")
        sys.exit(1)

def parse_arguments():
    """
    解析命令行参数。

    返回:
        args: 解析后的命令行参数
    """
    parser = argparse.ArgumentParser(
        description="将指定的 JSON 文件最小化，移除所有不必要的空格和换行符。",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="""
示例:
    python minify_json.py data.json
    python minify_json.py data.json --output minified_data.json.br
"""
    )
    parser.add_argument("input_file", help="输入的 JSON 文件路径")
    parser.add_argument(
        "--output", "-o",
        help="输出的最小化 JSON 文件路径\n如果未指定，默认在原文件名后添加 `.br` 后缀"
    )
    
    # 如果没有提供任何参数，则显示帮助并退出
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    
    return parser.parse_args()

def main():
    args = parse_arguments()
    
    input_path = args.input_file
    
    if args.output:
        output_path = args.output
    else:
        output_path = input_path + '.br'
    
    minify_json(input_path, output_path)

if __name__ == "__main__":
    main()
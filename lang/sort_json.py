#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
JSON 行长度排序脚本

功能:
    该脚本用于将指定的 JSON 文件中的键值对按每行的长度从短到长排序。
    排序后的 JSON 将被保存为一个新的文件，文件名在原文件名上加上 '+' 符号。

用法:
    python sort_json.py <input_file> [--output <output_file>]

参数:
    input_file          输入的 JSON 文件路径（必需）
    --output, -o        输出的排序后 JSON 文件路径（可选）
                        如果未指定，默认在原文件名上加上 '+' 符号

示例:
    python sort_json.py data.json
    python sort_json.py data.json --output sorted_data.json
"""

import sys
import json
import os
import argparse

def sort_json_by_line_length(input_file, output_file):
    """
    将 JSON 文件中的键值对按每行的长度从短到长排序。

    参数：
        input_file (str): 输入的 JSON 文件路径
        output_file (str): 输出的排序后 JSON 文件路径
    """
    if not os.path.isfile(input_file):
        print(f"错误: 输入文件 '{input_file}' 不存在。")
        sys.exit(1)
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"错误: 无法解析 JSON 文件。{e}")
        sys.exit(1)
    except Exception as e:
        print(f"处理文件时出错: {e}")
        sys.exit(1)
    
    if not isinstance(data, dict):
        print("错误: 不支持的 JSON 结构。请提供一个 JSON 对象（字典）。")
        sys.exit(1)
    
    # 将字典项转换为列表，包含 (key, value) 元组
    items = list(data.items())
    
    def line_length(item):
        """
        计算键值对行的长度。

        参数：
            item (tuple): (key, value) 元组

        返回:
            int: 行的长度
        """
        key, value = item
        # 将键和值转换为字符串形式，包括缩进和格式
        line = f'    "{key}": {json.dumps(value, ensure_ascii=False)},\n'
        return len(line)
    
    # 按行长度从短到长排序
    items.sort(key=line_length)
    
    # 重新构建排序后的字典
    sorted_data = {key: value for key, value in items}
    
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(sorted_data, f, ensure_ascii=False, indent=4)
        print(f"成功: 已将排序后的 JSON 写入 '{output_file}'。")
    except Exception as e:
        print(f"写入文件 '{output_file}' 时出错: {e}")
        sys.exit(1)

def parse_arguments():
    """
    解析命令行参数。

    返回:
        args: 解析后的命令行参数
    """
    parser = argparse.ArgumentParser(
        description="将指定的 JSON 文件中的键值对按每行的长度从短到长排序。",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="""
示例:
    python sort_json.py data.json
    python sort_json.py data.json --output sorted_data.json
"""
    )
    parser.add_argument("input_file", help="输入的 JSON 文件路径")
    parser.add_argument(
        "--output", "-o",
        help="输出的排序后 JSON 文件路径\n如果未指定，默认在原文件名上加上 '+' 符号"
    )
    
    # 如果没有提供任何参数，则显示帮助并退出
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    
    return parser.parse_args()

def main():
    args = parse_arguments()
    
    input_file = args.input_file
    
    if args.output:
        output_file = args.output
    else:
        base, ext = os.path.splitext(input_file)
        output_file = f"{base}+{ext}"
    
    sort_json_by_line_length(input_file, output_file)

if __name__ == "__main__":
    main()
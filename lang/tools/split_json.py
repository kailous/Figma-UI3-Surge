#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
JSON 分割脚本

功能:
    该脚本用于将一个大的 JSON 文件按指定的行数分割成多个小文件。
    支持将字典类型的 JSON 按键值对分割，每个分割文件包含指定数量的行。

用法:
    python split_json.py <input_file> <output_folder> [--lines_per_file LINES]

参数:
    input_file        输入的 JSON 文件路径
    output_folder     输出文件夹路径
    --lines_per_file  每个分割文件包含的行数，默认为 50 行

示例:
    python split_json.py jp.json jp_split --lines_per_file 100
    python split_json.py jp.json jp_split
"""

import json
import os
import sys
import argparse

def split_json_file(input_file, output_folder, lines_per_file=50):
    """
    将一个大的 JSON 文件按指定行数分割成多个小文件。

    参数：
        input_file (str): 输入的 JSON 文件路径
        output_folder (str): 输出文件夹路径
        lines_per_file (int): 每个分割文件包含的行数，默认为 50 行
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
    
    if isinstance(data, dict):
        # 将字典转换为项列表
        items = list(data.items())
        total_lines = len(items)
        file_index = 1

        # 创建输出文件夹
        os.makedirs(output_folder, exist_ok=True)
        
        for i in range(0, total_lines, lines_per_file):
            chunk = dict(items[i:i + lines_per_file])  # 分割字典为小块
            output_file = os.path.join(output_folder, f'part_{file_index:02}.json')
            try:
                with open(output_file, 'w', encoding='utf-8') as out_file:
                    json.dump(chunk, out_file, ensure_ascii=False, indent=4)
                print(f"成功: 创建 '{output_file}'。")
            except Exception as e:
                print(f"写入文件 '{output_file}' 时出错: {e}")
                sys.exit(1)
            file_index += 1
        print(f"完成: 总共分割了 {file_index - 1} 个文件。")
    else:
        print("错误: 不支持的 JSON 结构。请提供一个 JSON 对象。")
        sys.exit(1)

def parse_arguments():
    """
    解析命令行参数。
    
    返回:
        args: 解析后的命令行参数
    """
    parser = argparse.ArgumentParser(
        description="将一个大的 JSON 文件按指定行数分割成多个小文件。",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("input_file", help="输入的 JSON 文件路径")
    parser.add_argument("output_folder", help="输出文件夹路径")
    parser.add_argument(
        "--lines_per_file", 
        type=int, 
        default=50, 
        help="每个分割文件包含的行数，默认为 50 行"
    )
    
    # 如果没有提供任何参数，则显示帮助并退出
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    
    return parser.parse_args()

def main():
    args = parse_arguments()
    split_json_file(args.input_file, args.output_folder, args.lines_per_file)

if __name__ == "__main__":
    main()
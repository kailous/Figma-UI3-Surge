#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
JSON 键差异比较脚本

功能:
    该脚本用于比较两个 JSON 文件中的键，找出一个文件中存在而另一个文件中不存在的键。
    比较结果将分别保存到两个新的 JSON 文件中。

用法:
    python compare_json_keys.py <en_file> <zh_file> [--en_output <en_output_file>] [--zh_output <zh_output_file>]

参数:
    en_file               第一个输入的 JSON 文件路径（通常为英文版，例如 en.json）
    zh_file               第二个输入的 JSON 文件路径（通常为中文版，例如 zh.json）
    --en_output, -e       输出文件路径，用于保存 en_file 中有而 zh_file 中没有的键
                          默认为 'en_not_in_zh.json'
    --zh_output, -z       输出文件路径，用于保存 zh_file 中有而 en_file 中没有的键
                          默认为 'zh_not_in_en.json'

示例:
    python compare_json_keys.py en/en.json zh.json
    python compare_json_keys.py en/en.json zh.json --en_output missing_en.json --zh_output missing_zh.json
"""

import json
import os
import sys
import argparse

def compare_json_keys(en_file, zh_file, en_output, zh_output, verbose=False):
    """
    比较两个 JSON 文件中的键，找出差异部分并保存到输出文件中。

    参数：
        en_file (str): 第一个输入的 JSON 文件路径
        zh_file (str): 第二个输入的 JSON 文件路径
        en_output (str): 输出文件路径，用于保存 en_file 中有而 zh_file 中没有的键
        zh_output (str): 输出文件路径，用于保存 zh_file 中有而 en_file 中没有的键
        verbose (bool): 是否显示详细的处理信息
    """
    # 检查输入文件是否存在
    if not os.path.isfile(en_file):
        print(f"错误: 文件 '{en_file}' 不存在。")
        sys.exit(1)
    if not os.path.isfile(zh_file):
        print(f"错误: 文件 '{zh_file}' 不存在。")
        sys.exit(1)
    
    try:
        # 加载第一个 JSON 文件
        with open(en_file, 'r', encoding='utf-8') as f:
            en_data = json.load(f)
        if verbose:
            print(f"成功加载 '{en_file}'，包含 {len(en_data)} 个键。")
    except json.JSONDecodeError as e:
        print(f"错误: 无法解析 JSON 文件 '{en_file}'。{e}")
        sys.exit(1)
    except Exception as e:
        print(f"错误: 读取文件 '{en_file}' 时出错。{e}")
        sys.exit(1)
    
    try:
        # 加载第二个 JSON 文件
        with open(zh_file, 'r', encoding='utf-8') as f:
            zh_data = json.load(f)
        if verbose:
            print(f"成功加载 '{zh_file}'，包含 {len(zh_data)} 个键。")
    except json.JSONDecodeError as e:
        print(f"错误: 无法解析 JSON 文件 '{zh_file}'。{e}")
        sys.exit(1)
    except Exception as e:
        print(f"错误: 读取文件 '{zh_file}' 时出错。{e}")
        sys.exit(1)
    
    # 确保两个 JSON 文件都是字典类型
    if not isinstance(en_data, dict):
        print(f"错误: '{en_file}' 的 JSON 结构不是对象（字典）。")
        sys.exit(1)
    if not isinstance(zh_data, dict):
        print(f"错误: '{zh_file}' 的 JSON 结构不是对象（字典）。")
        sys.exit(1)
    
    # 获取键集合
    en_keys = set(en_data.keys())
    zh_keys = set(zh_data.keys())
    
    if verbose:
        print(f"'{en_file}' 中共有 {len(en_keys)} 个键。")
        print(f"'{zh_file}' 中共有 {len(zh_keys)} 个键。")
    
    # 找出 en 有而 zh 没有的键
    en_diff_keys = en_keys - zh_keys
    if verbose:
        print(f"'{en_file}' 中有 {len(en_diff_keys)} 个键在 '{zh_file}' 中不存在。")
    
    # 找出 zh 有而 en 没有的键
    zh_diff_keys = zh_keys - en_keys
    if verbose:
        print(f"'{zh_file}' 中有 {len(zh_diff_keys)} 个键在 '{en_file}' 中不存在。")
    
    # 获取对应的键值对
    en_diff_dict = {key: en_data[key] for key in en_diff_keys}
    zh_diff_dict = {key: zh_data[key] for key in zh_diff_keys}
    
    try:
        # 将 en_diff_dict 写入输出文件
        with open(en_output, 'w', encoding='utf-8') as f:
            json.dump(en_diff_dict, f, ensure_ascii=False, indent=4)
        if verbose:
            print(f"成功: '{en_output}' 已保存包含 {len(en_diff_dict)} 个键。")
    except Exception as e:
        print(f"错误: 写入文件 '{en_output}' 时出错。{e}")
        sys.exit(1)
    
    try:
        # 将 zh_diff_dict 写入输出文件
        with open(zh_output, 'w', encoding='utf-8') as f:
            json.dump(zh_diff_dict, f, ensure_ascii=False, indent=4)
        if verbose:
            print(f"成功: '{zh_output}' 已保存包含 {len(zh_diff_dict)} 个键。")
    except Exception as e:
        print(f"错误: 写入文件 '{zh_output}' 时出错。{e}")
        sys.exit(1)
    
    print("比较完成。")

def parse_arguments():
    """
    解析命令行参数。

    返回:
        args: 解析后的命令行参数
    """
    parser = argparse.ArgumentParser(
        description="比较两个 JSON 文件中的键，找出一个文件中存在而另一个文件中不存在的键。",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="""
示例:
    python compare_json_keys.py en/en.json zh.json
    python compare_json_keys.py en/en.json zh.json --en_output missing_en.json --zh_output missing_zh.json
    python compare_json_keys.py en/en.json zh.json -e missing_en.json -z missing_zh.json
"""
    )
    parser.add_argument("en_file", help="第一个输入的 JSON 文件路径（通常为英文版，例如 en.json）")
    parser.add_argument("zh_file", help="第二个输入的 JSON 文件路径（通常为中文版，例如 zh.json）")
    parser.add_argument(
        "--en_output", "-e",
        default="en_not_in_zh.json",
        help="输出文件路径，用于保存 en_file 中有而 zh_file 中没有的键\n默认为 'en_not_in_zh.json'"
    )
    parser.add_argument(
        "--zh_output", "-z",
        default="zh_not_in_en.json",
        help="输出文件路径，用于保存 zh_file 中有而 en_file 中没有的键\n默认为 'zh_not_in_en.json'"
    )
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
    compare_json_keys(
        en_file=args.en_file,
        zh_file=args.zh_file,
        en_output=args.en_output,
        zh_output=args.zh_output,
        verbose=args.verbose
    )

if __name__ == "__main__":
    main()
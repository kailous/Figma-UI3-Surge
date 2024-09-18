import sys
import os
import json

def minify_json(input_path):
    if not os.path.isfile(input_path):
        print(f"错误: 文件 '{input_path}' 不存在。")
        sys.exit(1)
    
    try:
        with open(input_path, 'r', encoding='utf-8') as f_in:
            data = json.load(f_in)
        
        minified_json = json.dumps(data, separators=(',', ':'))
        
        output_path = input_path + '.br'
        
        with open(output_path, 'w', encoding='utf-8') as f_out:
            f_out.write(minified_json)
        
        print(f"成功: 文件已最小化并保存为 '{output_path}'。")
    except json.JSONDecodeError as e:
        print(f"错误: 无法解析 JSON 文件。{e}")
        sys.exit(1)
    except Exception as e:
        print(f"处理文件时出错: {e}")
        sys.exit(1)

def print_usage():
    script_name = os.path.basename(sys.argv[0])
    print(f"用法: python {script_name} <path_to_json_file>")
    print("示例: python minify_json.py data.json")

def main():
    if len(sys.argv) != 2:
        print("错误: 参数数量不正确。")
        print_usage()
        sys.exit(1)
    
    input_path = sys.argv[1]
    minify_json(input_path)

if __name__ == "__main__":
    main()
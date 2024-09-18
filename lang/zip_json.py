import sys
import os
import brotli

def compress_file(input_path):
    if not os.path.isfile(input_path):
        print(f"错误: 文件 '{input_path}' 不存在。")
        sys.exit(1)

    if not input_path.lower().endswith('.json'):
        print(f"警告: 文件 '{input_path}' 似乎不是一个 JSON 文件。继续压缩。")

    output_path = input_path + '.br'

    try:
        with open(input_path, 'rb') as f_in:
            data = f_in.read()
            compressed_data = brotli.compress(data)
        
        with open(output_path, 'wb') as f_out:
            f_out.write(compressed_data)
        
        print(f"成功: 文件已压缩为 '{output_path}'。")
    except Exception as e:
        print(f"压缩过程中出现错误: {e}")
        sys.exit(1)

def print_usage():
    script_name = os.path.basename(sys.argv[0])
    print(f"用法: python {script_name} <path_to_json_file>")
    print("示例: python compress_json.py data.json")

def main():
    if len(sys.argv) != 2:
        print("错误: 参数数量不正确。")
        print_usage()
        sys.exit(1)
    
    input_path = sys.argv[1]
    compress_file(input_path)

if __name__ == "__main__":
    main()
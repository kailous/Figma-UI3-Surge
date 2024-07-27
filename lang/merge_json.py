import json
import os

def merge_json_files(input_directory, output_file):
    merged_data = {}
    file_list = [f for f in os.listdir(input_directory) if f.startswith('en_part_') and f.endswith('.json')]
    file_list.sort()  # 确保按顺序合并
    
    if not file_list:
        print("No files found.")
        return
    
    for input_file in file_list:
        filepath = os.path.join(input_directory, input_file)
        print(f"Processing file: {filepath}")
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                print(f"Loaded data from {input_file}: {data}")
                merged_data.update(data)
        except json.JSONDecodeError as e:
            print(f"Error reading {input_file}: {e}")
        except Exception as e:
            print(f"An error occurred with {input_file}: {e}")

    with open(output_file, 'w', encoding='utf-8') as out_file:
        json.dump(merged_data, out_file, ensure_ascii=False, indent=4)
    print(f"Data merged into {output_file}")

# 调用函数，假设分割文件在 'zh' 文件夹，输出文件名为 'merged_output.json'
merge_json_files('zh', 'zh.json')
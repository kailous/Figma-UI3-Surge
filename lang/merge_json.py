import json
import os

def merge_json_files(input_directory, output_file):
    merged_data = {}
    file_list = [f for f in os.listdir(input_directory) if f.startswith('zh_part_') and f.endswith('.json')]
    file_list.sort()  # 确保按顺序合并
    
    for input_file in file_list:
        with open(os.path.join(input_directory, input_file), 'r', encoding='utf-8') as f:
            data = json.load(f)
            merged_data.update(data)
    
    with open(output_file, 'w', encoding='utf-8') as out_file:
        json.dump(merged_data, out_file, ensure_ascii=False, indent=4)

# 调用函数，假设分割文件在 'zh' 文件夹，输出文件名为 'merged_output.json'
merge_json_files('zh', 'zh.json')
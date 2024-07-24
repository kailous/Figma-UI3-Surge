import json
import os

def split_json_file(input_file, lines_per_file=50):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    if isinstance(data, dict):
        # 将字典转换为项列表
        items = list(data.items())
        total_lines = len(items)
        file_index = 1

        # 创建输出文件夹
        output_folder = 'en'
        os.makedirs(output_folder, exist_ok=True)
        
        for i in range(0, total_lines, lines_per_file):
            chunk = dict(items[i:i + lines_per_file])
            output_file = os.path.join(output_folder, f'en_part_{file_index:02}.json')
            with open(output_file, 'w', encoding='utf-8') as out_file:
                json.dump(chunk, out_file, ensure_ascii=False, indent=4)
            file_index += 1
    else:
        print("Unsupported JSON structure. Please provide a JSON object.")

# 调用函数，假设输入文件名为 'en.json'
split_json_file('en.json')
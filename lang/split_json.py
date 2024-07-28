import json
import os

def split_json_file(input_file, output_folder, lines_per_file=50):
    """
    将一个大的 JSON 文件按指定行数分割成多个小文件。

    参数：
    input_file (str): 输入的 JSON 文件路径
    output_folder (str): 输出文件夹路径
    lines_per_file (int): 每个分割文件包含的行数，默认为 50 行
    """
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
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
            with open(output_file, 'w', encoding='utf-8') as out_file:
                json.dump(chunk, out_file, ensure_ascii=False, indent=4)
            file_index += 1
    else:
        print("不支持的 JSON 结构。请提供一个 JSON 对象。")

# 设置变量
input_file = 'jp.json'  # 输入的 JSON 文件路径
output_folder = 'jp_split'  # 输出文件夹路径
lines_per_file = 50  # 每个分割文件包含的行数

# 调用函数
split_json_file(input_file, output_folder, lines_per_file)
import sys
import json
import os

def sort_json_by_line_length(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 将字典项转换为列表，包含 (key, value) 元组
    items = list(data.items())
    
    # 定义一个函数，计算每个键值对行的长度
    def line_length(item):
        key, value = item
        # 将键和值转换为字符串形式，包括缩进和格式
        line = f'    "{key}": {json.dumps(value, ensure_ascii=False)},\n'
        return len(line)
    
    # 按行长度从短到长排序
    items.sort(key=line_length)
    
    # 重新构建排序后的字典
    sorted_data = {key: value for key, value in items}
    
    # 创建新的文件名，在原文件名上加上 '+'
    base, ext = os.path.splitext(filename)
    new_filename = f"{base}+{ext}"
    
    # 将排序后的字典写入新文件
    with open(new_filename, 'w', encoding='utf-8') as f:
        json.dump(sorted_data, f, ensure_ascii=False, indent=4)
    
    print(f'已将排序后的 JSON 写入 {new_filename}')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('用法: python sort_json.py <目标文件>')
    else:
        filename = sys.argv[1]
        sort_json_by_line_length(filename)
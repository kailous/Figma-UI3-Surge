import json
import os

def merge_json_files(input_directory, output_file, file_prefix):
    """
    合并指定目录中的所有 JSON 文件，并将结果写入到一个输出文件中。

    参数：
    input_directory (str): 输入文件所在的目录
    output_file (str): 合并后的输出文件路径
    file_prefix (str): 需要合并的文件前缀
    """
    merged_data = {}  # 用于存储合并后的数据
    # 获取目录下所有以指定前缀开头且以 '.json' 结尾的文件列表
    file_list = [f for f in os.listdir(input_directory) if f.startswith(file_prefix) and f.endswith('.json')]
    file_list.sort()  # 确保文件按顺序合并

    # 找不到文件时报错
    if not file_list:
        print("未找到符合条件的文件。")
        return
    
    # 逐个处理文件
    for input_file in file_list:
        filepath = os.path.join(input_directory, input_file)  # 获取文件的完整路径
        print(f"正在处理文件: {filepath}")
        try:
            # 读取并解析 JSON 文件
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                print(f"已从 {input_file} 加载数据: {data}")
                merged_data.update(data)  # 更新合并数据字典
        except json.JSONDecodeError as e:
            print(f"读取 {input_file} 时出错: {e}")
        except Exception as e:
            print(f"处理 {input_file} 时发生错误: {e}")

    # 将合并后的数据写入输出文件
    with open(output_file, 'w', encoding='utf-8') as out_file:
        json.dump(merged_data, out_file, ensure_ascii=False, indent=4)
    print(f"数据已合并到 {output_file}")

# 设置变量
input_directory = 'jp_split'  # 输入文件所在的目录
output_file = 'zh.json'  # 合并后的输出文件路径
file_prefix = 'part_'  # 需要合并的文件前缀

# 调用函数
merge_json_files(input_directory, output_file, file_prefix)
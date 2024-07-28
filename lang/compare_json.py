import json

def compare_and_organize_files(zh_file, jp_file, zh_old_file, jp_new_file):
    """
    对比 zh.json 和 jp.json，将键相同的键值对整理到 zh_old.json，不同的键值对整理到 jp_new.json。

    参数：
    zh_file (str): zh.json 文件路径
    jp_file (str): jp.json 文件路径
    zh_old_file (str): zh_old.json 文件路径
    jp_new_file (str): jp_new.json 文件路径
    """
    # 读取 zh.json 文件
    with open(zh_file, 'r', encoding='utf-8') as f:
        zh_data = json.load(f)

    # 读取 jp.json 文件
    with open(jp_file, 'r', encoding='utf-8') as f:
        jp_data = json.load(f)

    # 初始化结果字典
    zh_old_data = {}
    jp_new_data = {}
    same_count = 0
    different_count = 0

    # 对比键
    for key in jp_data:
        if key in zh_data:
            zh_old_data[key] = zh_data[key]
            same_count += 1
        else:
            jp_new_data[key] = jp_data[key]
            different_count += 1

    # 计算 zh_data 中独有的键
    zh_unique_keys = set(zh_data.keys()) - set(jp_data.keys())
    for key in zh_unique_keys:
        zh_old_data[key] = zh_data[key]
        # 增加 zh_old_data 中的唯一键的计数
        # 不增加 different_count，因为它只计算 jp_data 中的不同键

    
    # 写入 zh_old.json 文件
    with open(zh_old_file, 'w', encoding='utf-8') as f:
        json.dump(zh_old_data, f, ensure_ascii=False, indent=4)

    # 写入 jp_new.json 文件
    with open(jp_new_file, 'w', encoding='utf-8') as f:
        json.dump(jp_new_data, f, ensure_ascii=False, indent=4)

    print(f"相同的键数量: {same_count}")
    # 检查两个版本是否完全一致
    if different_count == 0:
        print("两个版本完全一致!")
    else:
        print(f"不同的键数量: {different_count}")
    print(f"已将相同的键整理到 {zh_old_file}")
    print(f"已将不同的键整理到 {jp_new_file}")

# 设置变量
zh_file = 'zh.json'  # zh.json 文件路径
jp_file = 'jp.json'  # jp.json 文件路径
zh_old_file = 'zh_old.json'  # zh_old.json 文件路径
jp_new_file = 'jp_new.json'  # jp_new.json 文件路径

# 调用函数
compare_and_organize_files(zh_file, jp_file, zh_old_file, jp_new_file)
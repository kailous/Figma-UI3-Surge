import json

# 设定变量
en_file = 'en/en.json'
zh_file = 'zh.json'

# 加载 JSON 文件
with open(en_file, 'r', encoding='utf-8') as f:
    en_data = json.load(f)

with open(zh_file, 'r', encoding='utf-8') as f:
    zh_data = json.load(f)

# 获取键集合
en_keys = set(en_data.keys())
zh_keys = set(zh_data.keys())

# 找出 en 有而 zh 没有的键
en_diff_keys = en_keys - zh_keys

# 找出 zh 有而 en 没有的键
zh_diff_keys = zh_keys - en_keys

# 获取对应的键值对
en_diff_dict = {key: en_data[key] for key in en_diff_keys}
zh_diff_dict = {key: zh_data[key] for key in zh_diff_keys}

# 将结果写入 JSON 文件
with open('en_not_in_zh.json', 'w', encoding='utf-8') as f:
    json.dump(en_diff_dict, f, ensure_ascii=False, indent=4)

with open('zh_not_in_en.json', 'w', encoding='utf-8') as f:
    json.dump(zh_diff_dict, f, ensure_ascii=False, indent=4)
import json

def compress_json(input_file, output_file):
    """
    压缩 JSON 文件，去掉所有的换行和多余的空格，但保留值中的空格。

    参数：
    input_file (str): 输入的 JSON 文件路径
    output_file (str): 输出的压缩后的 JSON 文件路径
    """
    # 读取 JSON 文件
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 将 JSON 数据转换为紧凑的字符串
    compressed_json = json.dumps(data, separators=(',', ':'))

    # 写入压缩后的 JSON 文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(compressed_json)

    print(f"已将压缩后的 JSON 写入到 {output_file}")

# 设置变量
input_file = 'zh.json'  # 输入的 JSON 文件路径
output_file = 'zh.json.br'  # 输出的压缩后的 JSON 文件路径

# 调用函数
compress_json(input_file, output_file)
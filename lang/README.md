# Figma 汉化项目

## 概述

这是一个汉化工作的工作台。`Tools` 目录下提供了便利的工具，用于处理和管理多语言 JSON 字典文件。通过这些工具，您可以轻松地最小化、分割、排序、合并和比较 JSON 文件，从而简化多语言文件的维护和管理。

## 目录结构
```
lang
├── en # 存放英文版 JSON 文件。
├── jp # 存放日文版 JSON 文件。
├── tools # 包含所有 JSON 处理工具脚本。
│   ├── compare_json_keys.py
│   ├── merge_json.py
│   ├── sort_json.py
│   ├── split_json.py
│   ├── zip_json.py
├── README.md
├── zh.json # 中文版 JSON 文件。
└── zh.json.br # 压缩后的中文版 JSON 文件。
```

## 工具说明

### 比较 JSON 键差异
`compare_json_keys.py`
```bash
# 使用方法
python tools/compare_json_keys.py <en_file> <zh_file> [--en_output <en_output_file>] [--zh_output <zh_output_file>] [--verbose]

# 示例
python tools/compare_json_keys.py en/en.json zh.json --verbose
```
### 排序 JSON 键值对
`sort_json.py`
```bash
# 使用方法
python tools/sort_json.py <input_file> [--output <output_file>] [--verbose]

# 示例
python tools/sort_json.py en/en.json --output en_sorted.json --verbose
```

### 合并 JSON 文件
`merge_json.py`
```bash
# 使用方法
python tools/merge_json.py <input_directory> <output_file> <file_prefix> [--verbose]

# 示例
python tools/merge_json.py jp_split zh.json part_ --verbose
```
### 分割 JSON 文件
`split_json.py`
```bash
# 使用方法
python tools/split_json.py <input_file> <output_folder> [--lines_per_file LINES] [--verbose]

# 示例
python tools/split_json.py en/en.json tools/en_split --lines_per_file 100 --verbose
```

### 压缩 JSON 文件
`zip_json.py`
```bash
# 使用方法
python tools/zip_json.py <input_file> [--output <output_file>] [--verbose]

# 示例
python tools/zip_json.py zh.json --verbose
```
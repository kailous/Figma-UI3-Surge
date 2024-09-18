import re
import requests

# 要抓取的页面 URL
url = "https://www.figma.com/webpack-artifacts/assets/"

# 发送 HTTP 请求获取页面内容，忽略 SSL 证书验证
response = requests.get(url, verify=False)
html_content = response.text

# 正则表达式匹配需要的文件 URL
pattern = r"https:\/\/www\.figma\.com\/webpack-artifacts\/assets\/figma_app-[a-f0-9]{16}\.min\.en\.json\.br"

# 查找所有匹配的 URL
matches = re.findall(pattern, html_content)

# 下载匹配的文件
for match in matches:
    file_name = match.split('/')[-1]  # 从 URL 中提取文件名
    print(f"Downloading {file_name} from {match} ...")
    
    file_response = requests.get(match, verify=False)
    
    # 将文件保存到本地
    with open(file_name, 'wb') as file:
        file.write(file_response.content)
    
    print(f"{file_name} downloaded successfully!")

print("All files downloaded!")
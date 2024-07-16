# Figma-UI3-Surge
## 使用Surge脚本绕过候选名单，强制开启Figma测试版UI3。
![image](https://github.com/kailous/Figma-UI3-Surge/blob/main/img/%E5%BC%80%E5%90%AF%E6%88%90%E5%8A%9F.png?raw=true)
Figma作为一款强大的设计工具，拥有许多测试版功能供用户尝试。然而，这些功能通常只对特定用户开放。如果你想绕过候选名单并强制开启Figma的测试版UI3，可以使用Surge脚本来实现。本文将详细介绍如何使用Surge脚本完成这一操作。

### 所需工具
Surge应用：一款强大的网络调试工具，支持HTTPS拦截和修改。（自行获取）
Figma-UI3.js脚本：用于修改Figma请求响应内容的脚本 [在此右键另存](https://raw.githubusercontent.com/kailous/Figma-UI3-Surge/main/Figma-UI3.js)

### 安装步骤
1. 首先，前往Surge官方网站下载并安装Surge应用，具体过程不在赘述，完成安装后，打开Surge的 `HTTPS解密` 功能并配置所需的证书，确保Surge能够拦截和修改HTTPS请求。
![image](https://github.com/user-attachments/assets/62c095b0-0881-4680-a618-62cd3811a457)
2. 将下载好的脚本 `Figma-UI3.js` 放在配置文件目录，在配置的设置页面中可以一键直达配置文件目录。
![image](https://github.com/kailous/Figma-UI3-Surge/blob/main/img/%E6%89%BE%E5%88%B0%E8%84%9A%E6%9C%AC%E7%9B%AE%E5%BD%95.png?raw=true)
3. 打开Surge应用，进入配置文件管理（Profiles），新建一个配置文件或编辑现有的配置文件，将以下内容粘贴进去：
```
[MITM]
hostname = *.figma.com

[General]
bypass-system = false
https = true

[Script]
Figma-UI3 = type=http-response,pattern=https:\/\/.*figma_app-.*\.min\.js\.br$,requires-body=1,max-size=-1,script-path=Figma-UI3.js
```
这里注意，如果你有在使用VPN，那么这个配置应当是追加，而不是修改，你可以将文件追加到配置中去。
4. 打开 Figma 客户端，在`帮助(Help)`清理缓存，重新登陆 Figma 。
![image](https://github.com/kailous/Figma-UI3-Surge/blob/main/img/%E6%B8%85%E7%90%86%E7%BC%93%E5%AD%98.png?raw=true)
5. 愉快的使用 Figma UI3 啦～

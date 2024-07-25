# Figma-UI3-Surge
## 使用Surge脚本绕过候选名单，强制开启Figma测试版UI3。
![image](https://github.com/kailous/Figma-UI3-Surge/blob/main/img/%E5%BC%80%E5%90%AF%E6%88%90%E5%8A%9F.png?raw=true)
Figma作为一款强大的设计工具，拥有许多测试版功能供用户尝试。然而，这些功能通常只对特定用户开放。如果你想绕过候选名单并强制开启Figma的测试版UI3，可以使用Surge脚本来实现。本文将详细介绍如何使用Surge脚本完成这一操作。

### 所需工具
Surge应用：一款强大的网络调试工具，支持HTTPS拦截和修改。（自行获取）
Figma-UI3.js脚本：用于修改Figma请求响应内容的脚本 [在此右键另存](https://raw.githubusercontent.com/kailous/Figma-UI3-Surge/main/Figma-UI3.js)

### 安装步骤
#### 安装Surge
首先，前往Surge官方网站下载并安装Surge应用，具体过程不在赘述，完成安装后，打开Surge的 `HTTPS解密` 功能并配置所需的证书，确保Surge能够拦截和修改HTTPS请求。
![image](https://github.com/user-attachments/assets/62c095b0-0881-4680-a618-62cd3811a457)

注意这里https解密 一定要开启 具体的配置如上图
1. 生成新的证书后 一定要安装到系统
2. MitM 一定要写主机名 一定要写 *.figma.com
3. 选项中 三个钩子 最好要勾上

#### 下载并放置脚本
将下载好的脚本 `Figma-UI3.js` 放在配置文件目录，在配置的设置页面中可以一键直达配置文件目录。
![image](https://github.com/kailous/Figma-UI3-Surge/blob/main/img/%E6%89%BE%E5%88%B0%E8%84%9A%E6%9C%AC%E7%9B%AE%E5%BD%95.png?raw=true)
#### 编辑Surge配置文件
进入配置文件管理（Profiles），新建一个配置文件或编辑现有的配置文件，将以下内容粘贴进去。这里注意，如果你有在使用VPN，那么这个配置应当是追加，而不是修改，你可以将文件追加到配置中去。
```
[MITM]
hostname = *.figma.com

[General]
bypass-system = false
https = true

[Script]
Figma-UI3 = type=http-response,pattern=https:\/\/.*figma_app-.*\.min\.js\.br$,requires-body=1,max-size=-1,script-path=Figma-UI3.js
```

注意检查脚本配置
![image](https://github.com/kailous/Figma-UI3-Surge/blob/main/img/%E8%84%9A%E6%9C%AC%E9%85%8D%E7%BD%AE.png?raw=true)
1. 脚本路径和正则表达式注意一定保证正确。
2. HTTP脚本参数 最大数据体尺寸 选无限制。
3. 超时自己斟酌，我设置为1(小白跟着我设置就好)。

#### 清理Figma缓存并重新登录
打开 Figma 客户端，在`帮助(Help)`清理缓存，重新登陆 Figma 。
![image](https://github.com/kailous/Figma-UI3-Surge/blob/main/img/%E6%B8%85%E7%90%86%E7%BC%93%E5%AD%98.png?raw=true)
#### 享受Figma UI3
现在，您可以愉快地使用Figma UI3啦！

通过以上步骤，您可以成功绕过候选名单并强制开启Figma测试版UI3。如果有任何问题或需要进一步的帮助，请随时联系我。


### 关于新的汉化方式
以绕过开启UI3为灵感，我想到了可以通过替换figma官方语言包的方式汉化，好处就是无需修改客户端，实现全平台汉化，如果企业可以写入路由规则的话，可以整个公司汉化也不是不可能，并且实时更新，客户端可以随着官方一起更新。
目前确认了，该方案可行并且优于原本的汉化方案，我打算使用这种方案重新汉化。我重新下载了日文语料，日文语料的汉化会更准确，能避免自动化翻译时一些不该翻译的部分。
在 /lang/jp_split 中存放了分割成 364 个 json 词典文件，字数限制在可以保障 GPT-4o 一次可以完整翻译。

### 新的汉化进度
我打算利用休息时间汉化这些分割出来的json
如果你想加入贡献，请联系我。
汉化非常简单
1. 只需要将分割的 json 丢给 GPT-4o 等待汉化完成
2. 复制 GPT-4o 返回的代码，替换原本的代码即可。
3. 需要注意是要求 GPT-4o 只汉化日文部分。
4. 别忘了对比原始代码与汉化后的词典键名称 是否一致。

当前进度：
25/364 ｜ 6.87%

![image](https://github.com/kailous/Figma-UI3-Surge/blob/main/img/%E6%B1%89%E5%8C%96%E8%BF%87%E7%A8%8B.png?raw=true)
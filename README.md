# 一个提供简单Telegram群组频道信息的机器人
该项目参考[GroupHub_Bot](https://github.com/livc/GroupHub_Bot)， 并使用了
python重写。

该机器人主要功能就是提供一些常用的TG群组信息，方便使用者索引。并提供了常用的查询工具供使用者使用。

# 安装方法
安装前请确保系统中有python3.7+。 

## 安装依赖
请先安装[python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)， 注意该库当前稳定版为11.1.0， 但请务必安装版本12+，使用命令：

    $pip install python-telegram-bot==12.0.0b1 --upgrade

为了数据持久，还需要安装[TinyDB](https://github.com/msiemens/tinydb) , 使用命令：

    $pip install tinydb

其他需要的库还有 `jtyoui` `pandas` `xlrd` `jieba`。分别安装即可：

    $pip install jtyoui pandas xlrd jieba

库`jtyoui`依赖  `jieba`来分词，`pandas` 依赖 `xlrd` 读取 `.xlsx` 文件

## 配置
使用 `git clone` 获取所有文件后。找到 `botConfig.cfg` ， 打开并填写你自己的 bot token, `token` 字段必须填写。 例如（当然下面这个 `token` 是捏造的，你需要写上你自己的合法 `token` ）：

    token = 435434808:SAxfHvzSAMIn35Zu_JOukxxjUf8heXMefqw

如果你使用ss之类的代理，请将填写 `porxy` 字段： 

    proxy = https://127.0.0.1:1234/

如果你没有使用代理，这一行就不要动。

最后，在命令行下运行：

    python bot.py

即可。

# 使用方法
和该机器人对话，或者将它添加到群组中使用。

与机器人对话，使用 `/` 开头的是命令，例如，输入 `/help` ，机器人将显示帮助信息。

直接输入的文本，机器人会尝试将文本解读为搜索查询命令。目前有内置五个查询类别，分别是 `天气 百科 伴游 校花 模特` 。例如：

输入 `天气 上海`

机器人就会返回相应的天气信息。

其他未识别为这五类的文本， 将在内置的群组信息库中搜索， 并返回符合的群组信息。

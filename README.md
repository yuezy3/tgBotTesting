# 一个提供简单Telegram群组频道信息的机器人
该项目参考[GroupHub_Bot](https://github.com/livc/GroupHub_Bot)， 并使用了
python重写。

该机器人主要功能就是提供一些常用的TG群组信息，方便使用者索引。

# 安装方法
安装前请确保系统中有python3.7+。 

## 安装依赖
请先安装[python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)， 注意该库当前稳定版为11.1.0， 但请务必安装版本12+，使用命令：

    $pip install python-telegram-bot==12.0.0b1 --upgrade

为了数据持久，还需要安装[TinyDB](https://github.com/msiemens/tinydb) , 使用命令：

    $pip install tinydb


## 配置
使用 `git clone` 获取所有文件后。找到 `botConfig.cfg` ， 打开并填写你自己的 bot token, `token` 字段必须填写。 例如（当然下面这个 `token` 是捏造的，你需要写上你自己的合法 `token` ）：

    token = 435434808:SAxfHvzSAMIn35Zu_JOukxxjUf8heXMefqw

如果你使用ss之类的代理，请将填写 `porxy` 字段： 

    proxy = https://127.0.0.1:1234/

如果你没有使用代理，这一行就不要动。

最后，在命令行下运行：

    python bot.py

即可。

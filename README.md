# 一个提供简单Telegram群组频道信息的机器人
该项目参考[GroupHub_Bot](https://github.com/livc/GroupHub_Bot)， 并使用了
python重写。

该机器人主要功能就是提供一些常用的TG群组信息，方便使用者索引。

# 安装方法
安装前请确保系统中有python3.7+。 

## 依赖
请先安装[python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)， 注意该库当前稳定版为11.1.0， 但请务必安装版本12+，使用命令：

    $pip installpython-telegram-bot==12.0.0b1 --upgrade

## 安装
使用 `git clone` 获取所有文件。打开 `bot.py` 找到以下行：

    request_kwargs={'proxy_url':'https://127.0.0.1:1080/'}

修改 `https://127.0.0.1:1080/` 为你自己的代理地址，如果你没有使用ss之类的代理，请将本行全部注释或删除。

找到以下行：

    updater = Updater(token='435434808:SAxfHvzSAMIn35Zu_JOukxxjUf8heXMefqw',

将 `435434808:SAxfHvzSAMIn35Zu_JOukxxjUf8heXMefqw` 替换为你自己的token即可。(该token必须替换为你自己的token)

最后，在命令行下运行：
    python bot.py

即可。

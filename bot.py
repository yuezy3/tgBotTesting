#***********************big variable def*********************
start_string = """GroupHub致力于收录tg中文圈优质群组。\n
				项目地址: https://github.com\n
				Bot: @GroupHub_bot\n
				广播站: @GroupHub\n
				交流群: @GroupHub_Chat\n
				群组收录更新: 将【群组名、分类、链接】发送到https://github.com/livc/GroupHub_Bot\n
				BUG提交/功能建议: https://github.com/livc/GroupHub_Bot/issues\n\n
				/groups 查询群组"""
keyMarkups = [ ["ACG", "软件","科学上网"],
               ["linux", "社区", "Geek"] ,
               ["编程",  "城市", "书影音"],
               ["政治", "资源", "其他"]
             ]

#************************util functions and classes*******************
import json
import base64
def fetchGroupDate(jsonpath='bot_groups.json'):
    myjson = ''
    with open(jsonpath,'r') as f:
        myjson = json.load(f)
    decodedDict = {}
    for k,v in myjson.items():
        newarray = []
        for link in v:
            try:
                newarray.append({"TEXT": base64.b64decode(link["TEXT"]).decode()})
            except:
                print(link["TEXT"])
        decodedDict[k] = newarray
    return decodedDict

from telegram.ext import BaseFilter
class FilterButton(BaseFilter):
    def __init__(self, text_list):
        super(BaseFilter,self).__init__()
        self.text_list = text_list
    def filter(self, message):
        return message.text in self.text_list


#***************perpare usefull variables********************************
from telegram.ext import Updater
updater = Updater(token='839434408:AAFfHvzSUMIn35Zu_JOukSvjUf8heXMefqw',
                  request_kwargs={'proxy_url':'https://127.0.0.1:1080/'},
                  use_context=True)
dispatcher = updater.dispatcher
# make the messagae filter
filter_button = FilterButton([i for sublist in keyMarkups for  i in sublist ])
groupDate = fetchGroupDate()
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)



#===========================================
def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, 
    text=start_string)
from telegram import ReplyKeyboardMarkup
def replyMarkUp(update,context):
    context.bot.send_message(chat_id=update.message.chat_id,
    text="what do you want seek",
    reply_markup = ReplyKeyboardMarkup(keyboard=keyMarkups))
from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
button_handler = CommandHandler('groups', replyMarkUp)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(button_handler)

#==============================================
def needGroup(update, context):
    group = update.message.text
    resp = ''
    for i in groupDate[group]:
        resp = resp + i['TEXT'] + '\n'
    
    context.bot.send_message(chat_id=update.message.chat_id, text=resp)
def echo(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text=update.message.text)
from telegram.ext import MessageHandler, Filters
group_handler = MessageHandler(filter_button, needGroup)
echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(group_handler)
dispatcher.add_handler(echo_handler)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++
updater.start_polling()













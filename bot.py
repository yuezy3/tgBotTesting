#***********************big variable def*********************
start_string = """中文圈优质TG群组\n
				项目地址: （填写你的项目地址）\n
				Bot: （填写你的Bot名称：@botname）\n
				广播站: （填写你的广播站）\n
				交流群: （填写你的交流群）\n
				群组收录更新: 将【群组名、分类、链接】发送到（填写你的联系所用地址）\n
				BUG提交/功能建议: （填写你的联系所用地址）\n\n
				/groups 查询群组"""
btSource = [ [{"text":"查询群组","callback_data":"groups"},
              {"text":"如何使用","callback_data":"help"}],  ]  #inline button: list of list
keyMarkups = [ ["ACG", "软件","科学上网"],
               ["linux", "社区", "Geek"] ,
               ["编程",  "城市", "书影音"],
               ["政治", "资源", "其他"]
             ]

#************************util functions and classes*******************
import json
import base64
import os.path
def fetchGroupdata(jsonpath='bot_groups.json'):
    myjson = ''
    script_path = os.path.dirname(os.path.abspath( __file__ ))
    absjsonpath = os.path.join(script_path, jsonpath)
    with open(absjsonpath,'r') as f:
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
updater = Updater(token='435434808:SAxfHvzSAMIn35Zu_JOukxxjUf8heXMefqw',
                  request_kwargs={'proxy_url':'https://127.0.0.1:1080/'},
                  use_context=True)
dispatcher = updater.dispatcher
# make the messagae filter
filter_button = FilterButton([i for sublist in keyMarkups for  i in sublist ])
groupdata = fetchGroupdata()
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


#===========================================
from telegram import InlineKeyboardMarkup
from telegram import InlineKeyboardButton
def start(update, context):
    inline_buttons = [[InlineKeyboardButton(**i) for i in bs ] for bs in btSource]
    context.bot.send_message(chat_id=update.message.chat_id, 
                             text=start_string, 
                             reply_markup=InlineKeyboardMarkup(inline_keyboard = inline_buttons))
from telegram import ReplyKeyboardMarkup
def replyMarkUp(update,context):
    context.bot.send_message(chat_id=update.message.chat_id,
    text="点击你要查看的分类\n",
    reply_markup = ReplyKeyboardMarkup(keyboard=keyMarkups))
from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
button_handler = CommandHandler('groups', replyMarkUp)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(button_handler)

#============================================
from telegram.ext import CallbackQueryHandler
def start_inline_callback(update,context):
    data = update.callback_query.data # inline button associated data
    original_message_text = update.callback_query.message.text
    if data == "groups":
        update.callback_query.edit_message_text(original_message_text + "\n\n点击 /groups 查看分组\n")
    if data == "help":
        category = '\n'.join([ '  |  '.join(ls)  for ls in keyMarkups])
        update.callback_query.edit_message_text("直接输入下列词语查看分类：\n"+
                                                category+"\n或者点击 /groups 查看分组\n ")
    update.callback_query.answer()
start_inline_callback_handler = CallbackQueryHandler(start_inline_callback)
dispatcher.add_handler(start_inline_callback_handler)

#==============================================
def needGroup(update, context):
    group = update.message.text
    resp = ''
    for i in groupdata[group]:
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
updater.idle()












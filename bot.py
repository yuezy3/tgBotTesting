#***********************big variable def*********************
start_string = """中文圈优质TG群组\n
				项目地址: （填写你的项目地址）\n
				Bot: （填写你的Bot名称：@botname）\n
				广播站: （填写你的广播站）\n
				交流群: （填写你的交流群）\n
				群组收录更新: 将【群组名、分类、链接】发送到（填写你的联系所用地址）\n
                直接使用 /a 群组的描述 群组地址 向机器人提交群组信息 \n
				BUG提交/功能建议: （填写你的联系所用地址）\n\n
				/groups 查询群组分类"""
help_string = "直接输入需要查询的关键字可以搜索群组\n" + \
              "使用 /a 群组的描述 群组地址 \n\n" +  \
              "可以向机器人添加群组信息\n" +  \
              "点击 /groups 查看已有群组的分类\n " +  \
              "点击 /help 显示这条帮助信息"
btSource = [ [{"text":"查询群组分类","callback_data":"groups"},
              {"text":"如何使用","callback_data":"help"}],  ]  #inline button: list of list
keyMarkups = [ ["/g ACG", "/g 软件","/g 科学上网"],
               ["/g linux", "/g 社区", "/g Geek"] ,
               ["/g 编程",  "/g 城市", "/g 书影音"],
               ["/g 政治", "/g 资源", "/g 其他"]
             ]

#************************util functions and classes*******************
import json
import base64
import os.path
import dbport, botconfig
from telegram.ext import BaseFilter
class FilterButton(BaseFilter):
    def __init__(self, text_list):
        super(BaseFilter,self).__init__()
        self.text_list = text_list
    def filter(self, message):
        return message.text in self.text_list


#***************perpare usefull variables********************************
from telegram.ext import Updater
updater = Updater(token=botconfig.token,
                  request_kwargs={'proxy_url':botconfig.proxy}if botconfig.proxy else {},
                  use_context=True)
dispatcher = updater.dispatcher
# make the messagae filter
filter_button = FilterButton([i for sublist in keyMarkups for  i in sublist ])
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
def help(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, 
                             text=help_string)
from telegram import ReplyKeyboardMarkup
def replyMarkUp(update,context):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="点击你要查看的分类\n",
                             reply_markup = ReplyKeyboardMarkup(keyboard=keyMarkups))
def fetchGroup(update,context):
    groupName = context.args[0]
    answer = '类别为{}的群组有：\n'.format(groupName)
    groups = dbport.category(groupName)
    if len(groups) == 0: # no named group found:
        answer = answer + "0个结果 \n" + "请尝试使用其他群组类别。\n" +"或使用 /help 查看帮助信息\n"
    else:
        for i in dbport.category(groupName):
            answer = answer + i['intro'] + '  ' + i['addr'] + '\n'
    context.bot.send_message(chat_id=update.message.chat_id, 
                             text=answer)
def addGroup(update,context):
    item = context.args
    dbport.addItem({'intro':' '.join(item[:-1]),'addr':item[-1]})
    context.bot.send_message(chat_id=update.message.chat_id, 
                             text="已添加群组信息\n")
from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
help_handler = CommandHandler('help', help)
button_handler = CommandHandler('groups', replyMarkUp)
group_handler = CommandHandler('g', fetchGroup)
add_handler = CommandHandler('a', addGroup)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(button_handler)
dispatcher.add_handler(group_handler)
dispatcher.add_handler(add_handler)

#============================================
from telegram.ext import CallbackQueryHandler
def start_inline_callback(update,context):
    data = update.callback_query.data # inline button associated data
    original_message_text = update.callback_query.message.text
    if data == "groups":
        update.callback_query.edit_message_text(original_message_text + "\n\n点击 /groups 查看分组\n")
    if data == "help":
        #category = '\n'.join([ '  |  '.join(ls)  for ls in keyMarkups])
        update.callback_query.edit_message_text(help_string)
    update.callback_query.answer()
start_inline_callback_handler = CallbackQueryHandler(start_inline_callback)
dispatcher.add_handler(start_inline_callback_handler)

#==============================================
import plugSearch
def plainSearch(update, context):
    searchString = update.message.text
    msg = "你输入的是 {} \n".format(searchString)
    key = searchString.strip().split()[0]
    sstirng = ''.join(searchString.strip().split()[1:])
    if key in plugSearch.exportKey:
        msg = msg + plugSearch.exportKey[key](sstirng)
    else:
        searchResult = dbport.search(searchString)
        if len(searchResult) == 0 :#no result
            msg = "你输入的是 {} \n".format(searchString) + \
                  "但是没有找到任何匹配项目" + \
                  "使用其他文字搜索或者使用 /help 命令查看帮助"
        else:
            for i in searchResult:
                msg = msg + i['intro'] + '  ' + i['addr'] + '\n'
    context.bot.send_message(chat_id=update.message.chat_id, 
                             text=msg)
def welcome(update, context):
    msg = '欢迎: \n'
    for member in update.message.new_chat_members:
        msg = msg + member.username + '\n'
    context.bot.send_message(chat_id=update.messagae.chat_id, text = msg)
from telegram.ext import MessageHandler, Filters
search_handler = MessageHandler(Filters.text, plainSearch)
welcome_handler = MessageHandler(Filters.status_update.new_chat_members, welcome)
dispatcher.add_handler(search_handler)
dispatcher.add_handler(welcome_handler)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++
updater.start_polling()
updater.idle()




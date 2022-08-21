from bots import bot,chat_id
from telegram import Update
from telegram.ext import CallbackContext

a={}

def add(update:Update,context:CallbackContext):
    user_text=update.message.text
    # user_text0=user_text.split(' ')[0]
    user_text1=user_text.split(' ')[1]
    user_text2=user_text.split(' ')[2]
    # if user_text0=='/add':
    a[user_text1]=user_text2

def handeler(update:Update,context:CallbackContext):
    user_text=update.message.text
    for i in a.keys():
        if user_text==i:
            bot.sendMessage(chat_id=chat_id,text=a.get(i))

def clear(update:Update,context:CallbackContext):
    global a
    a={}  
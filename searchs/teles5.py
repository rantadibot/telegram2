from telegram import Update
from bots import token
from telegram.ext import Updater,MessageHandler,Filters,CommandHandler,CallbackContext
from imgs import get_pic
from add2 import add,clear,handeler
from moef2 import moefs
from msit2 import msits
from me2 import mes
from mois2 import mois
from mcst2 import mcst
def help(update:Update, context:CallbackContext):
    update.message.reply_text("/help : 사용 명령어 표시\n/img sth: 이미지 보내기\n/moef name: 기재부 검색\n/msit name: 과기부 검색\n/me name: 환경부 검색\n/mois name: 행안부 검색\n/mcst name: 문체부 검색") 

def img(update:Update,context:CallbackContext):
    user_text=update.message.text
    user_text1=user_text.split(' ')[1]
    for i in get_pic(user_text1):
        update.message.reply_photo(i)
            
def new_member(update:Update,context:CallbackContext):
    names=update.message.from_user.last_name+' '+update.message.from_user.first_name
    for member in update.message.new_chat_members:
        update.message.reply_text(f'{names}님이 {member.username}님을 초대하였습니다')

def named(update:Update,context:CallbackContext):
    names=update.message.from_user.last_name+' '+update.message.from_user.first_name
    title=update.message.chat.title
    update.message.reply_text(f'{title} 방의 {names}님이시네요. 맞춰서 놀라셨죠?')
            
def main():
    updater=Updater(token=token,use_context=True)
    dispatcher=updater.dispatcher
    
    help_handler=CommandHandler('help', help)
    dispatcher.add_handler(help_handler)
    
    add_handlers=CommandHandler('add', add)
    dispatcher.add_handler(add_handlers)
    
    named_handler=CommandHandler('name', named)
    dispatcher.add_handler(named_handler)
    
    img_handler=CommandHandler('img', img)
    dispatcher.add_handler(img_handler)
    
    clear_handler=CommandHandler('clear', clear)
    dispatcher.add_handler(clear_handler)
    
    moef_handler=CommandHandler('moef', moefs)
    dispatcher.add_handler(moef_handler)

    msit_handler=CommandHandler('msit', msits)
    dispatcher.add_handler(msit_handler)
        
    me2_handler=CommandHandler('me', mes)
    dispatcher.add_handler(me2_handler)
    
    mois_handler=CommandHandler('mois', mois)
    dispatcher.add_handler(mois_handler)
    
    mcst_handler=CommandHandler('mcst', mcst)
    dispatcher.add_handler(mcst_handler)
        
    new_handler=MessageHandler(Filters.status_update.new_chat_members, new_member)
    dispatcher.add_handler(new_handler)
           
    echo_handler=MessageHandler(Filters.text,handeler)
    dispatcher.add_handler(echo_handler)    

    updater.start_polling(timeout=5,clean=True)
    updater.idle()
    
if __name__=='__main__':
    main()
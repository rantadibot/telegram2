from bots import token
from telegram import Update
from carrot import carrot
from carrot2 import carrot2
from olds import olds
from telegram.ext import Updater,CommandHandler,CallbackContext

def help(update:Update, context:CallbackContext):
    update.message.reply_text("/help : 사용 명령어 표시\n/old sth: 중고나라에서 검색\n/carrot sth: 당근나라 검색\n/carrot2 sth: 당근나라 검색(이미지 추가)") 

def main():
    updater = Updater(token, use_context=True)
    dispatcher=updater.dispatcher

    help_handler=CommandHandler('help', help)
    dispatcher.add_handler(help_handler)
    
    old_handlers=CommandHandler('old', olds)
    dispatcher.add_handler(old_handlers)
    
    carrot_handler=CommandHandler('carrot', carrot)
    dispatcher.add_handler(carrot_handler)

    carrot2_handler=CommandHandler('carrot2', carrot2)
    dispatcher.add_handler(carrot2_handler)

    updater.start_polling(timeout=20, clean=True)
    updater.idle()    

if __name__=='__main__':
    main()
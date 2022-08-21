from telegram import Bot

token='1922693876:AAHvM7oy1Caz_rbL0FAXZ0uu9hlRiPdQplU'
bot=Bot(token=token)
chat_id  = bot.getUpdates()[-1].message.chat.id
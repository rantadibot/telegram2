from telegram import Bot

token='5397535361:AAHWodYnIdtTvyMLF6j-q5KqVR_QQQ38WTQ'
bot=Bot(token=token)
chat_id  = bot.getUpdates()[-1].message.chat.id
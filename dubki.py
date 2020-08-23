import telebot

bot = telebot.TeleBot('1206644046:AAEF6f7NPlNR7XbxbPi5ctPnVs2Xw84_rLM')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

bot.polling()
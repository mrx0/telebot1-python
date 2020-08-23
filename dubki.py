import telebot
import datetime
import schedule
import time

#массив для названия месяцев в нужном падеже
a = ['января.', 'февраля.', 'марта.', 'апреля.', 'мая.', 'июня.', 'июля.', 'августа.', 'сентября.', 'октября.', 'ноября.', 'декабря.']

TOKEN = '1206644046:AAEF6f7NPlNR7XbxbPi5ctPnVs2Xw84_rLM'

bot = telebot.TeleBot(TOKEN)

group_id = '-1001362717183'

# now = datetime.datetime.now()
# a1 = datetime.datetime(1980, 8, 22)
# delta1 = now - a1

BDates = {'1-28':'Вилкова', '8-19':'Тюсина', '7-26':'Чивильдеева', '6-17':'Зубавленки', '6-10':'Харькова', '4-17':'Шубина', '1-17':'Антошки', '12-13':'Фомича', '12-10':'Леймана', '10-12':'Тышова'}
PDates = {'9-3':'И снова третья сентябряяяяяяЯЯЯЯ!!!', '1-1':'C Новм годм кароч'}

#обработка команды start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Сообщение инструкция')
#
# #обработка и сообщение о дате дня рождения.
# @bot.message_handler(content_types=['text'])
#
# # def send():
# #     bot.send_message(group_id, 'Как скажешь, Андрей, много не буду ;)')
#
#
# #проверка даты и отправка сообщения
# def send1():
#     # print(datetime.datetime.now())
#     # if a1.month == now.month and a1.day == now.day:
#         # bot.send_message(group_id,'Сегодня день рождения у Никого.' + 'Ему исполнилось ' +str(delta1.days // 365 ) +' лет.' )
#
#     now = datetime.datetime.now()
#     # print( str(now.month)+'-'+str(now.day) )
#
#     if str(now.month)+'-'+str(now.day) in BDates:
#         # print(BDates[str(now.month)+'-'+str(now.day)])
#         bot.send_message(group_id, 'Кстати, сегодня у ' + BDates[str(now.month)+'-'+str(now.day)] + ' ДР')
#
# def send2():
#     # print(datetime.datetime.now())
#     # if a1.month == now.month and a1.day == now.day:
#         # bot.send_message(group_id,'Сегодня день рождения у Никого.' + 'Ему исполнилось ' +str(delta1.days // 365 ) +' лет.' )
#
#     now = datetime.datetime.now()
#     # print( str(now.month)+'-'+str(now.day) )
#
#     if str(now.month)+'-'+str(now.day) in PDates:
#         # print(BDates[str(now.month)+'-'+str(now.day)])
#         bot.send_message(group_id, '' + PDates[str(now.month)+'-'+str(now.day)] + '')
#
#
# # спланируй.каждые(N).секунд.сделать(работу)
# # schedule.every(2).minutes.do(send)
# #периодичность проверки даты. Каждый день в указанное время.
# schedule.every().day.at("13:00").do(send1)
# schedule.every().day.at("00:00").do(send2)
#
# while True:
#     # print(a1)
#     schedule.run_pending()
#     time.sleep(1)

bot.polling(none_stop=True)
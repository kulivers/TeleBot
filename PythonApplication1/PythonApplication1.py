# -*- coding: utf-8 -*-

import sys
print (sys.path)
#sys.path.append(", ")
sys.path.append("D:\\libs\\python-telegram-bot-master")
print ('\n')
print (sys.path)

#    ВНИМАНИЕ!!! В СТУДИИ НЕ РАБОТАЕТ ПОЧЕМУ ТО, НО КОГДА Я ПЫТАЛСЯ СДЕЛАТЬ ЧЕРЕЗ NOTEPAD И CMD ВСЕ БЫЛО ОК, А ЕЩЕ ЕСЛИ ПРОБОВАТЬ ЗАПУСТИТЬ НАДО СВОЙ API ВВЕСТИ В 11 СТРОКЕ
from telegram.ext import updater, commandhandler, messagehandler, filters
updater = updater(token='748241724:AAEVNa8haMmAhNwjV5aUiOGEQDiOQhu4VS8') # токен api к telegram, его можно взять у botFather
dispatcher = updater.dispatcher

def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Привет, давай пообщаемся?')
def textMessage(bot, update):
    response = 'Получил Ваше сообщение: ' + update.message.text
    bot.send_message(chat_id=update.message.chat_id, text=response)
    # Хендлеры
start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)
# Добавляем хендлеры в диспетчер
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)
# Начинаем поиск обновлений
updater.start_polling(clean=True)

# Останавливаем бота, если были нажаты Ctrl + C
updater.idle()
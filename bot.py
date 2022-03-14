# -*- coding: utf-8 -*-

import pyowm
import config
import datetime
import telebot
import time

from telebot import types


from pyowm import OWM
owm = pyowm.OWM('1884e6b6d5605fee686cf449ac8b1e54', language= 'RU')
bot = telebot.TeleBot(config.token)


#Месяц
today = datetime.datetime.today()
mount = ['Января', 'Февраля', 'Марта', 'Апреля', 'Мая', 'Июня', 'Июля', 'Августа', 'Сентября', 'Октября', 'Ноября', 'Декабря']
mounth_real = int(today.strftime("%m"))

#день и месяц текстом
day = today.strftime("%A")
if day == 'Monday':
    day = 'понедельник'
elif day == 'Tuesday':
    day = "вторник"
elif day == 'Wednesday':
    day = "среда"
elif day == 'Thursday':
    day = "четверг"
elif day == 'Friday':
    day = "пятница"
elif day == 'Saturday':
    day = "суббота"
elif day == 'Sunday':
    day = "Воскресенье"


observation = owm.weather_at_place('Москва')
w = observation.get_weather()
temp = w.get_temperature('celsius')['temp']


text1 = ('Сегодня '+ day + ' ,' + today.strftime("%d") + ' ' + mount[mounth_real % 12] + ' ' + today.strftime("%Y") + ' г.')
text2 = ('Погода в Москве хорошая, ' + w.get_detailed_status()+ ' ' + str(round(temp)) + ' °C')


@bot.message_handler(content_types=["text"])
def message(message):
    bot.send_message(message.chat.id, "Привет. Это генератор отчётов.")
    time.sleep(2)
    bot.send_message(message.chat.id, text1)
    time.sleep(1)
    bot.send_message(message.chat.id, text2)
    time.sleep(2)

    markup = telebot.types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('ДА ', callback_data='1')
    button2 = types.InlineKeyboardButton('НЕТ ', callback_data='2')
    markup.row(button1, button2)
    bot.send_message(message.from_user.id, f"Вы хотите сгенерировать план на сегодня и отчёт за вчера?", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == '1':
        a = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, 'Что', reply_markup=a)
        bot.send_message(call.message.chat.id, 'Продолжаем разговор')

    elif call.data == '2':
        bot.send_message(call.message.chat.id, 'Тогда ПОКА! Заполняй свой отчёт сам.')


    


bot.polling(none_stop=True, interval=0)

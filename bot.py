# -*- coding: utf-8 -*-

import pyowm
import config
import datetime
import telebot
import time
import random


stations = ['Бейские Копи', 'Углесборочная', 'Барбаров', '1553 км', 'Б/п 5647', 'Выдрино', 'Горхон-Затяжной',
                    'Дивизионная',
                    'Заудинский', 'Звездная', 'Камышет', 'Кедровая', 'Клюевка', 'Куйтун', 'Мысовая', 'Онохой',
                    'Перевоз', 'Посольская',
                    'Рудногорск', 'Селенга', 'Слюдянка-2', 'Таловка', 'Танхой', 'Татаурово', 'Тимлюй', 'Ук', 'Хужир',
                    'Шалуты', 'Ардаши',
                    'Аэропорт', 'Вахитово', 'Восстание', 'Глазов', 'Гороховец', 'Горький сорт.', 'Каликино',
                    'Комбинат - Тихорецкая',
                    'Линда', 'Новки', 'Петушки', 'Поздино', 'Поздино - Полой', 'Просница', 'Просница - Бумкомбинат',
                    'Свияжск', 'Тереховицы-Второво',
                    'Тихорецкая', 'Федулово-Новки', 'Юбилейная - Комбинат', 'Амур', 'Барановский - Раздольное',
                    'Гвоздевский', 'Глухариный',
                    'Заячий', 'Иванокит', 'Икура', 'Кипарисово-Раздольное', 'Комсомольск сорт.', 'Комсомольская',
                    'Кувыкта', 'Кутыкан', 'Морошка',
                    'Николаевка', 'Первая речка', 'Побожий', 'Раздольное', 'Сосновый', 'Тында', 'Федосеев', 'Фридман',
                    'Хмыловский', 'Баляга',
                    'Декабристы', 'Домна', 'Кадала - Черновская', 'Кадала', 'Куэнга', 'Лесная', 'Улягир', 'Усть-Пера',
                    'Черновская', 'Черновская - Кадала',
                    'Яблоновая', 'Карбышево-1', 'Кемерово', 'Кокошино', 'Пикетное', 'Сыропятское', 'Укладочный',
                    'Чулымская', 'Юрга-1', 'Жетыген-Алтынколь',
                    'Егинсу', 'Жетыген', 'Узень', 'уч. Жетыген-Алтынколь', 'Гвардейск', 'Дзержинская Новая', 'Знаменск',
                    'Луговое-Новое', 'Озерки новые',
                    'Абакан', 'Заозерная', 'Зерцалы', 'Иланская', 'Ирба', 'Камала', 'Красный Кордон', 'Мана',
                    'п.п. 531км', 'Предметкино', 'Сорокино',
                    'Суслово', 'Уяр', 'Щетинкино', 'Звезда', 'Леонидовка', 'Пенза 2', 'Рузаевка', 'Черниковка',
                    'Авиационная', 'Александров-2',
                    'Бекасово-сорт.', 'Бельково', 'Бельково - Киржач', 'Березка', 'Давыдово', 'Дрезна', 'Жёлтиково',
                    'Ивантеевка', 'Иванцево',
                    'Канатчиково', 'Карабаново - Бельково', 'Киржач', 'Кожухово', 'Космос', 'Костино', 'Кусково',
                    'Лефортово-Черкизово',
                    'Монино', 'Москва-Товарная-Смоленская', 'Наугольный', 'Наугольный - Желтиково', 'Подмосковная',
                    'Подольск', 'Покров',
                    'Покров - Петушки', 'Реутово', 'Угрешская', 'Усад', 'Усад - Пост 97 км', 'Фрязино', 'Калашниково',
                    'Угловка', 'В.Баскунчак',
                    'Нефтяная', 'Пост 6км', 'Трусово', 'Шунгули', 'Гагарский-Мезенский', 'Демьянка', 'Кокшаровский',
                    'Мезенский-Баженово',
                    'Мезенский', 'Менделеево', 'Перегон', 'Пермь парк Г', 'Путевка', 'Пышминская', 'Свердловск-сорт.',
                    'Тобольск', 'Чепца',
                    'Шабуничи', 'Шарташ', 'Беклемишево-Рязанцево', 'Берендеево', 'Деболовская', 'Итларь', 'Рязанцево',
                    'Рязанцево - Шушково',
                    'Шушково - Берендеево', 'Козырьки', 'Джам- Айритам', 'Айритам - Алатун', 'Бактрия-Термез', 'Гузар',
                    'Мараканд - Гумбаз',
                    'Улус - Джам', 'Жаркурган - Бактрия', 'Камаши', 'Кашкадарья - Карши', 'Нигуз - Кашкадарья', 'Китаб',
                    'Кумкурган-Сурхан',
                    'Нигуз - Алатун', 'Разъезд 165 - Жаркурган', 'Сурхан - Разъезд 165', 'Танхоз', 'Гумбаз - Улус',
                    'Яккабог',
                    'Вольный - Сахновщина', 'Гражданский', 'Кегичевка - Вольный', 'Модуль 165 км - Гражданский',
                    'Орелька - Модуль 165 км',
                    'Пост 136 км - Пост 146 км', 'Пост 146 км - Орелька', 'Сахновщина - Пост 136 км', 'Разъезд 36',
                    'Ольха-Абрамовка',
                    'Ольха-Абрамовка', 'Абрамовка-Таловая', 'Евдаково', 'Зайцевка', 'Придонская-Икорец', 'Кантемировка',
                    'Лиски', 'Ольха',
                    'Подгорное', 'Сергеевка', 'Сомово-Отрожка', 'Иковка', 'Качусово-Каргополье',
                    'Кособродск'', ''Миасс', 'Твердыш-Окуневка',
                    'Окуневка-Кособродск', 'Просвет-Галкино', 'Твердыш', 'Челябинск Главный парк "П"',
                    'Челябинск парк А', 'Шагол',
                    'Шадринск', 'Алдан', 'Амга', 'Болотный', 'Денисовский', 'Кердем', 'Кюргелях', 'Нижний Бестях',
                    'Томмот']

work = ['Предрелизная проверка', 'Разработка ПО АРМ', 'АПК-ДК', 'Корректировка ПО АРМ', 'Разработка ДЦ',
                'Разработка ПО АРМ', 'Корректировка ДЦ']

text = ["""========================================================================================================================================================================================================
        = Поле "Объект:" должно содержать название станции/участка и название дороги                                                                                                                           =
        = Поле "Задача:" должно содержать номер 1-го связанного с задачей дефекта или текстовое описание при отсутствии дефекта, в последнем случае описание дополняется ссылкой на автора поставленной задачи =
        = Поле "%готовности:" должно содержать реальный процент готовности по указанной задаче                                                                                                                 =
        = При достижении 100% готовности задача удаляется из списка работ на следующий день                                                                                                                    =
        = Поле "%загрузки:" должно содержать реальный процент загруженности в течении дня по указанной задаче, сумма процентов по всем задачам должна быть равна 100%                                          =
        = Поле "Дата_окончания:" должно содержать планируемую дату окончания активностей по задаче                                                                                                             =
        = Поле "Активность_тестов:" должно содержать количество правок по дефекту в течении дня                                                                                                                =
        = Поле "Причина_неисполнения:" в случае превышения планируемых сроков или при наличии обстоятельств непреодолимой силы должно содержать описание причины                                               =
        ========================================================================================================================================================================================================"""]

text2 = ["""========================================================================================================================================================================================================
        = Объект:                              = Задача:                        = %готовности: = %загрузки: = Дата_окончания: = Активность_тестов:  =   Причина_неисполнения:                                  =
        ========================================================================================================================================================================================================"""]





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


    
    
    
    
    
    
    
            file = open(r"familiya.txt", "w")

        
        from datetime import date, timedelta
        yesterday = date.today() - timedelta(days=1)

        a1 = random.choice(stations)
        a2 = random.choice(stations)
        a3 = random.choice(stations)
        a4 = random.choice(stations)

        b1 = random.choice(work)
        b2 = random.choice(work)
        b3 = random.choice(work)
        b4 = random.choice(work)

        c1 = str(int(round(random.randint(1, 100) / 5.0) * 5.0))
        c2 = str(int(round(random.randint(1, 100) / 5.0) * 5.0))
        c3 = str(int(round(random.randint(1, 100) / 5.0) * 5.0))
        c4 = str(int(round(random.randint(1, 100) / 5.0) * 5.0))

        d1 = round(random.randint(1, 100) / 5) * 5
        d2 = round(random.randint(1, 100) / 5) * 5
        d3 = round(random.randint(1, 100) / 5) * 5
        d4 = round(random.randint(1, 100) / 5) * 5

        # вычисляем случайное число в сумме не больше 100
        zadachi = 4
        schetchik = random.randint(1, zadachi)

        if schetchik == 1:
            d1 = d1
            d2 = round(random.randint(1, 100 - d1) / 5) * 5
            d3 = round(random.randint(1, d2) / 5) * 5
            d4 = round(random.randint(1, d3) / 5) * 5

        if schetchik == 2:
            d2 = d2
            d1 = round(random.randint(1, 100 - d2) / 5) * 5
            d3 = round(random.randint(1, d1) / 5) * 5
            d4 = round(random.randint(1, d3) / 5) * 5

        if schetchik == 3:
            d3 = d3
            d1 = round(random.randint(1, 100 - d3) / 5) * 5
            d2 = round(random.randint(1, d1) / 5) * 5
            d4 = round(random.randint(1, d2) / 5) * 5

        if schetchik == 4:
            d4 = d4
            d1 = round(random.randint(1, 100 - d4) / 5) * 5
            d2 = round(random.randint(1, d1) / 5) * 5
            d3 = round(random.randint(1, d2) / 5) * 5

        print(d1, d2, d3, d4)

        # измеряем количество символов
        lena1 = len(a1)
        lena2 = len(a2)
        lena3 = len(a3)
        lena4 = len(a4)

        if b1 == 'Предрелизная проверка':
            c1 = "\t\t\t\t\t" + c1
        if b2 == 'Предрелизная проверка':
            c2 = "\t\t\t\t\t" + c2
        if b3 == 'Предрелизная проверка':
            c3 = "\t\t\t\t\t" + c3
        if b4 == 'Предрелизная проверка':
            c4 = "\t\t\t\t\t" + c4

        if b1 == 'Разработка ПО АРМ':
            c1 = "\t\t\t\t\t\t" + c1
        if b2 == 'Разработка ПО АРМ':
            c2 = "\t\t\t\t\t\t" + c2
        if b3 == 'Разработка ПО АРМ':
            c3 = "\t\t\t\t\t\t" + c3
        if b4 == 'Разработка ПО АРМ':
            c4 = "\t\t\t\t\t\t" + c4

        if b1 == 'АПК-ДК':
            c1 = "\t\t\t\t\t\t\t\t\t" + c1
        if b2 == 'АПК-ДК':
            c2 = "\t\t\t\t\t\t\t\t\t" + c2
        if b3 == 'АПК-ДК':
            c3 = "\t\t\t\t\t\t\t\t\t" + c3
        if b4 == 'АПК-ДК':
            c4 = "\t\t\t\t\t\t\t\t\t" + c4

        if b1 == 'Корректировка ПО АРМ':
            c1 = "\t\t\t\t\t" + c1
        if b2 == 'Корректировка ПО АРМ':
            c2 = "\t\t\t\t\t" + c2
        if b3 == 'Корректировка ПО АРМ':
            c3 = "\t\t\t\t\t" + c3
        if b4 == 'Корректировка ПО АРМ':
            c4 = "\t\t\t\t\t" + c4

        if b1 == 'Разработка ДЦ':
            c1 = "\t\t\t\t\t\t\t" + c1
        if b2 == 'Разработка ДЦ':
            c2 = "\t\t\t\t\t\t\t" + c2
        if b3 == 'Разработка ДЦ':
            c3 = "\t\t\t\t\t\t\t" + c3
        if b4 == 'Разработка ДЦ':
            c4 = "\t\t\t\t\t\t\t" + c4

        if b1 == 'Разработка ПО АРМ':
            c1 = "" + c1
        if b2 == 'Разработка ПО АРМ':
            c2 = "" + c2
        if b3 == 'Разработка ПО АРМ':
            c3 = "" + c3
        if b4 == 'Разработка ПО АРМ':
            c4 = "" + c4

        if lena1 == 1 or lena1 == 2 or lena1 == 3:
            a1 = a1 + "\t\t\t\t\t\t\t\t\t"

        if lena1 == 4 or lena1 == 5 or lena1 == 6 or lena1 == 7:
            a1 = a1 + "\t\t\t\t\t\t\t\t"

        if lena1 == 8 or lena1 == 9 or lena1 == 10 or lena1 == 11:
            a1 = a1 + "\t\t\t\t\t\t\t"

        if lena1 == 12 or lena1 == 13 or lena1 == 14 or lena1 == 15:
            a1 = a1 + "\t\t\t\t\t\t"

        if lena1 == 16 or lena1 == 17 or lena1 == 18 or lena1 == 19:
            a1 = a1 + "\t\t\t\t\t"

        if lena1 == 20 or lena1 == 21 or lena1 == 22 or lena1 == 23:
            a1 = a1 + "\t\t\t\t"

        if lena1 == 24 or lena1 == 25 or lena1 == 26 or lena1 == 27:
            a1 = a1 + "\t\t\t"

        if lena1 == 28 or lena1 == 29 or lena1 == 30 or lena1 == 31:
            a1 = a1 + "\t\t"

        # a2
        if lena2 == 1 or lena2 == 2 or lena2 == 3:
            a2 = a2 + "\t\t\t\t\t\t\t\t\t"

        if lena2 == 4 or lena2 == 5 or lena2 == 6 or lena2 == 7:
            a2 = a2 + "\t\t\t\t\t\t\t\t"

        if lena2 == 8 or lena2 == 9 or lena2 == 10 or lena2 == 11:
            a2 = a2 + "\t\t\t\t\t\t\t"

        if lena2 == 12 or lena2 == 13 or lena2 == 14 or lena2 == 15:
            a2 = a2 + "\t\t\t\t\t\t"

        if lena2 == 16 or lena2 == 17 or lena2 == 18 or lena2 == 19:
            a2 = a2 + "\t\t\t\t\t"

        if lena2 == 20 or lena2 == 21 or lena2 == 22 or lena2 == 23:
            a2 = a2 + "\t\t\t\t"

        if lena2 == 24 or lena2 == 25 or lena2 == 26 or lena2 == 27:
            a2 = a2 + "\t\t\t"

        if lena2 == 28 or lena2 == 29 or lena2 == 30 or lena2 == 31:
            a2 = a2 + "\t\t"

        # a3
        if lena3 == 1 or lena3 == 2 or lena3 == 3:
            a3 = a3 + "\t\t\t\t\t\t\t\t\t"

        if lena3 == 4 or lena3 == 5 or lena3 == 6 or lena3 == 7:
            a3 = a3 + "\t\t\t\t\t\t\t\t"

        if lena3 == 8 or lena3 == 9 or lena3 == 10 or lena3 == 11:
            a3 = a3 + "\t\t\t\t\t\t\t"

        if lena3 == 12 or lena3 == 13 or lena3 == 14 or lena3 == 15:
            a3 = a3 + "\t\t\t\t\t\t"

        if lena3 == 16 or lena3 == 17 or lena3 == 18 or lena3 == 19:
            a3 = a3 + "\t\t\t\t\t"

        if lena3 == 20 or lena3 == 21 or lena3 == 22 or lena3 == 23:
            a3 = a3 + "\t\t\t\t"

        if lena3 == 24 or lena3 == 25 or lena3 == 26 or lena3 == 27:
            a3 = a3 + "\t\t\t"

        if lena3 == 28 or lena3 == 29 or lena3 == 30 or lena3 == 31:
            a3 = a3 + "\t\t"

        # a4
        if lena4 == 1 or lena4 == 2 or lena4 == 3:
            a4 = a4 + "\t\t\t\t\t\t\t\t\t"

        if lena4 == 4 or lena4 == 5 or lena4 == 6 or lena4 == 7:
            a4 = a4 + "\t\t\t\t\t\t\t\t"

        if lena4 == 8 or lena4 == 9 or lena4 == 10 or lena4 == 11:
            a4 = a4 + "\t\t\t\t\t\t\t"

        if lena4 == 12 or lena4 == 13 or lena4 == 14 or lena4 == 15:
            a4 = a4 + "\t\t\t\t\t\t"

        if lena4 == 16 or lena4 == 17 or lena4 == 18 or lena4 == 19:
            a4 = a4 + "\t\t\t\t\t"

        if lena4 == 20 or lena4 == 21 or lena4 == 22 or lena4 == 23:
            a4 = a4 + "\t\t\t\t"

        if lena4 == 24 or lena4 == 25 or lena4 == 26 or lena4 == 27:
            a4 = a4 + "\t\t\t"

        if lena4 == 28 or lena4 == 29 or lena4 == 30 or lena4 == 31:
            a4 = a4 + "\t\t"

        # values = [1, 100]
        # for i in range(100):
        #    values.append(random.random())
        # values.sort()
        # results = []
        # for i in range(1,5):
        #    results.append(values[i])
        # print (results)

        file.write("\n".join(text))
        file.write("\nОтчёт за " + str(yesterday.strftime('%d.%m.%y')))
        file.write("\n" + "\n".join(text2))
        file.write("\n" + a1 + b1 + c1 + '%\t\t\t\t' + str(d1) + '%')
        file.write("\n" + a2 + b2 + c2 + '%\t\t\t\t' + str(d2) + '%')
        file.write("\n" + a3 + b3 + c3 + '%\t\t\t\t' + str(d3) + '%')
        file.write("\n" + a4 + b4 + c4 + '%\t\t\t\t' + str(d4) + '%')

        bot.send_document(message.chat.id, f, "familiya.txt")

        file.close()
    
    
    
    
    
    
    
    



@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == '1':
        bot.send_message(call.message.chat.id, 'Продолжаем разговор')

        bot.send_message(call.message.chat.id, 'Генерюсь')




#@bot.message_handler(commands=['marksSYAP'])
#        def send_welcome(message):
#           with open("D:\\MarksSYAP.xlsx", "rb") as misc:
#               f = misc.read()
#           bot.send_document(message.chat.id, f)


    elif call.data == '2':
     bot.send_message(call.message.chat.id, 'Тогда ПОКА! Заполняй свой отчёт сам.')







bot.polling(none_stop=True, interval=0)

















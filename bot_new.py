# -*- coding: utf-8 -*-

import pyowm
import config
import datetime
import telebot
import time
import random
import os.path


from telebot import types

from pyowm import OWM

owm = pyowm.OWM('1884e6b6d5605fee686cf449ac8b1e54', language='RU')
bot = telebot.TeleBot(config.token)



stations = ['Бейские Копи', 'Углесборочная', 'Барбаров', '1553 км', 'Б/п 5647', 'Выдрино', 'Горхон-Затяжной', 'Дивизионная',
            'Заудинский', 'Звездная', 'Камышет', 'Кедровая', 'Клюевка', 'Куйтун', 'Мысовая', 'Онохой', 'Перевоз', 'Посольская',
            'Рудногорск', 'Селенга', 'Слюдянка-2', 'Таловка', 'Танхой', 'Татаурово', 'Тимлюй', 'Ук', 'Хужир', 'Шалуты', 'Ардаши',
            'Аэропорт', 'Вахитово', 'Восстание', 'Глазов', 'Гороховец', 'Горький сорт.', 'Каликино', 'Комбинат - Тихорецкая',
            'Линда', 'Новки', 'Петушки', 'Поздино', 'Поздино - Полой', 'Просница', 'Просница - Бумкомбинат', 'Свияжск', 'Тереховицы-Второво',
            'Тихорецкая', 'Федулово-Новки', 'Юбилейная - Комбинат', 'Амур', 'Барановский - Раздольное', 'Гвоздевский', 'Глухариный',
            'Заячий', 'Иванокит', 'Икура', 'Кипарисово-Раздольное', 'Комсомольск сорт.', 'Комсомольская', 'Кувыкта', 'Кутыкан', 'Морошка',
            'Николаевка', 'Первая речка', 'Побожий', 'Раздольное', 'Сосновый', 'Тында', 'Федосеев', 'Фридман', 'Хмыловский', 'Баляга',
            'Декабристы', 'Домна', 'Кадала - Черновская', 'Кадала', 'Куэнга', 'Лесная', 'Улягир', 'Усть-Пера', 'Черновская', 'Черновская - Кадала',
            'Яблоновая', 'Карбышево-1', 'Кемерово', 'Кокошино', 'Пикетное', 'Сыропятское', 'Укладочный', 'Чулымская', 'Юрга-1', 'Жетыген-Алтынколь',
            'Егинсу', 'Жетыген', 'Узень', 'уч. Жетыген-Алтынколь', 'Гвардейск', 'Дзержинская Новая', 'Знаменск', 'Луговое-Новое', 'Озерки новые',
            'Абакан', 'Заозерная', 'Зерцалы', 'Иланская', 'Ирба', 'Камала', 'Красный Кордон', 'Мана', 'п.п. 531км', 'Предметкино', 'Сорокино',
            'Суслово', 'Уяр', 'Щетинкино', 'Звезда', 'Леонидовка', 'Пенза 2', 'Рузаевка', 'Черниковка', 'Авиационная', 'Александров-2',
            'Бекасово-сорт.', 'Бельково', 'Бельково - Киржач', 'Березка', 'Давыдово', 'Дрезна', 'Жёлтиково', 'Ивантеевка', 'Иванцево',
            'Канатчиково', 'Карабаново - Бельково', 'Киржач', 'Кожухово', 'Космос', 'Костино', 'Кусково', 'Лефортово-Черкизово',
            'Монино', 'Москва-Товарная-Смоленская', 'Наугольный', 'Наугольный - Желтиково', 'Подмосковная', 'Подольск', 'Покров',
            'Покров - Петушки', 'Реутово', 'Угрешская', 'Усад', 'Усад - Пост 97 км', 'Фрязино', 'Калашниково', 'Угловка', 'В.Баскунчак',
            'Нефтяная', 'Пост 6км', 'Трусово', 'Шунгули', 'Гагарский-Мезенский', 'Демьянка', 'Кокшаровский', 'Мезенский-Баженово',
            'Мезенский', 'Менделеево', 'Перегон', 'Пермь парк Г', 'Путевка', 'Пышминская', 'Свердловск-сорт.', 'Тобольск', 'Чепца',
            'Шабуничи', 'Шарташ', 'Беклемишево-Рязанцево', 'Берендеево', 'Деболовская', 'Итларь', 'Рязанцево', 'Рязанцево - Шушково',
            'Шушково - Берендеево', 'Козырьки', 'Джам- Айритам', 'Айритам - Алатун', 'Бактрия-Термез', 'Гузар', 'Мараканд - Гумбаз',
            'Улус - Джам', 'Жаркурган - Бактрия', 'Камаши', 'Кашкадарья - Карши', 'Нигуз - Кашкадарья', 'Китаб', 'Кумкурган-Сурхан',
            'Нигуз - Алатун', 'Разъезд 165 - Жаркурган', 'Сурхан - Разъезд 165', 'Танхоз', 'Гумбаз - Улус', 'Яккабог',
            'Вольный - Сахновщина', 'Гражданский', 'Кегичевка - Вольный', 'Модуль 165 км - Гражданский', 'Орелька - Модуль 165 км',
            'Пост 136 км - Пост 146 км', 'Пост 146 км - Орелька', 'Сахновщина - Пост 136 км', 'Разъезд 36', 'Ольха-Абрамовка',
            'Ольха-Абрамовка', 'Абрамовка-Таловая', 'Евдаково', 'Зайцевка', 'Придонская-Икорец', 'Кантемировка', 'Лиски', 'Ольха',
            'Подгорное', 'Сергеевка', 'Сомово-Отрожка', 'Иковка', 'Качусово-Каргополье', 'Кособродск'', ''Миасс', 'Твердыш-Окуневка',
            'Окуневка-Кособродск', 'Просвет-Галкино', 'Твердыш', 'Челябинск Главный парк "П"', 'Челябинск парк А', 'Шагол',
            'Шадринск', 'Алдан', 'Амга', 'Болотный', 'Денисовский', 'Кердем', 'Кюргелях', 'Нижний Бестях', 'Томмот']


work = ['Предрелизная проверка', 'Разработка ПО АРМ', 'АПК-ДК', 'Корректировка ПО АРМ', 'Разработка ДЦ', 'Разработка ПО АРМ', 'Корректировка ДЦ']

text_one = ["""========================================================================================================================================================================================================
= Поле "Объект:" должно содержать название станции/участка и название дороги                                                                                                                           =
= Поле "Задача:" должно содержать номер 1-го связанного с задачей дефекта или текстовое описание при отсутствии дефекта, в последнем случае описание дополняется ссылкой на автора поставленной задачи =
= Поле "%готовности:" должно содержать реальный процент готовности по указанной задаче                                                                                                                 =
= При достижении 100% готовности задача удаляется из списка работ на следующий день                                                                                                                    =
= Поле "%загрузки:" должно содержать реальный процент загруженности в течении дня по указанной задаче, сумма процентов по всем задачам должна быть равна 100%                                          =
= Поле "Дата_окончания:" должно содержать планируемую дату окончания активностей по задаче                                                                                                             =
= Поле "Активность_тестов:" должно содержать количество правок по дефекту в течении дня                                                                                                                =
= Поле "Причина_неисполнения:" в случае превышения планируемых сроков или при наличии обстоятельств непреодолимой силы должно содержать описание причины                                               =
========================================================================================================================================================================================================"""]

text_two = ["""========================================================================================================================================================================================================
= Объект:                              = Задача:                        = %готовности: = %загрузки: = Дата_окончания: = Активность_тестов:  =   Причина_неисполнения:                                  =
========================================================================================================================================================================================================"""]

text_tree = ["""========================================================================================================================================================================================================"""]



from datetime import date, timedelta
yesterday = date.today() - timedelta(days=1)
friday = date.today() + timedelta(days=3)
saturday = date.today() + timedelta(days=2)
sunday = date.today() + timedelta(days=1)
saturday_otchet = date.today() - timedelta(days=1)
sunday_otchet = date.today() - timedelta(days=2)
monday = date.today() - timedelta(days=3)

a1=random.choice(stations)
a2=random.choice(stations)
a3=random.choice(stations)
a4=random.choice(stations)
a5=random.choice(stations)
a6=random.choice(stations)
a7=random.choice(stations)

#генерим два случайных плана из отчёта
plan=random.sample([1,2,3,4],2)
plan1=plan[0]
plan2=plan[1]
print(plan,plan1,plan2)

b1=random.choice(work)
b2=random.choice(work)
b3=random.choice(work)
b4=random.choice(work)
b5=random.choice(work)
b6=random.choice(work)
b7=random.choice(work)

c1=str(int(round(random.randint(1, 100)/5.0)*5.0))
c2=str(int(round(random.randint(1, 100)/5.0)*5.0))
c3=str(int(round(random.randint(1, 100)/5.0)*5.0))
c4=str(int(round(random.randint(1, 100)/5.0)*5.0))
c5=str(int(round(random.randint(1, 100)/5.0)*5.0))
c6=str(int(round(random.randint(1, 100)/5.0)*5.0))
c7=str(int(round(random.randint(1, 100)/5.0)*5.0))

#d1=round(random.randint(1, 100)/5)*5
#d2=round(random.randint(1, 100)/5)*5
#d3=round(random.randint(1, 100)/5)*5
#d4=round(random.randint(1, 100)/5)*5

#вычисляем случайное число в сумме не больше 100
zadachi = 4
schetchik = random.randint(1,zadachi)

if schetchik == 1:
    d1 = round(random.randint(0, 100)/5)*5
    d2 = round(random.randint(0, 100-d1)/5)*5
    d3 = round(random.randint(0, 100-d1-d2)/5)*5
    d4 = (100-d1-d2-d3)
    print(d1, d2, d3, d4)

if schetchik == 2:
    d2 = round(random.randint(0, 100)/5)*5
    d1 = round(random.randint(0, 100 - d2)/5)*5
    d3 = round(random.randint(0, 100-d2-d1)/5)*5
    d4 = (100-d2-d1-d3)
    print(d1, d2, d3, d4)

if schetchik == 3:
    d3 = round(random.randint(0, 100)/5)*5
    d1 = round(random.randint(0, 100 - d3)/5)*5
    d2 = round(random.randint(0, 100-d3-d1)/5)*5
    d4 = (100-d3-d1-d2)
    print(d1, d2, d3, d4)

if schetchik == 4:
    d4 = round(random.randint(0, 100)/5)*5
    d1 = round(random.randint(0, 100 - d4)/5)*5
    d2 = round(random.randint(0, 100-d4-d1)/5)*5
    d3 = (100-d4-d1-d2)
    print(d1, d2, d3, d4)

print (d1,d2,d3,d4)

#измеряем количество символов
lena1=len(a1)
lena2=len(a2)
lena3=len(a3)
lena4=len(a4)
lena5=len(a5)
lena6=len(a6)

if b1 == 'Предрелизная проверка':
   c1=  "\t\t\t\t\t" + c1
if b2 == 'Предрелизная проверка':
   c2=  "\t\t\t\t\t" + c2
if b3 == 'Предрелизная проверка':
   c3=  "\t\t\t\t\t" + c3
if b4 == 'Предрелизная проверка':
   c4=  "\t\t\t\t\t" + c4
if b5 == 'Предрелизная проверка':
   c5=  "\t\t\t\t\t" + c5
if b6 == 'Предрелизная проверка':
   c6=  "\t\t\t\t\t" + c6


if b1 == 'Разработка ПО АРМ':
   c1=  "\t\t\t\t\t\t" + c1
if b2 == 'Разработка ПО АРМ':
   c2=  "\t\t\t\t\t\t" + c2
if b3 == 'Разработка ПО АРМ':
   c3=  "\t\t\t\t\t\t" + c3
if b4 == 'Разработка ПО АРМ':
   c4=  "\t\t\t\t\t\t" + c4
if b5 == 'Разработка ПО АРМ':
   c5=  "\t\t\t\t\t\t" + c5
if b6 == 'Разработка ПО АРМ':
   c6=  "\t\t\t\t\t\t" + c6

if b1 == 'АПК-ДК':
   c1=  "\t\t\t\t\t\t\t\t\t" + c1
if b2 == 'АПК-ДК':
   c2=  "\t\t\t\t\t\t\t\t\t" + c2
if b3 == 'АПК-ДК':
   c3=  "\t\t\t\t\t\t\t\t\t" + c3
if b4 == 'АПК-ДК':
   c4=  "\t\t\t\t\t\t\t\t\t" + c4
if b5 == 'АПК-ДК':
   c5=  "\t\t\t\t\t\t\t\t\t" + c5
if b6 == 'АПК-ДК':
   c6=  "\t\t\t\t\t\t\t\t\t" + c6

if b1 == 'Корректировка ПО АРМ':
   c1=  "\t\t\t\t\t" + c1
if b2 == 'Корректировка ПО АРМ':
   c2=  "\t\t\t\t\t" + c2
if b3 == 'Корректировка ПО АРМ':
   c3=  "\t\t\t\t\t" + c3
if b4 == 'Корректировка ПО АРМ':
   c4=  "\t\t\t\t\t" + c4
if b5 == 'Корректировка ПО АРМ':
   c5=  "\t\t\t\t\t" + c5
if b6 == 'Корректировка ПО АРМ':
   c6=  "\t\t\t\t\t" + c6

if b1 == 'Разработка ДЦ':
   c1=  "\t\t\t\t\t\t\t" + c1
if b2 == 'Разработка ДЦ':
   c2=  "\t\t\t\t\t\t\t" + c2
if b3 == 'Разработка ДЦ':
   c3=  "\t\t\t\t\t\t\t" + c3
if b4 == 'Разработка ДЦ':
   c4=  "\t\t\t\t\t\t\t" + c4
if b5 == 'Разработка ДЦ':
   c5=  "\t\t\t\t\t\t\t" + c5
if b6 == 'Разработка ДЦ':
   c6=  "\t\t\t\t\t\t\t" + c6

if b1 == 'Разработка ПО АРМ':
   c1=  "" + c1
if b2 == 'Разработка ПО АРМ':
   c2=  "" + c2
if b3 == 'Разработка ПО АРМ':
   c3=  "" + c3
if b4 == 'Разработка ПО АРМ':
   c4=  "" + c4
if b5 == 'Разработка ПО АРМ':
   c5=  "" + c5
if b6 == 'Разработка ПО АРМ':
   c6=  "" + c6

if b1 == 'Корректировка ДЦ':
   c1=  "\t\t\t\t\t\t" + c1
if b2 == 'Корректировка ДЦ':
   c2=  "\t\t\t\t\t\t" + c2
if b3 == 'Корректировка ДЦ':
   c3=  "\t\t\t\t\t\t" + c3
if b4 == 'Корректировка ДЦ':
   c4=  "\t\t\t\t\t\t" + c4
if b5 == 'Корректировка ДЦ':
   c5=  "\t\t\t\t\t\t" + c5
if b6 == 'Корректировка ДЦ':
   c6=  "\t\t\t\t\t\t" + c6

if lena1 == 1 or lena1 == 2 or lena1 == 3:
    a1=  a1 + "\t\t\t\t\t\t\t\t\t"

if lena1 == 4 or lena1 == 5 or lena1 == 6 or lena1 == 7:
    a1=  a1 + "\t\t\t\t\t\t\t\t"

if lena1 == 8 or lena1 == 9 or lena1 == 10 or lena1 == 11:
    a1=  a1 + "\t\t\t\t\t\t\t"

if lena1 == 12 or lena1 == 13 or lena1 == 14 or lena1 == 15:
    a1=  a1 + "\t\t\t\t\t\t"

if lena1 == 16 or lena1 == 17 or lena1 == 18 or lena1 == 19:
    a1=  a1 + "\t\t\t\t\t"

if lena1 == 20 or lena1 == 21 or lena1 == 22 or lena1 == 23:
    a1=  a1 + "\t\t\t\t"

if lena1 == 24 or lena1 == 25 or lena1 == 26 or lena1 == 27:
    a1=  a1 + "\t\t\t"

if lena1 == 28 or lena1 == 29 or lena1 == 30 or lena1 == 31:
    a1=  a1 + "\t\t"


#a2
if lena2 == 1 or lena2 == 2 or lena2 == 3:
    a2=  a2 + "\t\t\t\t\t\t\t\t\t"

if lena2 == 4 or lena2 == 5 or lena2 == 6 or lena2 == 7:
    a2=  a2 + "\t\t\t\t\t\t\t\t"

if lena2 == 8 or lena2 == 9 or lena2 == 10 or lena2 == 11:
    a2=  a2 + "\t\t\t\t\t\t\t"

if lena2 == 12 or lena2 == 13 or lena2 == 14 or lena2 == 15:
    a2=  a2 + "\t\t\t\t\t\t"

if lena2 == 16 or lena2 == 17 or lena2 == 18 or lena2 == 19:
    a2=  a2 + "\t\t\t\t\t"

if lena2 == 20 or lena2 == 21 or lena2 == 22 or lena2 == 23:
    a2=  a2 + "\t\t\t\t"

if lena2 == 24 or lena2 == 25 or lena2 == 26 or lena2 == 27:
    a2=  a2 + "\t\t\t"

if lena2 == 28 or lena2 == 29 or lena2 == 30 or lena2 == 31:
    a2=  a2 + "\t\t"


#a3
if lena3 == 1 or lena3 == 2 or lena3 == 3:
    a3=  a3 + "\t\t\t\t\t\t\t\t\t"

if lena3 == 4 or lena3 == 5 or lena3 == 6 or lena3 == 7:
    a3=  a3 + "\t\t\t\t\t\t\t\t"

if lena3 == 8 or lena3 == 9 or lena3 == 10 or lena3 == 11:
    a3=  a3 + "\t\t\t\t\t\t\t"

if lena3 == 12 or lena3 == 13 or lena3 == 14 or lena3 == 15:
    a3=  a3 + "\t\t\t\t\t\t"

if lena3 == 16 or lena3 == 17 or lena3 == 18 or lena3 == 19:
    a3=  a3 + "\t\t\t\t\t"

if lena3 == 20 or lena3 == 21 or lena3 == 22 or lena3 == 23:
    a3=  a3 + "\t\t\t\t"

if lena3 == 24 or lena3 == 25 or lena3 == 26 or lena3 == 27:
    a3=  a3 + "\t\t\t"

if lena3 == 28 or lena3 == 29 or lena3 == 30 or lena3 == 31:
    a3=  a3 + "\t\t"

#a4
if lena4 == 1 or lena4 == 2 or lena4 == 3:
    a4=  a4 + "\t\t\t\t\t\t\t\t\t"

if lena4 == 4 or lena4 == 5 or lena4 == 6 or lena4 == 7:
    a4=  a4 + "\t\t\t\t\t\t\t\t"

if lena4 == 8 or lena4 == 9 or lena4 == 10 or lena4 == 11:
    a4=  a4 + "\t\t\t\t\t\t\t"

if lena4 == 12 or lena4 == 13 or lena4 == 14 or lena4 == 15:
    a4=  a4 + "\t\t\t\t\t\t"

if lena4 == 16 or lena4 == 17 or lena4 == 18 or lena4 == 19:
    a4=  a4 + "\t\t\t\t\t"

if lena4 == 20 or lena4 == 21 or lena4 == 22 or lena4 == 23:
    a4=  a4 + "\t\t\t\t"

if lena4 == 24 or lena4 == 25 or lena4 == 26 or lena4 == 27:
    a4=  a4 + "\t\t\t"

if lena4 == 28 or lena4 == 29 or lena4 == 30 or lena4 == 31:
    a4=  a4 + "\t\t"

#a5
if lena5 == 1 or lena5 == 2 or lena5 == 3:
    a5=  a5 + "\t\t\t\t\t\t\t\t\t"

if lena5 == 4 or lena5 == 5 or lena5 == 6 or lena5 == 7:
    a5=  a5 + "\t\t\t\t\t\t\t\t"

if lena5 == 8 or lena5 == 9 or lena5 == 10 or lena5 == 11:
    a5=  a5 + "\t\t\t\t\t\t\t"

if lena5 == 12 or lena5 == 13 or lena5 == 14 or lena5 == 15:
    a5=  a5 + "\t\t\t\t\t\t"

if lena5 == 16 or lena5 == 17 or lena5 == 18 or lena5 == 19:
    a5=  a5 + "\t\t\t\t\t"

if lena5 == 20 or lena5 == 21 or lena5 == 22 or lena5 == 23:
    a5=  a5 + "\t\t\t\t"

if lena5 == 24 or lena5 == 25 or lena5 == 26 or lena5 == 27:
    a5=  a5 + "\t\t\t"

if lena5 == 28 or lena5 == 29 or lena5 == 30 or lena5 == 31:
    a5=  a5 + "\t\t"


#a6
if lena6 == 1 or lena6 == 2 or lena6 == 3:
    a6=  a6 + "\t\t\t\t\t\t\t\t\t"

if lena6 == 4 or lena6 == 5 or lena6 == 6 or lena6 == 7:
    a6=  a6 + "\t\t\t\t\t\t\t\t"

if lena6 == 8 or lena6 == 9 or lena6 == 10 or lena6 == 11:
    a6=  a6 + "\t\t\t\t\t\t\t"

if lena6 == 12 or lena6 == 13 or lena6 == 14 or lena6 == 15:
    a6=  a6 + "\t\t\t\t\t\t"

if lena6 == 16 or lena6 == 17 or lena6 == 18 or lena6 == 19:
    a6=  a6 + "\t\t\t\t\t"

if lena6 == 20 or lena6 == 21 or lena6 == 22 or lena6 == 23:
    a6=  a6 + "\t\t\t\t"

if lena6 == 24 or lena6 == 25 or lena6 == 26 or lena6 == 27:
    a6=  a6 + "\t\t\t"

if lena6 == 28 or lena6 == 29 or lena6 == 30 or lena6 == 31:
    a6=  a6 + "\t\t"



# Месяц
today = datetime.datetime.today()
mount = ['Января', 'Февраля', 'Марта', 'Апреля', 'Мая', 'Июня', 'Июля', 'Августа', 'Сентября', 'Октября', 'Ноября',
         'Декабря']
mounth_real = int(today.strftime("%m"))

# день и месяц текстом
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

text1 = ('Сегодня ' + day + ' ,' + today.strftime("%d") + ' ' + mount[mounth_real % 12] + ' ' + today.strftime(
    "%Y") + ' г.')
text2 = ('Погода в Москве хорошая, ' + w.get_detailed_status() + ' ' + str(round(temp)) + ' °C')




@bot.message_handler(content_types=["text"])
def message(message):
    users_id = message.chat.id
    users_name = message.chat.first_name
    timers = datetime.datetime.today().strftime("%d.%m.%Y %H:%M:%S")
    doc = open('stat/stat.txt', 'a', encoding='utf-8')
    doc.write(f'{users_id} : {users_name} : {timers} - start\n')
    doc.close

    bot.send_message(message.chat.id, "Привет. Это генератор отчётов.")
    time.sleep(1)
    bot.send_message(message.chat.id, text1)
    time.sleep(1)
    bot.send_message(message.chat.id, text2)
    time.sleep(1)
    markup = telebot.types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('ДА ', callback_data='1')
    button2 = types.InlineKeyboardButton('НЕТ ', callback_data='2')
    markup.row(button1, button2)
    bot.send_message(message.from_user.id, f"Вы хотите сгенерировать план на сегодня и отчёт за вчера?",
                     reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == '1':

        bot.send_message(call.message.chat.id, 'Продолжаем разговор')
        bot.send_message(call.message.chat.id, 'Генерю')

        file = open("D:\\test.txt", "w")
        file.write("\n".join(text_one))

        if day == 'суббота':
            file.write("\nОтчёт за " + str(saturday_otchet.strftime('%d.%m.%y')) + "\n")
        elif day == 'пятница':
            file.write("\nОтчёт за " + str(sunday_otchet.strftime('%d.%m.%y')) + "\n")
        elif day == 'понедельник':
            file.write("\nОтчёт за " + str(monday.strftime('%d.%m.%y')) + "\n")
        else:
            file.write("\nОтчёт за " + str(today.strftime('%d.%m.%y')) + "\n")

        file.write("\n" + "\n".join(text_two))
        file.write("\n" + a1 + b1 + c1 + '%\t\t\t\t' + str(d1) + '%')
        file.write("\n" + a2 + b2 + c2 + '%\t\t\t\t' + str(d2) + '%')
        file.write("\n" + a3 + b3 + c3 + '%\t\t\t\t' + str(d3) + '%')
        file.write("\n" + a4 + b4 + c4 + '%\t\t\t\t' + str(d4) + '%')
        file.write("\n")
        file.write("\n")
        file.write("\n".join(text_tree))

        if day == 'суббота':
            file.write("\nПлан на " + str(saturday.strftime('%d.%m.%y')) + "\n")
        elif day == 'Воскресенье':
            file.write("\nПлан на " + str(sunday.strftime('%d.%m.%y')) + "\n")
        elif day == 'пятница':
            file.write("\nПлан на " + str(sunday.strftime('%d.%m.%y')) + "\n")
        else:
            file.write("\nПлан на " + str(today.strftime('%d.%m.%y')) + "\n")

        file.write("\n".join(text_tree))

        # добавляем одну станцию из отчёта в план
        if plan1 == 1:
            c1 == '100%'
            file.write("\n" + a1 + b1 + c1 + '%\t\t\t\t' + str(d1) + '%')
            d5 = 100 - d1
        elif plan1 == 2:
            c2 == '100%'
            file.write("\n" + a2 + b2 + c2 + '%\t\t\t\t' + str(d2) + '%')
            d5 = 100 - d2
        elif plan1 == 3:
            c3 == '100%'
            file.write("\n" + a3 + b3 + c3 + '%\t\t\t\t' + str(d3) + '%')
            d5 = 100 - d3
        elif plan1 == 4:
            c4 == '100%'
            file.write("\n" + a4 + b4 + c4 + '%\t\t\t\t' + str(d4) + '%')
            d5 = 100 - d4

        # добавляем вторую станцию из отчёта в план
        if plan2 == 1:
            file.write("\n" + a1 + b1 + c1 + '%\t\t\t\t' + str(d1) + '%')
            d6 = 100 - d1
        elif plan2 == 2:
            file.write("\n" + a2 + b2 + c2 + '%\t\t\t\t' + str(d2) + '%')
            d6 = 100 - d2
        elif plan2 == 3:
            file.write("\n" + a3 + b3 + c3 + '%\t\t\t\t' + str(d3) + '%')
            d6 = 100 - d3
        elif plan2 == 4:
            file.write("\n" + a4 + b4 + c4 + '%\t\t\t\t' + str(d4) + '%')
            d6 = 100 - d4


        dd = int(abs((100 - d5 - d6) / 2))

        #планы на новые станции
        file.write("\n" + a5 + b5 + c5 + '%\t\t\t\t' + str(dd) + '%')
        file.write("\n" + a6 + b6 + c6 + '%\t\t\t\t' + str(dd) + '%')

        file.write("\n")
        file.write("\n")
        file.write("\n" + 'Замороженные объекты')
        file.write("\n" + a7 + b7 + c7 + '%\t\t\t\t' + '0' + '%')


        file.close()

        f = open("D:\\test.txt", "rb")
        bot.send_document(call.message.chat.id, f)

        file.close()

        check_file = os.path.isfile('D:\\test.txt')  # True
        print(check_file)
        if check_file == True:
            bot.send_message(call.message.chat.id, 'Отчёт создан')
        elif check_file == False:
            bot.send_message(call.message.chat.id, 'Отчёт не создан')

    elif call.data == '2':
        bot.send_message(call.message.chat.id, 'Тогда ПОКА! Заполняй свой отчёт сам.')


bot.polling(none_stop=True, interval=0)

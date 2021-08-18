# В этом файле работаем с самым основным алгоритмом:
# Получение разницы курса относительно рубля между двумя датами за выбранную дату,
# метод должен принимать символьный код валюты, и две даты.

import requests     # обработка URL
import re           # регулярные выражения
import currency_character_code


def date_conversion(date):  # в условиях даты передаются в формате YYYY-MM-DD, для сайта нужен иной формат
    date = date.split('-')
    date[0], date[2] = date[2], date[0]
    return "/".join(date)


def date_check(date):       # проверка на правильность даты
    date = date.split('-')
    for i in date:      # проверка, что бы не падало приложение при вводе иных символов
        if not i.isdigit():
            return False
    if int(date[0]) > 1900 and 1 <= int(date[1]) <= 12 and 1 <= int(date[2]) <= 31:
        return True
    else:
        return False


def currency_difference(date_from, date_to, curr_cod):
    new_date_from = date_conversion(date_from)      # меняем формат даты для сайта
    new_date_to = date_conversion(date_to)
    new_url = f"https://www.cbr.ru/scripts/XML_dynamic.asp?date_req1={new_date_from}&date_req2={new_date_to}&VAL_NM_RQ={currency_character_code.currency_dict[curr_cod][2]}"
    site_responce = requests.get(new_url).text      # создали нужный нам URL и получили ответ
    site_responce = re.sub(r'\<[^>]*\>', ' ', site_responce).split()
    if len(site_responce) < 5:      # если список пуст, значит нет значений
        return "Нет значений за выбранный период"
    return f"Курс за {date_from} составляет: {site_responce[1]} за {site_responce[0]} {curr_cod}\n" \
           f"Курс за {date_to} составляет: {site_responce[-1]} за {site_responce[-2]} {curr_cod}\n" \
           f"Разница состовляет: {float(re.sub(',', '.', site_responce[1])) - float(re.sub(',', '.', site_responce[-1]))} ₽"


def switch_two():       # интерфейс меню с проверкой вводимых значений
    curr_cd = input('Код валюты: ').upper().strip()
    while curr_cd not in currency_character_code.currency_dict:     # проверка на правильный формат ввода значений
        print('Такой валюты нет.')
        currency_character_code.currency_code()
        curr_cd = input('Введите правильный код валюты: ').upper().strip()

    date_frm = input('Начало отслеживаемого периода: ').strip()
    while not date_check(date_frm):
        print('Неправильный формат даты')
        date_frm = input('Начало отслеживаемого периода в формате YYYY-MM-DD: ').strip()

    date_to = input('Конец отслеживаемого периода: ').strip()
    while not date_check(date_to):
        print('Неправильный формат даты')
        date_to = input('Конец отслеживаемого периода в формате YYYY-MM-DD: ').strip()

    print(currency_difference(date_frm, date_to, curr_cd))      # выводим ответ

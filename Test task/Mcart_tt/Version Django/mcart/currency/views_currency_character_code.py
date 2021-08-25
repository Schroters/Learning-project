# Вывод списка доступных валют
from django.shortcuts import render
import requests, re


url_currency = requests.get("http://www.cbr.ru/scripts/XML_valFull.asp").text
url_currency = re.sub(r'\<[^>]*\>', 'space', url_currency).split('space')   # удалили html теги и разделили на список
currency_dict = {}
temp_list = []

for i in url_currency:
    if i != "" and i[0].isalpha():     # Убрали не нужные нам строки
        if i.isupper() and i not in ['SDR', 'XDR', 'ЭКЮ', 'ECU', 'XEU'] and i[-1].isalpha():
            currency_dict[i] = temp_list   # Если большие буквы, значит символьный код валюты, он же ключ в словаре
            temp_list = []
        elif i == 'XDR':
            currency_dict['XDR'] = ['СДР (специальные права заимствования)', 'SDR', 'R01589']
            temp_list = []
        elif i == 'XEU':
            currency_dict['XEU'] = ['ЭКЮ', 'ECU', 'R01790']
            temp_list = []
        else:
            temp_list.append(i.rstrip())


def currency_list(request):
    currency_info = {}
    for i in currency_dict:
        currency_info[i] = currency_dict[i][0]
    return render(request, 'currency/currency_list.html', context={'title': 'Список валют', 'info': currency_info})

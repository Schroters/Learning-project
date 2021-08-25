# Валюта за период
import requests, re
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import exchRate_models
from .views_currency_character_code import currency_dict


def date_conversion(date):  # в условиях даты передаются в формате YYYY-MM-DD, для сайта нужен иной формат
    print(date)
    date = date.split('-')
    date[0], date[2] = date[2], date[0]
    return "/".join(date)


def currency_difference(date_to, date_from, curr_cod):
    new_date_from = date_conversion(date_from)      # меняем формат даты для сайта
    new_date_to = date_conversion(date_to)
    new_url = f"https://www.cbr.ru/scripts/XML_dynamic.asp?date_req1={new_date_from}&date_req2={new_date_to}&VAL_NM_RQ={currency_dict[curr_cod][2]}"
    site_responce = requests.get(new_url).text      # создали нужный нам URL и получили ответ
    site_responce = re.sub(r'\<[^>]*\>', ' ', site_responce).split()

    if len(site_responce) < 5:      # если список пуст, значит нет значений
        return "Нет значений за выбранный период"

    return {'amountCur': int(site_responce[0]),
            'size_to': site_responce[1],
            'size_from': site_responce[-1],
            'difference': float(re.sub(',', '.', site_responce[1])) - float(re.sub(',', '.', site_responce[-1]))}


def exchange_rate(request):
    history = exchRate_models.objects.order_by('-id')

    if request.method == "POST":
        new_data = exchRate_models()
        new_data.symbolCod_curr = request.POST.get('symbolCod_curr')
        new_data.date_to = request.POST.get('date_to')
        new_data.date_from = request.POST.get('date_from')
        # Получаем информацию исходя из полученных данных
        dict_func = currency_difference(new_data.date_from, new_data.date_to, new_data.symbolCod_curr)
        new_data.amountCur = dict_func['amountCur']
        new_data.size_to = dict_func['size_to']
        new_data.size_from = dict_func['size_from']
        new_data.difference = dict_func['difference']

        new_data.save()

        return HttpResponseRedirect('/exchange_rate')

    return render(request, 'currency/exchange_rate.html', {'history': history})

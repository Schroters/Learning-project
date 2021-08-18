# Основной файл, от сюда происходит запсук приложения

from currency_character_code import currency_code
from currency_exchange_rate import switch_two

breaker = True
while breaker:
    print('Введите "1" Если хотите увидеть список доступных валют\n'
          'Введите "2" Если хотите увидеть разницу курса относительно рубля между двумя датами\n'
          'Введите "0" Если хотите выйти')
    switch = input("Ваш выбор: ")
    if switch in ['1', '2', '0']:   # проверка меню
        if switch == "1":
            currency_code()         # вывод списка доступных валют
            print()
        elif switch == "2":
            print('Введите пожалуйста код валюты, дату с которой хотите начать '
                  'и дату конца отслеживаемого периода (формат даты YYYY-MM-DD)')
            switch_two()            # работа приложения по датам и вывод разницы
            print()
        elif switch == "0":
            breaker = False
            print('До свидания')
            break                   # выход из приложения
    else:
        print('Неизвестная команда, повторите пожалуйста ввод\n')

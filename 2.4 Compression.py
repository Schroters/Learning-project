# https://stepik.org/lesson/3367/step/7?thread=solutions&unit=950
# Требовалось написать программу, которая преобразует строку с количеством повторяющихся символов
# Кодирование осуществляется следующим образом: s = 'aaaabbсaa' преобразуется в 'a4b2с1a2',
# то есть группы одинаковых символов исходной строки
# заменяются на этот символ и количество его повторений в этой позиции строки.

s = input(str(''))
h = 1
k = len(s)

for i in range(k - 1):
    if s[i] == s[i+1]:              # сравниваем символ по текущему индексу со следующим
        h += 1                      # и прибовляем к счетчику
    elif s[i] != s[i+1]:            # если разные, то выводим значение счетчика
        print(s[i] + str(h), end='')
        h = 1

print(s[-1:], end='')
print(h)
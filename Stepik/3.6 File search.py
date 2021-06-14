# https://stepik.org/lesson/3378/step/3?unit=961
# Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
# Первое слово в тексте последнего файла: "We".
# Все файлы располагаются в каталоге по адресу:
# https://stepic.org/media/attachments/course67/3.6.3/

import requests


lin = "https://stepic.org/media/attachments/course67/3.6.3/"
with open('dataset_3378_3.txt','r') as file:
    stroka = file.readline().strip()
read=requests.get(stroka).text
while read[0:2] != "We":    # если не равно ве
    ht = lin + read         # прибавляем к ссылке, то что прочли
    read = requests.get(ht).text   # прочли по адресу
    print(ht)               # вывод что бы не думать, что все зависло
else:
    print(ht)   # последняя ссылка для скачивания файла
    print(read)    # прочли последний файл и вывели

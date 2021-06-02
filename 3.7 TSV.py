# https://stepik.org/lesson/3380/step/5?unit=963
# Дан файл с таблицей в формате TSV с информацией о росте школьников разных классов.
# Программа прочитает этот файл и подсчитает для каждого класса средний рост учащегося.
# Файл состоит из набора строк, каждая из которых представляет собой три поля: Класс / Фамилия / Рост
# Выводить информацию о среднем росте следует в порядке возрастания номера класса (для классов с первого по одиннадцатый).
# Если про какой-то класс нет информации, необходимо вывести напротив него прочерк.
# В качестве ответа прикрепите файл с полученными данными о среднем росте.

dic = {i: [0, 0] for i in range(1, 12)}  # Словарь {класс : [сумма роста : ученики]
with open('input.txt') as inf:
    # Заполняем словарь:
    for i in inf:
        line = i.strip().split('\t')
        dic[int(line[0])][0] += int(line[2])  # tab[класс][0] += рост ученика
        dic[int(line[0])][1] += 1  # tab[класс][1] += 1 (счетчик учеников в классе)
    for i in dic.keys():
        if dic[i][1] == 0:  # печать класса, в котором нет учеников
            print(i, '-')
        else:  # считаем учеников и средний рост
            print(i, (dic[i][0] / dic[i][1]))
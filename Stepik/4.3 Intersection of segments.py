# https://stepik.org/lesson/265082/step/11?unit=246030
# На числовой прямой даны два отрезка. Напишите программу, которая находит их пересечение
# Two segments are given on the numerical line. Write a program that finds their intersection

def intersection(a1, b1, a2, b2):
    if a1 > b2 or b1 < a2:  # значит не пересекаются вообще, отдельно
        print('пустое множество')

    elif a2 == b1:  # пересечение с одной стороны
        print(a2)
        print('Пересечение с одной стороны 1')
    elif a1 == b2:  # пересечение с одной стороны
        print(b2)
        print('Пересечение с одной стороны 2')

    elif a1 <= a2 < b1 < b2:    # частичное пересечение
        print(a2, b1)
        print('Частичное пересечение 1')
    elif a2 <= a1 < b2 < b1:
        print(a1, b2)
        print('Частичное пересечение 2')

    elif a2 < a1 < b1 <= b2:    # Частичное пересечение внутри
        print(a1, b1)
        print('Частичное пересечение внутри 1')
    elif a1 < a2 < b2 <= b1:
        print(a2, b2)
        print('Частичное пересечение внутри 2')

    elif a1 == a2 and b1 == b2:     # один в одном
        print(a1, b1)
        print('Полное пересечение')

    else:
        print('Всё плохо')

def intersection2(a1, b1, a2, b2):
    if min(b1, b2) < max(a1, a2):
        print('пустое множество')
    elif min(b1, b2) == max(a1, a2):
        print(min(b1, b2))
    else:
        print(max(a1, a2), min(b1, b2))


# проверка
data_test = [[1, 5, 6, 10],     # пустое множество
             [6, 10, 1, 5],     # пустое множество
             [1, 10, 3, 5],     # 3 5
             [1, 5, 3, 7],      # 3 5
             [3, 7, 1, 5],      # 3 5
             [3, 5, 1, 10],     # 3 5
             [1, 5, 5, 10],     # 5
             [5, 10, 1, 5],     # 5
             [1, 5, 1, 5],      # 1 5
             [1, 5, 1, 10],     # 1 5
             [5, 10, 1, 10],    # 5 10
             [1, 10, 5, 10],    # 5 10
             [1, 10, 1, 5]]     # 1 5


for i in data_test:
    print(i[0], i[1], i[2], i[3])
    intersection(i[0], i[1], i[2], i[3])
    intersection2(i[0], i[1], i[2], i[3])
    print('------------------------')

print('Свои тесты')
a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
intersection(a1, b1, a2, b2)




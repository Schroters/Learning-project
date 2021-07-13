# https://stepik.org/lesson/265082/step/10?unit=246030
# Определение цвета рулетки по числу
# Determining the color of the roulette by number

a = int(input())

if 0 <= a <= 36:
    if a == 0:
        print('зеленый')
    if 1 <= a < 11 or 19 <= a < 29:
        if a % 2 == 0:
            print('черный')
        else:
            print('красный')
    elif 11 <= a < 19 or 29 <= a <= 36:
        if a % 2 == 0:
            print('красный')
        else:
            print('черный')
else:
    print('ошибка ввода')


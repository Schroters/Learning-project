# Написать метод/функцию, который/которая на вход принимает массив городов.
# В качестве результата возвращает строку, где города разделены запятыми, а в конце стоит точка.
def comma_separated(lst):
    return ", ".join(lst) + "."


print(comma_separated(['Москва', 'Санкт-Петербург', 'Воронеж']))    # Москва, Санкт-Петербург, Воронеж.


# Написать метод/функцию, который/которая на вход принимает число (float),
# а на выходе получает число, округленное до пятерок.
def rounding(num):
    return round(num / 5) * 5


print(rounding(27))     # 25
print(rounding(27.8))   # 30
print(rounding(41.7))   # 40


# Написать метод/функцию, который/которая на вход принимает число (int),
# а на выходе выдает слово “компьютер” в падеже, соответствующем указанному количеству.
def num_computers(value):
    if 20 > value % 100 > 10:
        return str(value) + ' компьютеров'
    elif 5 > value % 10 > 1:
        return str(value) + ' компьютера'
    elif value % 10 == 1:
        return str(value) + ' компьютер'
    else:
        return str(value) + ' компьютеров'


print(num_computers(25))    # 25 компьютеров
print(num_computers(41))    # 41 компьютер
print(num_computers(1048))  # 1048 компьютеров
print(num_computers(22))
print(num_computers(1))


# Написать метод/функцию, который/которая на вход принимает целое число,
# а на выходе возвращает то, является ли число простым (не имеет делителей кроме 1 и самого себя).
def smpl_numb(numb):
    if numb == 1:
        return "Единица не относится ни к простым, ни к составным числам"
    else:
        temp_numb = 2
        while numb % temp_numb != 0:
            temp_numb += 1
        if temp_numb == numb:
            return f"Число {numb} простое"
        else:
            return f"Число {numb} составное"


print(smpl_numb(2))     # Число простое
print(smpl_numb(1))     # Исключение
print(smpl_numb(19))    # Число простое
print(smpl_numb(39))    # Составное число
print(smpl_numb(98))    # Составное число


# Написать метод, который определяет, какие элементы присутствуют в двух экземплярах в каждом из массивов
def repeat_array(arr_1, arr_2):
    result = set()
    for i in arr_1:
        if arr_1.count(i) > 1 and arr_2.count(i) > 1:
            result.add(i)
    return list(result)


print(repeat_array([7, 17, 1, 9, 1, 17, 56, 56, 23], [56, 17, 17, 1, 23, 34, 23, 1, 8, 1]))     # [1, 17]

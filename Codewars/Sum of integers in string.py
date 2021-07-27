# Sum of integers in string
# https://www.codewars.com/kata/598f76a44f613e0e0b000026
# Your task in this kata is to implement a function that calculates the sum of the integers inside a string
# Ваша задача в этом ката - реализовать функцию, которая вычисляет сумму целых чисел внутри строки.

import re


def sum_of_integers_in_string(s):             # first version
    return sum(map(int, re.findall(r'\d+', s)))


# Second version
def sum_of_integers_in_string_2(s):

    s = re.sub(r'[^A-z0-9]', 'SUB', s)
    new_s, s_sum = '', 0

    for i in s:
        if i.isdigit():              # Состоит ли строка из цифр
            new_s += i               # и прибовляем к счетчику
        elif i.isalpha():            # Состоит ли строка из букв
            if new_s != '':
                s_sum += int(new_s)
                new_s = ''
    if len(new_s) != 0:
        s_sum += int(new_s)
    return s_sum



print(sum_of_integers_in_string("The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog"))    # 3635
print(sum_of_integers_in_string("12.4"))    # 16
print(sum_of_integers_in_string("12/4"))    # 16
print(sum_of_integers_in_string("12-4"))    # 16
print(sum_of_integers_in_string("h3ll0w0rld"))  # 3
print(sum_of_integers_in_string("2 + 3 = "))    # 5
print(sum_of_integers_in_string("Our company made approximately 1 million in gross revenue last quarter.")) # 1
print(sum_of_integers_in_string("The Great Depression lasted from 1929 to 1939."))      # 3868
print(sum_of_integers_in_string("Dogs are our best friends."))     # 0
print(sum_of_integers_in_string("C4t5 are 4m4z1ng."))      # 18




# сделать списко с цифрами в строке, если без плюс, каждая строка отдельно
print(re.findall(r'\d+',"The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog"))
# ['30', '20', '10', '0', '1203', '914', '3', '1349', '102', '4']
print(re.findall(r'\d',"The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog"))
# ['3', '0', '2', '0', '1', '0', '0', '1', '2', '0', '3', '9', '1', '4', '3', '1', '3', '4', '9', '1', '0', '2', '4']
print(re.findall(r'\w',"The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog"))
# каждый символ в отдельном списке
print(re.findall(r'\s',"The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog"))

print(sum(map(int, re.findall(r'\d+',"The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog"))))
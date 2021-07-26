# вывести максимальные числа в списке, колиечство максимальных чисел n

def max_2(arr, n):
    if n < len(arr):
        new_arr = []
        for i in range(n):
            mx_arr = max(arr)
            new_arr.append(mx_arr)
            arr.remove(mx_arr)

        return new_arr
    return 0


def max_2_ver2(arr, n):
    if n < len(arr):
        return 0
    arr = sorted(arr, reverse=True)
    return arr[:n]


print(max_2([2,1,5,5,8], 3))
print(max_2_ver2([2, 1, 9, 9, 4, 7, 4, 2, 5, 5, 5, 8], 6))
print(max_2_ver2([], 1))






# Написать функцию, которая определяет, является ли переданная строка палиндромом
# (читается слева-направо и справа-налево одинаково).
# Примеры палиндромов:
# - Казак
# - А роза упала на лапу Азора
# - Do geese see God?
# - Madam, I’m Adam


def is_palindrome(data):
    import re
    data = str(data)
    result = re.sub(r'[^A-zА-я0-9]', '', data).lower()
    if result[::-1] == result:
        return True
    else:
        return False


print(is_palindrome('Madam, I’m Adam'))
print(is_palindrome('Казак'))
print(is_palindrome('А роза упала на лапу Азора'))
print(is_palindrome('Do geese see God?'))
print(is_palindrome('S'))
print(is_palindrome('No palindrome'))

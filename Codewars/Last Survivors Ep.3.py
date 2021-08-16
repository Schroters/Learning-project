# Last Survivors Ep.3
# https://www.codewars.com/kata/60a2d7f50eee95000d34f414
# Considering the list of strings as a 2D character array, the idea is to remove from each column, starting from bottom,
# as many letters as indicated in the list of numbers. Then return the remaining letters in any order as a string.
# Рассматривая список строк как массив двумерных символов, идея состоит в том, чтобы удалить из каждого столбца,
# начиная снизу, столько букв, сколько указано в списке чисел.
# Затем верните оставшиеся буквы в любом порядке в виде строки.


def last_survivors(arr, nums):
    arr_separate = list(map(lambda x: list(x), arr))
    result = ''
    for i in reversed(range(len(arr))):
        for j in range(len(arr[0])):
            if arr_separate[i][j] != " ":   # если не пусто
                if nums[j] != 0:            # если нет нуля
                    nums[j] -= 1            # вычитаем значение
                    arr_separate[i][j] = None   # убираем букву
            if arr_separate[i][j] != None and arr_separate[i][j] != " ":
                result += str(arr_separate[i][j])   # все наше добовляем в строку

    return result


print(last_survivors(['abc', '   ', ' a '], [0, 4, 1]))     # a
print('empty', last_survivors([' ','z'], [1]))   # ''
print(last_survivors(['zj','zj'], [9,0]))   # jj
print('empty', last_survivors(['d',' ',' ',' ',' '], [1]))  # ''
print(last_survivors(['help us we are dying'], [2,0,2,1,2,0,2,1,2,0,2,1,2,0,2,1,2,0,2,1]))  # eeeiu
print(last_survivors(['to   ', '  tal', 'it   ', '  ari', 'an   ', '  ism'], [7, 6, 4, 2, 1]))  # ail
print('empty', last_survivors([' ',' '], [0]))  # ''
print('empty', last_survivors([''], [1,2,3,4])) # ''
print('empty', last_survivors(['','','',''], []))   # ''
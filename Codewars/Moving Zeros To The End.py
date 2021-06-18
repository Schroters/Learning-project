# Moving Zeros To The End
# Algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements
# Алгоритм, который берет массив и перемещает все нули в конец, сохраняя порядок других элементов
def move_zeros(array):
    newarr = []
    for i in array:                  # новый массив без нулей
        if i != 0:
            newarr += [i]
    newarr += [0] * array.count(0)   # узнаем сколько 0 и прибавляем в конец

    return newarr

print(move_zeros([1, 0, 1, 2, 0, 1, 3]))   # returns [1, 1, 2, 1, 3, 0, 0]))
print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))  # [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))   # [1, 2, 1, 1, 3, 1, 0, 0, 0, 0])))
print(move_zeros([0, 0]))
print(move_zeros([0]))
print(move_zeros([ ]))
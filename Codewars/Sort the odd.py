# Sort the odd
# Have to sort the odd numbers in ascending order while leaving the even numbers at their original positions
# Отсортировать нечетные числа в порядке возрастания, оставляя четные числа на своих исходных позициях

lm = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]     # [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
lm1 = [7, 1]                            # [1, 7]
lm2 = [5, 8, 6, 3, 4]                   # [3, 8, 6, 5, 4]
lm3 = []                                # []
lm4 = [5, 3, 2, 8, 1, 4]                # [1, 3, 2, 8, 5, 4]
lm5 = [5, 3, 1, 8, 0]                   # [1, 3, 5, 8, 0]


def sort_array(source_array):
    counter = 0
    newevenumb, newodnumb = ['x'] * len(source_array), []     # четный и нечет
    for i in source_array:
        if i % 2 == 0:
            newevenumb[counter] = i
        else:
            newodnumb += [i]
        counter += 1

    newodnumb.sort() #   # сорт нечет
    counter, counterod = 0, 0           # обнулили счетчик и добавили новый
    for i in newevenumb:
        if i == 'x':
            newevenumb[counter] = newodnumb[counterod]
            counterod += 1
        counter += 1

    return newevenumb

print(sort_array(lm))
print(sort_array(lm1))
print(sort_array(lm2))
print(sort_array(lm3))
print(sort_array(lm4))
print(sort_array(lm5))
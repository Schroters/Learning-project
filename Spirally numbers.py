n = (int(input()))  # чтение размеров поля
a = [[0 for j in range(n)] for i in range(n)]  # матрица нулей
b, ai, aj, aim, ajm = 1, 0, 0, -1, -1   # счетчик / строки / столбцы / строка другой стороны / столбец другой

while b <= n * n:
    for j in range(n):  # top to right
        if a[ai][j] == 0:
            a[ai][j] = b
            b += 1
    for i in range(n):  # bottom to left
        if a[i][ajm] == 0:
            a[i][ajm] = b
            b += 1
    for jj in reversed(range(n)):  # bottom to right
        if a[aim][jj] == 0:
            a[aim][jj] = b
            b += 1
    for ii in reversed(range(n)):  # left to top
        if a[ii][aj] == 0:
            a[ii][aj] = b
            b += 1
    else:
        ai += 1
        ajm -= 1
        aj += 1
        aim -= 1

for row in a:
    for elem in row:
        print(elem, end=' ')
    print()
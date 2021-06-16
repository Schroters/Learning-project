# Gravity Flip (3D version)
# Given the initial configuration of the cubes in the box,
# find out how many cubes are in each of the n and m columns after Bob switches the gravity.
# Кубики перемещаются в сторону

def flip(d, olda):
    newa = olda.copy()
    if d == 'R':
        for i in range(len(newa)):
            newa[i] = sorted(newa[i])
    elif d == 'L':
        for i in range(len(newa)):
            newa[i] = sorted(newa[i], reverse=True)   # обратная сортировка
    elif d == 'U':
        newl, newml = [], []
        for i in range(len(newa[0])):
            for j in range(len(newa)):
                newl += [newa[j][i]]
            newl = sorted(newl, reverse=True)   # обратная сортировка так как верх сверху
            newml += [newl]     # дабвляем наш столбец в новую матрицу которая имеет столбцов зеркально
            newl = []           # обнуляем
        for i in range(len(newa[0])):
            for j in range(len(newa)):
                newa[j][i] = newml[i][j]   # меняем матрицы местами
    elif d == 'D':
        newl, newml = [], []
        for i in range(len(newa[0])):
            for j in range(len(newa)):
                newl += [newa[j][i]]
            newl = sorted(newl)
            newml += [newl]     # дабвляем наш столбец в новую матрицу которая имеет столбцов зеркально
            newl = []           # обнуляем
        for i in range(len(newa[0])):
            for j in range(len(newa)):
                newa[j][i] = newml[i][j]   # меняем матрицы местами

    return newa

box = [[1, 3, 2],
       [4, 5, 1],
       [6, 5, 3],
       [7, 2, 9]]
print(flip('R', box)) # [[1, 2, 3],
                     #  [1, 4, 5],
                     #  [3, 5, 6],
                     #  [2, 7, 9]])
print(flip('L', box)) # [[3, 2, 1],
                     #  [5, 4, 1],
                     #  [6, 5, 3],
                     #  [9, 7, 2]])
print(flip('U', box)) #[[7, 5, 9],
                       #[6, 5, 3],
                       #[4, 3, 2],
                       #[1, 2, 1]])

print(flip('D', box)) #[[1, 2, 1],
                  #[4, 3, 2],
                  #[6, 5, 3],
                  #[7, 5, 9]])
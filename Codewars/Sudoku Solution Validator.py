# Sudoku Solution Validator
# Sudoku is a game played on a 9x9 grid.
# The goal of the game is to fill all cells of the grid with digits from 1 to 9,
# so that each column, each row, and each of the nine 3x3 sub-grids (also known as blocks)
# contain all of the digits from 1 to 9.
# Сделать проверку правильности судоку, а именно не в одной лини повторяющихся символов и в квадрате 3*3

def valid_solution(board):
    if len(board) == 0 or len(board[0]) == 0:   # проверка на пустоту
        return False

    for i in range(0, 9):
        horizont, vertical = {}, {}   # горизонт и вертикаль

        for j in range(0, 9):       # благодаря i и j мы перемещаемся на +1 и добовляем в словарь
            if board[i][j] == 0:    # проверка на нулевой эллемент
                return False
            elif board[i][j] in horizont:   # проверка на повтор
                return False
            else:
                horizont[board[i][j]] = True  # а вот если все хорошо, то записываем эллемент

            if board[j][i] == 0:    # проверка на ноль эллемент
                return False
            elif board[j][i] in vertical:   # проверка на повтор
                return False
            else:
                vertical[board[j][i]] = True  # а вот если все хорошо, то записываем эллемент

    for m in range(0, 3):
        for n in range(0, 3):
            square_three = {}
            for i in range(m*3, m*3 + 3):       # 0 умножив на 3 будет ноль, а дальше будет три и шесть
                for j in range(n*3, n*3 + 3):   # и так же range +3 ограничение тоже остается
                    if board[i][j] == 0:        # если оказался ноль, то провал
                        return False
                    elif board[i][j] in square_three:   # если оказался повтор, то ливаем
                        return False
                    else:                       # а вот если все хорошо, то записываем эллемент
                        square_three[board[i][j]] = True

    return True




print(valid_solution([
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]]))  # True

print(valid_solution([
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 0, 3, 4, 8],
    [1, 0, 0, 3, 4, 2, 5, 6, 0],
    [8, 5, 9, 7, 6, 1, 0, 2, 0],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 0, 1, 5, 3, 7, 2, 1, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 0, 0, 4, 8, 1, 1, 7, 9]]))  # False

print(valid_solution([
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 3, 5, 2, 8, 6, 1, 7, 9]]))  # False

print(valid_solution([
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 5]]))  # False

print(valid_solution([
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 2, 9]]))  # False

print(valid_solution([
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 1, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]]))  # False

print(valid_solution([
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 0]]))  # False

print(valid_solution([[]]))  # False

print(valid_solution([[ 1, 2, 3, 4, 5, 6, 7, 8, 9 ],
                      [ 2, 3, 1, 5, 6, 4, 8, 9, 7 ],
                      [ 3, 1, 2, 6, 4, 5, 9, 7, 8 ],
                      [ 4, 5, 6, 7, 8, 9, 1, 2, 3 ],
                      [ 5, 6, 4, 8, 9, 7, 2, 3, 1 ],
                      [ 6, 4, 5, 9, 7, 8, 3, 1, 2 ],
                      [ 7, 8, 9, 1, 2, 3, 4, 5, 6 ],
                      [ 8, 9, 7, 2, 3, 1, 5, 6, 4 ],
                      [ 9, 7, 8, 3, 1, 2, 6, 4, 5 ]]))  # False

print(valid_solution([[1, 3, 2, 5, 7, 9, 4, 6, 8],
                      [4, 9, 8, 2, 6, 0, 3, 7, 5],
                      [7, 0 , 6, 3, 8, 0, 2, 1, 9],
                      [6, 4, 3, 1, 5, 0, 7, 9, 2],
                      [5, 2, 1, 7, 9, 0, 8 , 4, 6],
                      [9, 8, 0, 4, 2, 6, 5, 3, 1],
                      [2, 1, 4, 9, 3, 5, 6, 8, 7],
                      [3, 6 , 0, 8, 1, 7, 9, 2, 4],
                      [8, 7, 0, 6, 4, 2, 1, 3, 5]]))

print(valid_solution([[45, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 45, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0,45, 0, 0],
                      [0,45, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0,45, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0,45, 0],
                      [0, 0,45, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0,45, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0,45]]))

print(valid_solution([[5, 5, 5, 5, 5, 5, 5, 5, 5],
                      [5, 5, 5, 5, 5, 5, 5, 5, 5],
                      [5, 5, 5, 5, 5, 5, 5, 5, 5],
                      [5, 5, 5, 5, 5, 5, 5, 5, 5],
                      [5, 5, 5, 5, 5, 5, 5, 5, 5],
                      [5, 5, 5, 5, 5, 5, 5, 5, 5],
                      [5, 5, 5, 5, 5, 5, 5, 5, 5],
                      [5, 5, 5, 5, 5, 5, 5, 5, 5],
                      [5, 5, 5, 5, 5, 5, 5, 5, 5]]))

print(valid_solution([[4, 3, 5, 6, 7, 8, 9, 1, 2],
                      [6, 7, 2, 1, 9, 5, 3, 4, 8],
                      [2, 9, 7, 3, 4, 2, 5, 6, 7],
                      [8, 5, 9, 7, 6, 1, 4, 2, 3],
                      [4, 2, 6, 8, 5, 3, 7, 9, 1] ,
                      [7, 1, 3, 9, 2, 4, 8, 5, 6],
                      [9, 6, 1, 5, 3, 7, 2, 8, 4],
                      [2, 8, 7, 4, 1, 9, 6, 3, 5],
                      [3, 4, 5, 2, 8, 6, 1, 7, 9]]))

print(valid_solution([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                         ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                         ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                         ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                         ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                         ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                         ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                         ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                         ,[8, 7, 9, 6, 4, 2, 1, 3, 5]]))

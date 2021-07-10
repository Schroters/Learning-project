# Validate Sudoku with size `NxN`
# Given a Sudoku data structure with size NxN, N > 0 and √N == integer,
# write a method to validate if it has been filled out correctly.
# Учитывая структуру данных судоку с размером, напишите метод для проверки правильности заполнения


class Sudoku(object):
    def __init__(self, data):
        self.board = data
    def is_valid(self):
        board = self.board
        if len(board) < 2 or len(board[0]) < 2:
            # Проверка на различные парвила, как порядок значения, буквы и размер
            if isinstance(board[0], list):      # уточняем матрица вообще или нет
                if isinstance(board[0][0], str) or isinstance(board[0][0], bool) or board[0][0] != 1:
                    # если строка, bool или не равно единице
                    return False
                return True
            elif not isinstance(board[0], list):    # если НЕ матрица - провал
                return False
            else:
                 return True

        for i in range(0, len(board)):      # Проверив исключения идем проверять сам судоку
            horizont, vertical = {}, {}     # горизонт и вертикаль

            for j in range(0, len(board)):       # благодаря i и j мы перемещаемся на +1 и добовляем в словарь
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
        if len(board) % 3 == 0 and len(board[0]) % 3 == 0:  # проверка на маленькие квадраты только при полном судоку
            for m in range(0, (len(board) // 3)):
                for n in range(0, (len(board[0]) // 3)):
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


goodSudoku1 = Sudoku([
    [7,8,4, 1,5,9, 3,2,6],
    [5,3,9, 6,7,2, 8,4,1],
    [6,1,2, 4,3,8, 7,5,9],

    [9,2,8, 7,1,5, 4,6,3],
    [3,5,7, 8,4,6, 1,9,2],
    [4,6,1, 9,2,3, 5,8,7],

    [8,7,6, 3,9,4, 2,1,5],
    [2,4,3, 5,6,1, 9,7,8],
    [1,9,5, 2,8,7, 6,3,4]
])
goodSudoku2 = Sudoku([
    [1, 4, 2, 3],
    [3, 2, 4, 1],
    [4, 1, 3, 2],
    [2, 3, 1, 4]
])

badSudoku1 = Sudoku([
    [0,2,3, 4,5,6, 7,8,9],
    [1,2,3, 4,5,6, 7,8,9],
    [1,2,3, 4,5,6, 7,8,9],

    [1,2,3, 4,5,6, 7,8,9],
    [1,2,3, 4,5,6, 7,8,9],
    [1,2,3, 4,5,6, 7,8,9],

    [1,2,3, 4,5,6, 7,8,9],
    [1,2,3, 4,5,6, 7,8,9],
    [1,2,3, 4,5,6, 7,8,9]
])      # Нарушение правил
badSudoku2 = Sudoku([
    [1,2,3,4,5],
    [1,2,3,4],
    [1,2,3,4],
    [1]
])      # Нарушение правил
goodSudoku3 = Sudoku([[1]])     # 1x1
badSudoku4 = Sudoku([['']])     # Пусто
badSudoku5 = Sudoku([3])        # Нарушен порядок
badSudoku6 = Sudoku([[True]])   # Нет цифр
goodSudoku4 = Sudoku([[7, 8, 4, 1, 5, 9, 3, 2, 6],
                     [5, 3, 9, 6, 7, 2, 8, 4, 1],
                     [6, 1, 2, 4, 3, 8, 7, 5, 9],
                     [9, 2, 8, 7, 1, 5, 4, 6, 3],
                     [3, 5, 7, 8, 4, 6, 1, 9, 2],
                     [4, 6, 1, 9, 2, 3, 5, 8, 7],
                     [8, 7, 6, 3, 9, 4, 2, 1, 5],
                     [2, 4, 3, 5, 6, 1, 9, 7, 8],
                     [1, 9, 5, 2, 8, 7, 6, 3, 4]])
badSudoku8 = Sudoku([[2], ])     # Нарушен порядок
badSudoku9 = Sudoku([[''], ])    # Пусто
badSudoku10 = Sudoku([[0], ])    # Нарушен порядок
badSudoku11 = Sudoku([[True], ])  # Нет цифр
badSudoku12 = Sudoku([[1, 4, 4, 3, 'a'],
                      [3, 2, 4, 1],
                      [4, 1, 3, 3],
                      [2, 0, 1, 4],
                      ['', False, None, '4']])      # Иные символы
badSudoku13 = Sudoku([[1, 2, 3, 4, 5, 6, 7, 8, 9],
                      [2, 3, 1, 5, 6, 4, 8, 9, 7],
                      [3, 1, 2, 6, 4, 5, 9, 7, 8],
                      [4, 5, 6, 7, 8, 9, 1, 2, 3],
                      [5, 6, 4, 8, 9, 7, 2, 3, 1],
                      [6, 4, 5, 9, 7, 8, 3, 1, 2],
                      [7, 8, 9, 1, 2, 3, 4, 5, 6],
                      [8, 9, 7, 2, 3, 1, 5, 6, 4],
                      [9, 7, 8, 3, 1, 2, 6, 4, 5]])     # Нарушение правил


print('goodSudoku1 tr', goodSudoku1.is_valid())
print('goodSudoku2 tr', goodSudoku2.is_valid())
print('goodSudoku3 tr', goodSudoku3.is_valid())
print('goodSudoku4 tr', goodSudoku4.is_valid())
print('badSudoku1 fls', badSudoku1.is_valid())
print('badSudoku2 fls', badSudoku2.is_valid())
print('badSudoku4 fls', badSudoku4.is_valid())
print('badSudoku5 fls', badSudoku5.is_valid())
print('badSudoku6 fls', badSudoku6.is_valid())
print('badSudoku8 fls', badSudoku8.is_valid())
print('badSudoku9 fls', badSudoku9.is_valid())
print('badSudoku10 fls', badSudoku10.is_valid())
print('badSudoku11 fls', badSudoku11.is_valid())
print('badSudoku12 fls', badSudoku12.is_valid())
print('badSudoku13 fls', badSudoku13.is_valid())

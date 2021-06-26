# TV Remote (shift and space)
# How many button presses on my remote are required to type a given?
# Сколько нажатий кнопок на моем пульте дистанционного управления необходимо, чтобы ввести заданное значение?
# Появились кнопки изменения размера и пробел
def tv_remote(word):
    remote = [['a', 'b', 'c', 'd', 'e', '1', '2', '3'],
              ['f', 'g', 'h', 'i', 'j', '4', '5', '6'],
              ['k', 'l', 'm', 'n', 'o', '7', '8', '9'],
              ['p', 'q', 'r', 's', 't', '.', '@', '0'],
              ['u', 'v', 'w', 'x', 'y', 'z', '_', '/'],
              ['aA', 'SP', '', '', '', '', '', '']]
    sym = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '@', '0', '_', '/']    # символы без регистра
    cnt, sustep, biglet, spale = 0, 0, 0, 0    # счетчик по строкам, сумма шагов, буква была большой или нет
    corl = []                                  # координаты буквы верт и горизонт
    if len(word) == 0:
        return 0

    for let in word:
        cnt = 0     # обнуляем для нового индекса
        while cnt != 6:
            if let in remote[cnt]:  # есть ли маленькая
                if any((c in sym) for c in let):    # проверка на спецсимволы, что бы не обнулить память больших
                    corl += [[remote[cnt].index(let.lower()) + 1, cnt + 1]]
                    cnt = 5
                else:           # если буквы
                    if biglet == 1:
                        corl += [[remote[5].index('aA') + 1, 6]]    # если прошлая большая то идем снова до Аа
                        corl += [[remote[cnt].index(let.lower()) + 1, cnt + 1]]
                        biglet, cnt = 0, 5  # биг 0 так как символ маленький и к счетчику пять что бы выйти
                    elif biglet == 0:   # прошлая маленькая
                        corl += [[remote[cnt].index(let) + 1, cnt + 1]]     # добавили координаты в матрицу
                        biglet, cnt = 0, 5  # биг, так как маленькая

            elif let not in remote[cnt]:
                if let.lower() in remote[cnt]:      # проверка есть ли большая
                    if biglet == 1:                 # уже были большие или нет
                        corl += [[remote[cnt].index(let.lower()) + 1, cnt + 1]]
                        biglet, cnt = 1, 5  # оставляем биг 1 так как символ большой

                    elif biglet == 0:   # прошлая маленькая
                        corl += [[remote[5].index('aA') + 1, 6]]    # если большая прошлой нет, то прибавялем координат
                        corl += [[remote[cnt].index(let.lower()) + 1, cnt + 1]]
                        biglet, cnt = 1, 5  # биг 1 так как символ большой и к счетчику пять что бы выйти

                elif let == ' ':
                    corl += [[remote[5].index('SP') + 1, 6]]
                    spale, cnt = 1, 5

            cnt += 1

    sustep += sum(corl[0]) - 1      # добавили первую букву
    for i in range(1, len(corl)):
        vrsum = (abs(corl[i][0] - corl[i-1][0]) + abs(corl[i][1] - corl[i-1][1])) + 1   # сложили прошлую координату с нынешней
        sustep += vrsum     # прибавили разницу в общую сумму

    return sustep


print(tv_remote('Solution'))            # 49
print(tv_remote('yad9@w3L7NbSPfLN2'))   # 132
print(tv_remote(''))
print(tv_remote(' / @M@L@l'))

# TV Remote 1 https://www.codewars.com/kata/tv-remote
# How many button presses on my remote are required to type a given?
# Сколько нажатий кнопок на моем пульте дистанционного управления необходимо, чтобы ввести заданное значение?
def tv_remote(word):
    remote = [['a', 'b', 'c', 'd', 'e', '1', '2', '3'],
              ['f', 'g', 'h', 'i', 'j', '4', '5', '6'],
              ['k', 'l', 'm', 'n', 'o', '7', '8', '9'],
              ['p', 'q', 'r', 's', 't', '.', '@', '0'],
              ['u', 'v', 'w', 'x', 'y', 'z', '_', '/']]
    count, sustep = 0, 0                    # счетчик по строкам и сумма шагов
    corl = []                               # координаты буквы верт и горизонт

    for let in word:
        count = 0
        while count != 5:
            if let in remote[count]:
                corl += [[remote[count].index(let) + 1, count + 1]]     # добавили координаты в матрицу
                count = 4
            count += 1

    sustep += sum(corl[0]) - 1      # добавили первую букву

    for i in range(1, len(word)):
        vrsum = (abs(corl[i][0] - corl[i-1][0]) + abs(corl[i][1] - corl[i-1][1])) + 1   # сложили прошлую координату с нынешней
        sustep += vrsum     # прибавили разницу в общую сумму

    return sustep


print(tv_remote('codewars'))    # 36
print(tv_remote('does'))        # 16
print(tv_remote('your'))        # 23
print(tv_remote('solution'))    # 33
print(tv_remote('work'))        # 20
print(tv_remote('for'))         # 12
print(tv_remote('these'))       # 27
print(tv_remote('words'))       # 25
print(tv_remote('lpoh3'))       # 24
print(tv_remote('otpd'))        # 21
print(tv_remote('7jwp'))        # 21
print(tv_remote('e6xq'))        # 22
print(tv_remote('lnqz'))        # 17
print(tv_remote('iq'))          # 10
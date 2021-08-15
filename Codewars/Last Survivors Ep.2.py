# Last Survivors Ep.2
# https://www.codewars.com/kata/60a1aac7d5a5fc0046c89651
# Substitute two equal letters by the next letter of the alphabet (two letters convert to one)
# Замените две равные буквы следующей буквой алфавита (две буквы преобразуются в одну)


def last_survivors(string):
    let_arr = list(string)
    counter, exit_while, temp_st = 0, len(let_arr), ''
    while counter < exit_while:
        if let_arr.count(let_arr[counter]) > 1:
            temp_st = let_arr[counter]  # временное хранение переменной
            if ord(temp_st) == 122:     # если последняя буква, то А
                let_arr[counter] = 'a'
                let_arr.remove(temp_st)
            else:
                let_arr[counter] = chr(ord(temp_st)+1)              # следующая буква
                let_arr.remove(temp_st)                             # удаление второго повтора
            counter = 0         # обнуляем, что бы начать с нуля

        counter += 1            # если повтора нет, продолжаем
        exit_while = len(let_arr)   # меняется размер списка, меняется и ограничитель

    return ''.join(let_arr)

print(last_survivors('abaa'))   # ac
print(last_survivors('zzab'))   # c
print(last_survivors('zzzab'))  # cz
print(last_survivors(''))       # ''
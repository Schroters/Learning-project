# Decode the Morse code
# https://www.codewars.com/kata/54b724efac3d5402db00065e
# You have to write a simple Morse code decoder. Вы должны написать простой декодер кода Морзе.

morse_dict = {'A':'.-', 'B':'-...',
              'C':'-.-.', 'D':'-..', 'E':'.',
              'F':'..-.', 'G':'--.', 'H':'....',
              'I':'..', 'J':'.---', 'K':'-.-',
              'L':'.-..', 'M':'--', 'N':'-.',
              'O':'---', 'P':'.--.', 'Q':'--.-',
              'R':'.-.', 'S':'...', 'T':'-',
              'U':'..-', 'V':'...-', 'W':'.--',
              'X':'-..-', 'Y':'-.--', 'Z':'--..',
              '1':'.----', '2':'..---', '3':'...--',
              '4':'....-', '5':'.....', '6':'-....',
              '7':'--...', '8':'---..', '9':'----.',
              '0':'-----', ', ':'--..--', '.':'.-.-.-',
              '?':'..--..', '/':'-..-.', '-':'-....-',
              '(':'-.--.', ')':'-.--.-', 'SOS':'...---...', '':'', '!':'-.-.--'}


def decodeMorse(morse_code):
    morse_code_arr, result = morse_code.split(' '), []
    for i in morse_code_arr:
        if len(i) != 0:     # имеет значение записываем в список
            for alphabet, mors in morse_dict.items():
                if i == mors:
                    result.append(alphabet)
        elif len(i) == 0:   # если пусто то делаем пробел
            result.append(' ')
    for i in reversed(range(0, len(result)-1)):    # удаление повторных пробелов
        if result[i].isspace():
            if result[i] == result[i+1]:
                del result[i]

    if result[0].isspace():
        del result[0]
    if result[-1].isspace():
        del result[-1]

    result = ''.join(result)    # создаем строку

    return result


print(decodeMorse('.... . -.--   .--- ..- -.. .'))  # 'HEY JUDE'
print(decodeMorse(' . .'))  # E E
print(decodeMorse('.     .'))   # E E
print(decodeMorse('      ...---... -.-.--   - .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.-     '))
# SOS! THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.
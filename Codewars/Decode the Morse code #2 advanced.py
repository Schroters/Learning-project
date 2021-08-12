# Decode the Morse code #2 advanced
# https://www.codewars.com/kata/decode-the-morse-code-advanced
# You have to write a Morse code decoder for wired electrical telegraph.
# Вы должны написать декодер кода Морзе для проводного электрического телеграфа.

def dict_morse(letter):
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

    for alphabet, mors in morse_dict.items():
        if letter == mors:
            return alphabet


def decodeMorse(morseCode):
    morse_words = morseCode.split("   ")    # делим на слова, убирая три пробела
    morse_words = list(filter(None, morse_words))    # удаляем пробелы
    norm_letter, normal_sentence = '', []     # для слова и полученное предложение

    for morse_word in morse_words:
        morse_word = morse_word.lstrip().rstrip()     # удаление вначале и в конце пробелов
        morse_letters = morse_word.split(" ")  # сделали список с каждой буквой отдельно
        for letter in morse_letters:    # по каждой букве в слове прошлись
            norm_letter += dict_morse(letter)    # добавили в строку букву на норм
        normal_sentence.append("".join(norm_letter))  # добавляем слово которое получилось
        norm_letter = ''        # обнуляем строку

    return " ".join(normal_sentence).strip()


def decode_bits(bits):
    bit = bits.strip('0')   # удаляем нули с конца и сначала строки
    min_repeats = 888888    # единица измерения повторов
    count = 1       # счетчик повторов (с одного, так как повтор знч есть)
    for i in range(1, len(bit)):    # узнаем количество пробелов/повторов
        if bit[i] == bit[i-1]:  # сравнение эллементов
            count += 1
        else:
            if count < min_repeats:    # минимальное количество повторов берем за основу
                min_repeats = count
                count = 1
            else:
                count = 1

    morse_code = ''
    for word in bit.split('0'*min_repeats*7):  # умножаем на семь наш тайм, и разделяем слова
        for letter in word.split('0'*min_repeats*3):    # разделяем на буквы
            for chrPush in letter.split('0'*min_repeats):    # разделяем на отдельные нажатия и символы
                if chrPush == '1'*min_repeats:
                    morse_code += '.'
                elif chrPush == '1'*min_repeats*3:     # если повторяется по три, то значит тире
                    morse_code += '-'
                else:       # если не разобрались, то по условию задачи точка
                    morse_code += '.'
            morse_code += ' '   # пробел между символами
        morse_code += '   '     # пробел между словами
    return morse_code




print(decodeMorse(decode_bits('1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011')))
# HEY JUDE
print('\n', decodeMorse(decode_bits('1')), '\n')       # E
print('\n', decodeMorse(decode_bits('101')), '\n')     # I
print('\n', decodeMorse(decode_bits('10001')), '\n')   # EE
print('\n', decodeMorse(decode_bits('1110111')), '\n') # M
print('\n', decodeMorse(decode_bits('1110111')), '\n') # M
print('\n', decodeMorse(decode_bits('111')), '\n')     # E
print('\n', decodeMorse(decode_bits('1111111')), '\n')  # E
print('\n', decodeMorse(decode_bits('111110000011111')), '\n')     # E

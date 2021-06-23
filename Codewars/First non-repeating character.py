# First non-repeating character
# Function that takes a string input, and returns the first character that is not repeated anywhere in the string.
# Функция, которая принимает строковый ввод и возвращает первый символ, который не повторяется нигде в строке.
def first_non_repeating_letter(word):
    if len(word) <= 1:
        return word
    else:
        neword = sorted(word.lower())   # сортируем и
        dit, nl = dict(), []

        for letter in neword:
            if letter in dit:       # если есть слово в словаре, то прибавляем значение
                dit[letter] += 1
            else:               # если слова нет в словаре, то добавляем с значением 1
                dit[letter] = 1

        for el in dit:
            if dit[el] == 1:
                nl += el

        dit = dict()    # обнуление словаря для поиска индекса
        # если в спискe так и нет эллементов, значит одногоэлемента нет, значит возвращаем все пустое
        if len(nl) == 0:
            return ''
        else:
            for wo in nl:
                dit[wo] = word.lower().find(wo)


            minlet = min(dit, key=dit.get)  # поиск минимального эллемента в словаре

            return word[word.lower().find(minlet)]  # возвращаем повторяющегося символа с правильным регистром


print(first_non_repeating_letter('a'))
print(first_non_repeating_letter('stress'))
print(first_non_repeating_letter('moonmen'))

print(first_non_repeating_letter(''))

print(first_non_repeating_letter('abba'))
print(first_non_repeating_letter('aa'))

print(first_non_repeating_letter('~><#~><'))
print(first_non_repeating_letter('hello world, eh?'))
print()
print(first_non_repeating_letter('sTreSS'))
print(first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!'))


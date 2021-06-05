# https://stepik.org/lesson/3363/step/3?unit=1135
# https://stepik.org/lesson/3373/step/6?unit=956
# Counting duplicate words in a file (Подсчет повторяющихся слов в файле)
s, d = str(), dict()

with open("open.txt", "r") as f:
    s = f.read().lower().strip().split()   # прочли, уменьшили, убрали спец символы и все в список
s = s.lower().strip().split()
s.sort()    # отсортировали 
for word in s:
    if word in d:       # если есть слово в словаре, то прибавляем значение
        d[word] += 1
    else:               # если слова нет в словаре, то добавляем с значением 1
        d[word] = 1

# Сортировка не позволяет изменять порядок словаря на месте.
# Записываем упорядоченные пары в совершенно новый пустой словарь.

sorted_dict = dict()
sordickey = sorted(d, key=d.get)  # возвращает список ключей, значения сортируются по порядку
for w in reversed(sordickey):   # идем по отсортированным ключам в обратном порядке от большего к меньшему
    sorted_dict[w] = d[w]    # и в новый отсорт.словарь добавляем, значения по ключу


print(sorted_dict)
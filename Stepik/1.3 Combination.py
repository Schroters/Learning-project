# https://stepik.org/lesson/24459/step/15?unit=6764
# Combination
# Сочетанием из n элементов по k называется подмножество этих n элементов размера k.
# Два сочетания называются различными, если одно из сочетаний содержит элемент, который не содержит другое.
# Числом сочетаний из n по k называется количество различных сочетаний из n по k

n, k = map(int, input().split())
sumn, sumk = 1, 1
for i in reversed(range((n-k+1), n+1)):
    sumn *= i
for j in range(1, (k+1)):
    sumk *= j

print(int(sumn/sumk))

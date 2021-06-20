# IQ Test
# Program that among the given numbers finds one that is different in evenness, and return a position of this number
# Программа должна найти число одно, которое отличается по четности и вывести его позицию

a = "2 4 7 8 10"
a1 = '1 2 2'
a2 = '1 2 1 1'

def iq_test(numbers):
    ms = numbers.split()
    odd = 0     # нечет
    eve = 0     # чет
    print(ms)

    for i in ms:
        if int(i) % 2 == 0:
            eve += 1
            evenum = i
        else:
            odd += 1
            oddnum = i
    if eve > odd:
        return (ms.index(str(oddnum))+1)
    elif odd > eve:
        return (ms.index(str(evenum))+1)


print(iq_test(a))
print(iq_test(a1))
print(iq_test(a2))

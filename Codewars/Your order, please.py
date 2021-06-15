#Your order, please
#test.assert_equals(order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")
#test.assert_equals(order("4of Fo1r pe6ople g3ood th5e the2"), "Fo1r the2 g3ood 4of th5e pe6ople")
#test.assert_equals(order(""), "")


def order(sentence):
    ms = sentence.split()   # изначальный список
    nms = [''] * len(ms)    # пустой список

    for i in range(len(ms)):
        for j in range(len(ms[i])):
            if ms[i][j].isdigit():
                nms[int(ms[i][j])-1] = ms[i]    # по индексу в новый список

    return ' '.join(nms)    # превратили список в с трочку

print(order('is2 Thi1s T4est 3a'))
print(order('4of Fo1r pe6ople g3ood th5e the2'))
print(order(''))
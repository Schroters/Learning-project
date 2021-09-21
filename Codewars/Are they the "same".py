# Are they the "same"?
# Function that checks whether the two arrays have the "same" elements, with the same multiplicities.
# "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.
# Функция, которая проверяет, имеют ли два массива «одинаковые» элементы с одинаковой кратностью.
# "То же" означает, что элементы в b - это элементы в квадрате, независимо от порядка.
a1 = [121, 144, 19, 161, 19, 144, 19, 11]
b1 = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
a2 = [121, 144, 19, 161, 19, 144, 19, 11]
b2 = [132, 14641, 20736, 361, 25921, 361, 20736, 361]
a3 = [121, 144, 19, 161, 19, 144, 19, 11]
b3 = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]
a4 = None
b4 = None
a5 = {}
b5 = {}
a6 = [2, 2, 3]
b6 = [4, 4, 9]
a7 = [2, 2, 3]
b7 = [4, 9, 9]


def comp(a, b):
    if a is None or b is None:
        return False

    a, b = sorted(a), sorted(b)
    tempa, tempb = a, b

    for ia in a:
        if ia*ia not in b:      # если нет квадрата в б то провал
            return False
        elif ia*ia in b:        # если есть
            if ia*ia in tempb:  # проверяем есть ил во временном
                tempb.remove(ia*ia)     # удаляем из временного B
            else:               # если нет во временном то провал
                return False

    if len(tempb) != 0:         # если чтото осталось, то провал
        return False

    for ib in b:
        if ib**0.5 not in a:    # если нет корня в а то провал
            return False

    return True


print(comp(a1, b1))
print(comp(a2, b2))
print(comp(a3, b3))
print(comp(a4, b4))
print(comp(a5, b5))
print(comp(a6, b6))
print(comp(a7, b7))

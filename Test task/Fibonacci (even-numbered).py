# Написать функцию возвращающую четные элементы последовательности Фибоначчи. Например, f(4) вернет 0,2,8,34

def f(number):
    f1 = f2 = 1
    result = [0]
    while len(result) < number:
        f1, f2 = f2, f1 + f2
        if f2 % 2 == 0:
            result.append(f2)
    return ",".join(map(lambda x: str(x), result))

print(f(4))
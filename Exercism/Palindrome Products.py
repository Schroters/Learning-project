# Palindrome Products
# https://exercism.org/tracks/python/exercises/palindrome-products

def section(min_factor, max_factor):  # поиск отрезков для цикла
    result = list([min_factor])
    difference = (max_factor+1 - min_factor) // 4
    for _ in range(3):
        min_factor = min_factor + difference
        result.append(min_factor)
    result.append(max_factor+1)
    return result


def find_factors(value, min_factor, max_factor):        # поиск для нужного эллемента множителей
    factors = []
    for coefficient in range(min_factor, max_factor):
        if value % coefficient == 0 and (min_factor <= (value // coefficient) <= max_factor):
            factors.append([coefficient, value // coefficient])
    return factors


def smallest(min_factor, max_factor):
    numb_test(min_factor, max_factor)
    start, stop = 0, 1
    select = section(min_factor, max_factor)
    for _ in range(4):
        for i in range(select[start], select[stop]):
            for j in range(select[start], select[stop]):
                numb = str(i * j)
                if numb == numb[::-1]:
                    return int(numb), find_factors(int(numb), min_factor, max_factor)
        start += 1
        stop += 1
    return None, []


def largest(min_factor, max_factor):
    numb_test(min_factor, max_factor)
    start, stop = -2, -1
    select = section(min_factor, max_factor)
    for _ in range(4):
        for i in reversed(range(select[start], select[stop])):
            for j in reversed(range(select[start], select[stop])):
                numb = str(i * j)
                if numb == numb[::-1]:
                    return int(numb), find_factors(int(numb), min_factor, max_factor)
        start -= 1
        stop -= 1
    return None, []


def numb_test(min_factor, max_factor):      # тест по условиям
    if min_factor > max_factor:
        raise ValueError("Value Error!")


print(smallest(1000, 9999))     # (1002001, [[1001, 1001]])
print(largest(100, 999))    # (906609, [[913, 993], [993, 913]])
print(largest(1, 9))        # (9, [[1, 9], [3, 3]])
print(smallest(1, 9))       # (1, [[1, 1]])
print(largest(10, 99))      # (9009, [[91, 99]])
print(smallest(10, 99))     # (121, [[11, 11]])
value, factors = largest(min_factor=1, max_factor=9)
print(value)                # 9
print(factors)              # [[1, 9], [3, 3]]

print(smallest(1002, 1003))     # (None, [])
print(largest(15, 15))          # (None, [])
print(smallest(10000, 1))       # ValueError
print(largest(2, 1))            # ValueError

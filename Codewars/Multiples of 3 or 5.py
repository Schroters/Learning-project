# Multiples of 3 or 5
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in
# Возвращает сумму всех кратных 3 или 5 числам ниже переданного числа

def solution1(number):
    s = 0
    if number > 0:
        for i in range(number):
            if (i % 3) == 0:
                s += i
                continue
            if i % 5 == 0:
                s += i
                continue

    return s

def solution2(number):
    s = 0
    if number > 0:
        for i in range(number):
            if i % 3 == 0 or i % 5 == 0:
                s += i

    return s

print(solution1(10))
print(solution1(16))

print(solution2(10))
print(solution2(16))
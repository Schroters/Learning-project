# Collatz Conjecture
# https://exercism.org/tracks/python/exercises/collatz-conjecture

def steps(number):
    count = 0
    if number < 1:
        raise ValueError('ValueError')
    while number != 1:
        if number % 2 == 0:
            number = number / 2
        else:
            number = number * 3 + 1
        count += 1
    return count


print(steps(12))    # 9
print(steps(1))     # 0
print(steps(16))    # 4
print(steps(1000000))     # 152
print(steps(0))     # ValueError
print(steps(-15))   # ValueError

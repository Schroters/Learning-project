# Grains
# https://exercism.org/tracks/python/exercises/grains


def square(number):
    if 0 >= number or 64 < number:
        raise ValueError('The number must be from 1 to 64')
    else:
        return 2**(number-1)


def total():
    return 18446744073709551615


print(total())
print(square(9))
print(square(-1))
print(square(64))
print(square(0))
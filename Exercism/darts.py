# Darts
# https://exercism.org/tracks/python/exercises/darts

def score(x, y):
    r = (x*x + y*y) ** 0.5
    if r <= 1:
        return 10
    if 5 >= r > 1:
        return 5
    if 10.0 >= r > 5:
        return 1
    return 0


print(score(-9, -9))
print(score(0, 10))
print(score(-5, 0))
print(score(-3.5, 3.5))

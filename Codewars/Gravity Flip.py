# Gravity Flip
# Given the initial configuration of the cubes in the box,
# find out how many cubes are in each of the n columns after Bob switches the gravity.
# Кубики перемещаются в сторону

def flip(d, a):
    if d == 'R':
        a = sorted(a)
    elif d == 'L':
        a = sorted(a, reverse=True) # обратная сортировка

    return a

print(flip('R', [3, 2, 1, 2]))
print(flip('L', [1, 4, 5, 3, 5]))
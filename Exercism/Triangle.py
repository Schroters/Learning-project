# Triangle
# https://exercism.org/tracks/python/exercises/triangle

def equilateral(sides):
    if 0 in sides:
        return False
    elif sides[0] == sides[1] and sides[1] == sides[2]:
        return True
    return False


def isosceles(sides):
    if (0 in sides) or triangle_inequality(sides):
        return False
    elif sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]:
        return True
    return False


def scalene(sides):
    if (0 in sides) or triangle_inequality(sides) or equilateral(sides) or isosceles(sides):
        return False
    return True


def triangle_inequality(sides):
    if (sides[0] + sides[1] < sides[2]) or (sides[2] + sides[1] < sides[0]) or (sides[0] + sides[2] < sides[1]):
        return True
    return False

# Sublist
# https://exercism.org/tracks/python/exercises/sublist
SUBLIST = "A is a sublist of B"
SUPERLIST = "A is a superlist of B"
EQUAL = "A is equal to B"
UNEQUAL = "A is not a superlist of, sublist of or equal to B"


def sublist(list_one, list_two):
    line_one = ', '.join(str(e) for e in list_one)
    line_two = ', '.join(str(e) for e in list_two)
    if line_one == line_two:
        return EQUAL
    elif (len(line_one) == 0) or (line_one in line_two):
        return SUBLIST
    elif (len(line_two) == 0) or (line_two in line_one):
        return SUPERLIST
    else:
        return UNEQUAL


print(sublist([1, 2, 3], [1, 2, 3, 4, 5]))  # A is a sublist of B
print(sublist([3, 4, 5], [1, 2, 3, 4, 5]))  # A is a sublist of B
print(sublist([3, 4], [1, 2, 3, 4, 5]))     # A is a sublist of B
print(sublist([1, 2, 5], [0, 1, 2, 3, 1, 2, 5, 6]))     # A is a sublist of B
print(sublist([], [1, 2, 3]))               # A is a sublist of B
print(sublist([1, 1, 2], [0, 1, 1, 1, 2, 1, 2]))    # A is a sublist of B
print(sublist([1, 2, 3], [1, 2, 3]))        # A is equal to B
print(sublist([], []))                      # A is equal to B
print(sublist([1, 3, 4], []))               # A is a superlist of B
print(sublist([1, 2, 3, 4, 5], [2, 3, 4]))  # A is a superlist of B
print(sublist([1, 2, 4], [1, 2, 3, 4, 5]))  # A is not a superlist of, sublist of or equal to B
print(sublist([1, 3], [1, 2, 3]))           # A is not a superlist of, sublist of or equal to B
print(sublist([1, 2, 3], [1, 3]))           # A is not a superlist of, sublist of or equal to B
print(sublist([1, 2, 3], [2, 3, 4]))        # A is not a superlist of, sublist of or equal to B
print(sublist([1, 0, 1], [10, 1]))          # A is not a superlist of, sublist of or equal to B

# Nice Array
# https://www.codewars.com/kata/59b844528bcb7735560000a0

def is_nice(arr):
    if (len(arr) == 0) or (arr.count(0) == len(arr)):
        return False
    for i in arr:
        if (i + 1 not in arr) and (i - 1 not in arr):
            return False
    return True


print(is_nice([2, 10, 9, 3]))  # True
print(is_nice([2, 10, 9, 4]))  # False
print(is_nice([3, 4, 5, 7]))   # False
print(is_nice([]))             # False
print(is_nice([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))  # False

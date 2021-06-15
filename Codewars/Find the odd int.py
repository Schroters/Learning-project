# Find the odd int
# Given an array of integers, find the one that appears an odd number of times.
# Учитывая массив целых чисел, найдите то, которое появляется нечетное число раз.
from collections import Counter

def find_it(seq):
    counter = Counter(seq)
    for i in counter:
        if counter[i] % 2 != 0:
            newi = i

    return newi


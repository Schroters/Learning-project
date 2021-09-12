# Highest and Lowest
# https://www.codewars.com/kata/554b4ac871d6813a03000035
# In this little assignment you are given a string of space separated numbers,
# and have to return the highest and lowest number.


def high_and_low(numbers):
    numbers = list(map(int, numbers.split()))
    return str(max(numbers)) + ' ' + str(min(numbers))


print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))
print(high_and_low("1 2 3"))

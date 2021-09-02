# Previous multiple of three
# https://www.codewars.com/kata/61123a6f2446320021db987d/python
# Given a positive integer n: 0 < n < 1e6,
# remove the last digit until you're left with
# a number that is a multiple of three.


def prev_mult_of_three(n):
    nuer = list(str(n))
    for i in reversed(range(len(nuer))):
        if int(''.join(nuer[:i+1])) % 3 == 0:
            return int(''.join(nuer[:i+1]))
        elif i == len(nuer):
            return None


print(prev_mult_of_three(1))       # None
print(prev_mult_of_three(25))      # None
print(prev_mult_of_three(36))      # 36
print(prev_mult_of_three(1244))    # 12
print(prev_mult_of_three(952406))  # 9

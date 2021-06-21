# Sum of Digits / Digital Root
# Given n, take the sum of the digits of n.
# If that value has more than one digit, continue reducing in this way until a single-digit number is produced.
# The input will be a non-negative integer.
# Пока не будет одной цифры, сумма цифр
def digital_root(n):
    n = str(n)
    sumi = 0
    while len(n) != 1:
        for i in n:
            sumi += int(i)

        n = str(sumi)
        sumi = 0

    return int(n)


print(digital_root(16))     # 7
print(digital_root(942))    # 6
print(digital_root(132189)) # 6
print(digital_root(493193)) # 2
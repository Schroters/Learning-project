# Pairs of integers from m to n
# https://www.codewars.com/kata/588e2a1ad1140d31cb00008c
# Implement a function that receives two integers m and n and generates a
# sorted list of pairs (a, b) such that m <= a <= b <= n

m = 2
n = 4
result = [(2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]

# result = []
print(result)
result.append((4, 5))

print(result[2][1])
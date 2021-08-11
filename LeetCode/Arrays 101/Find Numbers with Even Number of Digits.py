# Find Numbers with Even Number of Digits
# https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3237/
# Given an array nums of integers, return how many of them contain an even number of digits
# Дан массив целых чисел, верните, сколько из них содержат четное количество цифр


class Solution(object):
    def findNumbers(self, nums):
        count_even = 0
        for i in nums:
            if len(str(i)) % 2 == 0:
                count_even += 1

        return count_even


print(Solution().findNumbers([12, 345, 2, 6, 7896]))
print(Solution().findNumbers([555, 901, 482, 1771]))
print(Solution().findNumbers([]))
print(Solution().findNumbers([12]))
print(Solution().findNumbers([6]))
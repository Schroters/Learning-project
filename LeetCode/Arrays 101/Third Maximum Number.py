# Third Maximum Number
# https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3231/
# Given integer array nums, return the third maximum number in this array.
# If the third maximum does not exist, return the maximum number.
# Учитывая целые числа массива, вернуть третье максимальное число в этом массиве.
# Если третьего максимума не существует, верните максимальное число.


class Solution(object):
    def thirdMax(self, nums):
        noduplicates = list(set(nums))
        if len(noduplicates) == 0:
            return noduplicates
        elif len(noduplicates) < 3:
            return max(noduplicates)
        else:
            noduplicates.sort()
            return noduplicates[-3]


print(Solution().thirdMax([3, 2, 1]))   # 1
print(Solution().thirdMax([1, 2]))  # 2
print(Solution().thirdMax([2, 2, 3, 1]))    # 1
print(Solution().thirdMax([2, 2, 3, 1, 4, 6, 2, 3, 7, 9, 1, 5, 7, 2]))  # 6
print(Solution().thirdMax([1, 1, 2]))    # 2
print(Solution().thirdMax([-1, 2, 3]))  # -1
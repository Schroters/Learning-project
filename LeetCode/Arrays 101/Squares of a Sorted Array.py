# Squares of a Sorted Array
# https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3574/
# Given an integer array nums sorted in non-decreasing order,
# return an array of the squares of each number sorted in non-decreasing order.
# Учитывая целочисленный массив nums, отсортированный в неубывающем порядке,
# вернуть массив квадратов каждого числа, отсортированных в неубывающем порядке.


# the first one doesn't fit
class Solution_first(object):
    def sortedSquares(self, nums):
        return sorted(list(map(lambda x: x*x, nums)))

newTest1 = Solution_first()
print(newTest1.sortedSquares([-4, -1, 0, 3, 10]))   # [0, 1, 9, 16, 100]

newTest1 = Solution_first()
print(newTest1.sortedSquares([-7, -3, 2, 3, 11]))       # [4, 9, 9, 49, 121]


# second
class Solution_second(object):
    def sortedSquares(self, nums):
        return sorted([x*x for x in nums])


newTest1 = Solution_second()
print(newTest1.sortedSquares([-4, -1, 0, 3, 10]))   # [0, 1, 9, 16, 100]

newTest1 = Solution_second()
print(newTest1.sortedSquares([-7, -3, 2, 3, 11]))       # [4, 9, 9, 49, 121]


# third
class Solution_third(object):
    def sortedSquares(self, nums):
        nums = [abs(number) for number in nums]
        nums.sort()
        for i in range(len(nums)):
            nums[i] = nums[i]*nums[i]
        return nums

newTest1 = Solution_third()
print(newTest1.sortedSquares([-4, -1, 0, 3, 10]))   # [0, 1, 9, 16, 100]

newTest1 = Solution_third()
print(newTest1.sortedSquares([-7, -3, 2, 3, 11]))       # [4, 9, 9, 49, 121]

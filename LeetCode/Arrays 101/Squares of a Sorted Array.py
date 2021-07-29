# Squares of a Sorted Array
# https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3240/
# Given an integer array nums sorted in non-decreasing order,
# return an array of the squares of each number sorted in non-decreasing order.
# Учитывая целочисленный массив nums, отсортированный в неубывающем порядке,
# вернуть массив квадратов каждого числа, отсортированных в неубывающем порядке


class Solution(object):
    def sortedSquares(self, nums):
        return sorted(list(map(lambda x: x*x, nums)))


newTest1 = Solution()
print(newTest1.sortedSquares([-4,-1,0,3,10]))   # Output: [0,1,9,16,100]
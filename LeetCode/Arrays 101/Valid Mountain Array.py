# Valid Mountain Array
# https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3251/
# Given an array of integers arr, return true if and only if it is a valid mountain array.
# Учитывая массив целых чисел arr, вернуть true тогда и только тогда, когда это действительный горный массив.


class Solution(object):
    def validMountainArray(self, arr):
        mountain_top = max(arr)
        if arr.count(mountain_top) > 1 or len(arr) < 3 or arr.index(mountain_top) == len(arr)-1 or arr.index(mountain_top) == 0:
            # если больше двух вершин или маленький список или индекс вершины, является первым или последним эллементом
            return False
        for i in range(len(arr[:arr.index(mountain_top)])):    # в гору
            if arr[i] >= arr[i+1]:
                return False
        for i in range(arr.index(mountain_top), (len(arr))-1):    # с горы
            if arr[i] <= arr[i+1]:
                return False
        return True


print(Solution().validMountainArray([0, 2, 3, 4, 5, 2, 1, 0]))  # True
print(Solution().validMountainArray([0, 2, 3, 3, 5, 2, 1, 0]))  # False
print(Solution().validMountainArray([2, 1]))    # False
print(Solution().validMountainArray([3, 5, 5])) # False
print(Solution().validMountainArray([0, 3, 2, 1]))  # True
print(Solution().validMountainArray([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))    # False
print(Solution().validMountainArray([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))    # False
print(Solution().validMountainArray([1, 7, 9, 5, 4, 1, 2]))     # False
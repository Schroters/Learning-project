# Replace Elements with Greatest Element on Right Side
# https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3259/
# Given an array arr, replace every element in that array with the greatest element among the elements to its right,
# and replace the last element with -1.
# Учитывая массив arr, замените каждый элемент в этом массиве самым большим элементом среди элементов справа от него
# и замените последний элемент на -1.


class Solution(object):
    def replaceElements(self, arr):
        for i in range(len(arr)-1):
            arr[i] = max(arr[i+1:])
        arr[-1] = -1

        return arr


newTest1 = Solution()
print(newTest1.replaceElements([17, 18, 5, 4, 6, 1]))   # [18,6,6,6,1,-1]

newTest2 = Solution()
print(newTest2.replaceElements([400]))   # [-1]
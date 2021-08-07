# Merge Sorted Array
# https://leetcode.com/explore/learn/card/fun-with-arrays/525/inserting-items-into-an-array/3253/
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
# and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Вам даны два целых массива nums1и nums2, отсортированных в неубывающем порядке,
# и два целых числа mи n, представляющие количество элементов в nums1и nums2соответственно.
# Объединить nums1 и nums2в единый массив, отсортированный в неубывающем порядке.
# Do not return anything, modify nums1 in-place instead.


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        cnt = 0
        for i in range(m, len(nums1)):
            nums1[i] = nums2[cnt]
            cnt += 1

    def merge_old(self, nums1, m, nums2, n):        # first version
        for i in range(len(nums1) - m):
            del nums1[-1]
        for i in range(len(nums2) - n):
            del nums2[-1]
        nums1.extend(nums2)
        nums1.sort()


newTest1, newTest_1_List = Solution(), [1, 2, 3, 0, 0, 0]
newTest1.merge(newTest_1_List, 3, [2, 5, 6], 3)
print(newTest_1_List)      # [1,2,2,3,5,6]


newTest1, newTest_2_List = Solution(), [1]
newTest1.merge(newTest_2_List, 1, [], 0)
print(newTest_2_List)      # [1]

newTest1, newTest_3_List = Solution(), [0]
newTest1.merge(newTest_3_List, 0, [1], 1)
print(newTest_3_List)      # [1]
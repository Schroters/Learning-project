# Remove Element
# https://leetcode.com/explore/learn/card/fun-with-arrays/526/deleting-items-from-an-array/3247/
# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
# The relative order of the elements may be changed.
# Учитывая целочисленный массив nums и целое число val, удалите все вхождения val в nums на месте.
# Относительный порядок элементов может быть изменен.

class Solution(object):
    def removeElement(self, nums, val):
        count = []
        if val in nums:
            for i in range(len(nums)):  # пробежали по циклу
                if nums[i] == val:
                    count += [i]        # добавили место ненужного символа
        for i in reversed(count):       # и потом удалили все не нужные
            del nums[i]
        return len(nums)


newTest1 = Solution()
nt1n = [0, 1, 2, 2, 3, 0, 4, 2]
print(newTest1.removeElement(nt1n, 2))    # 5, nums = [0,1,4,0,3, _, _, _]
print(nt1n)

newTest2 = Solution()
nt2n = [3,2,2,3]
print(newTest2.removeElement(nt2n, 3))     # 2, nums = [2,2, _, _]
print(nt2n)
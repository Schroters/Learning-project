# Remove Element
# https://leetcode.com/explore/learn/card/fun-with-arrays/526/deleting-items-from-an-array/3247/
# and
# https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3575/
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

# and
class Solution_2(object):
    def removeElement(self, nums, val):
        if val in nums:
            for i in range(nums.count(val)):  # идем по количеству повторов
                nums.pop(nums.index(val))     # удаляем по индексу
        return len(nums)

newTest1 = Solution()
newTest_1_List = [0, 1, 2, 2, 3, 0, 4, 2]
print(newTest1.removeElement(newTest_1_List, 2))    # 5, nums = [0,1,4,0,3, _, _, _]
print(newTest_1_List)

newTest2 = Solution()
newTest_2_List = [3,2,2,3]
print(newTest2.removeElement(newTest_2_List, 3))     # 2, nums = [2,2, _, _]
print(newTest_2_List)

newTest1 = Solution_2()
newTest_1_List = [0, 1, 2, 2, 3, 0, 4, 2]
print(newTest1.removeElement(newTest_1_List, 2))    # 5, nums = [0,1,4,0,3, _, _, _]
print(newTest_1_List)

newTest2 = Solution_2()
newTest_2_List = [3,2,2,3]
print(newTest2.removeElement(newTest_2_List, 3))     # 2, nums = [2,2, _, _]
print(newTest_2_List)
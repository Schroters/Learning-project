# Move Zeroes
# https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3157/
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.
# Для целочисленного массива nums переместите все 0 в его конец, сохраняя относительный порядок ненулевых элементов.
# Обратите внимание, что вы должны сделать это на месте, не копируя массив.


nums = [0,1,0,3,12]     # [1,3,12,0,0]

class Solution(object):
    def moveZeroes(self, nums):
        for i in range(nums.count(0)):
            nums.append(0)
            nums.remove(0)

newTest1 = Solution()
newTest_1_List = [0,1,0,3,12]
newTest1.moveZeroes(newTest_1_List)
print(newTest_1_List)     # [1, 3, 12, 0, 0]

newTest2 = Solution()
newTest_2_List = [0]
newTest2.moveZeroes(newTest_2_List)
print(newTest_2_List)     # [0]

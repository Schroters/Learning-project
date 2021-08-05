# Sort Array By Parity
# https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3260/
# Given an integer array nums,
# move all the even integers at the beginning of the array followed by all the odd integers.
# Return any array that satisfies this condition.
# Учитывая целочисленный массив nums,
# переместите все четные целые числа в начало массива, а затем все нечетные целые числа.
# Верните любой массив, удовлетворяющий этому условию.


class Solution(object):
    def sortArrayByParity(self, nums):
        for i in reversed(range(len(nums))):
            if nums[i] % 2 != 0 or nums[i] == 1:
                nums.append(nums.pop(i))
        return nums     # не обязателен, меняется на месте, но по условию задачи


newTest1 = Solution()
newTest_1_List = [3, 1, 2, 4]
newTest1.sortArrayByParity(newTest_1_List)
print(newTest_1_List)     # [2,4,1,3] or [4,2,1,3]

newTest2 = Solution()
newTest_2_List = [0]
newTest2.sortArrayByParity(newTest_2_List)
print(newTest_2_List)     # [0]
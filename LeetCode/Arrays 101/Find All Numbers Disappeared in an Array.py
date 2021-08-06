# Find All Numbers Disappeared in an Array
# https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3270/
# Given an array nums of n integers where nums[i] is in the range [1, n],
# return an array of all the integers in the range [1, n] that do not appear in nums.
# Дан массив nums из n целых чисел, где nums [i] находится в диапазоне [1, n],
# вернуть массив всех целых чисел в диапазоне [1, n], которые не представлены в nums.


# the first long option
class Solution_long(object):
    def findDisappearedNumbers(self, nums):
        disappeared = []
        nums.sort()
        for i in range(1, len(nums)+1):
            if i not in nums:
                disappeared.append(i)
        return disappeared

newTest1 = Solution_long()
print(newTest1.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))  # [5, 6]

newTest1 = Solution_long()
print(newTest1.findDisappearedNumbers([1, 1]))  # [2]


# the second one after a while
class Solution(object):
    def findDisappearedNumbers(self, nums):
        for i in range(len(nums)):
            new_index = abs(nums[i]) - 1    # В new_index запишется индекс числа в for
            if nums[new_index] > 0:     # Минус
                nums[new_index] *= -1
        disappeared = []
        # Если число положительно, то добавляем его индекс в результат
        for i in range(1, len(nums) + 1):
            if nums[i - 1] > 0:     # что бы проверить с нулевого эллемента
                disappeared.append(i)    # чистое i так как числа без нуля, а индексирования с нуля

        return disappeared

newTest1 = Solution()
print(newTest1.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))  # [5, 6]

newTest1 = Solution()
print(newTest1.findDisappearedNumbers([1, 1]))  # [2]


# options after the submitted decision
class Solution_after(object):
    def findDisappearedNumbers(self, nums):
        set_=set(nums)
        missing=[]
        for i in range(1,len(nums)+1):
            if i not in set_:
                missing.append(i)
        return missing

newTest1 = Solution_after()
print(newTest1.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))  # [5, 6]

newTest1 = Solution_after()
print(newTest1.findDisappearedNumbers([1, 1]))  # [2]
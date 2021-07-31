# Remove Duplicates from Sorted Array
# https://leetcode.com/explore/learn/card/fun-with-arrays/526/deleting-items-from-an-array/3248/
# and
# https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3258/
# Given an integer array nums sorted in non-decreasing order,
# remove the duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same.
# Учитывая целочисленный массив, numsотсортированный в неубывающем порядке, удалите дубликаты на месте,
# чтобы каждый уникальный элемент появлялся только один раз.
# Относительный порядок элементов должен быть держал же.

class Solution(object):
    def removeDuplicates(self, nums):
        count = []
        for i in range(len(nums)-1):  # пробежали по циклу
            if nums[i] == nums[i+1]:
                count += [i]        # добавили место ненужного символа
        for i in reversed(count):
            del nums[i]

        return len(nums)


# and


class Solution_2(object):
    def removeDuplicates(self, numbers):
        cnt = len(numbers)-1
        while cnt > -1:
            if numbers.count(numbers[cnt]) > 1:
                drawb = numbers.count(numbers[cnt])-1   # количество повторов
                del numbers[(cnt-drawb):cnt]        # удаляем отрезок
                cnt -= drawb    # переключили счетчик
            cnt -= 1
        return len(numbers)

newTest1 = Solution()
newTest_1_List = [1, 1, 2]
print(newTest1.removeDuplicates(newTest_1_List))
print(newTest_1_List)     # [1,2,_]

newTest_2 = Solution()
newTest_2_List = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(newTest_2.removeDuplicates(newTest_2_List))
print(newTest_2_List)     # [0,1,2,3,4,_,_,_,_,_]

newTest1 = Solution_2()
newTest_1_List = [1, 1, 2]
print(newTest1.removeDuplicates(newTest_1_List))
print(newTest_1_List)     # [1,2,_]s

newTest_2 = Solution_2()
newTest_2_List = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(newTest_2.removeDuplicates(newTest_2_List))
print(newTest_2_List)     # [0,1,2,3,4,_,_,_,_,_]
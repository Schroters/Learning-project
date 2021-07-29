# Max Consecutive Ones
# https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3238/
# Given a binary array nums, return the maximum number of consecutive 1's in the array
# Для двоичного массива nums вернуть максимальное количество последовательных 1 в массиве


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        if nums.count(1) == 0:  # нет единиц нет смысла продолжать
            return 0
        if len(nums) == 1:      # проверка на пустоту
            if nums[0] == 1:
                return 1
        max_count, new_count = 0, 1     # два счетчика
        count_for = 1       # счетчик for
        for i in nums:
            if count_for < len(nums):
                if i == 1:      # если i = 1
                    if i == nums[count_for]:
                        new_count += 1
                    else:
                        if new_count >= max_count:  # если новые повтор больше или равен максимальному
                            max_count = new_count   # то передаем значение
                        new_count = 1           # и обнуляем
                count_for +=1

            # сверить последние повторения
            if new_count >= max_count:  # если новые повторю больше или равен максимальному
                max_count = new_count   # то передаем значение
        return max_count


new_test1 = Solution()
print(new_test1.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]))

new_test2 = Solution()
print(new_test2.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))

new_test3 = Solution()
print(new_test3.findMaxConsecutiveOnes([0]))

new_test4 = Solution()
print(new_test4.findMaxConsecutiveOnes([1]))

new_test5 = Solution()
print(new_test5.findMaxConsecutiveOnes([0, 0]))

new_test6 = Solution()
print(new_test6.findMaxConsecutiveOnes([]))
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


print(Solution().findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]))
print(Solution().findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
print(Solution().findMaxConsecutiveOnes([0]))
print(Solution().findMaxConsecutiveOnes([1]))
print(Solution().findMaxConsecutiveOnes([0, 0]))
print(Solution().findMaxConsecutiveOnes([]))
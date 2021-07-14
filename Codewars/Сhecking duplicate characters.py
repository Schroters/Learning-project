# Check for consecutive duplicate characters in the list
# Проверка на последовательные повторяющиеся символы в списке


class Solution(object):
    def findMaxConsecutive(self, nums):
        if len(nums) == 1:      # проверка на пустоту
            return 0
        max_count, new_count = 0, 1     # два счетчика
        count_for = 1       # счетчик для for
        for i in nums:
            if count_for < len(nums):
                if i == nums[count_for]:
                    new_count += 1
                else:
                    if new_count >= max_count:  # если новые повторюшкин больше или равен максимальному
                        max_count = new_count   # то передаем значение
                    new_count = 1           # и обнуляем
                count_for +=1

            # сверить последние повторения
            if new_count >= max_count:  # если новые повторюшкин больше или равен максимальному
                max_count = new_count   # то передаем значение

        return max_count


new_test1 = Solution()
print(new_test1.findMaxConsecutive([1, 0, 1, 1, 0, 1]))

new_test2 = Solution()
print(new_test2.findMaxConsecutive([1, 1, 0, 1, 1, 1]))

new_test3 = Solution()
print(new_test3.findMaxConsecutive([0]))

new_test4 = Solution()
print(new_test4.findMaxConsecutive([1]))

new_test5 = Solution()
print(new_test5.findMaxConsecutive([0, 0]))

new_test6 = Solution()
print(new_test6.findMaxConsecutive([]))

new_test7 = Solution()
print(new_test7.findMaxConsecutive([1, 2, 2, 1, 3, 3, 3, 4, 3]))
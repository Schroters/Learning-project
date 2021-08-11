# Check If N and Its Double Exist
# https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3250/
# Given an array arr of integers,
# check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).
# Учитывая массив arr целых чисел, проверьте, существует ли два целых числа, N и M такое,
# что N является двойным от M(т.е. N = 2 * M).


class Solution(object):
    def checkIfExist(self, arr):
        for i in arr:
            if i % 2 == 0 and i != 0:
                if (i // 2) in arr:
                    return True
        if arr.count(0) > 1:
            return True
        return False


print(Solution().checkIfExist([10, 2, 5, 3]))   # True
print(Solution().checkIfExist([7, 1, 14, 11]))  # True
print(Solution().checkIfExist([3, 1, 7, 11]))   # False
print(Solution().checkIfExist([-2, 0, 10, -19, 4, 6, -8]))      # False
print(Solution().checkIfExist([0, 0]))  # True

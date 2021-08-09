# Height Checker
# https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3228/
# Comparison of the sorted list with the original one. And the output of the difference.
# Сравнение отсортированного списка с исходным. И вывод разницы.


class Solution(object):
    def heightChecker(self, heights):
        sort_heights, cnt = sorted(heights), 0
        for i in range(len(heights)):
            if heights[i] != sort_heights[i]:
                cnt += 1
        return cnt


newTest1 = Solution()
print(newTest1.heightChecker([1, 1, 4, 2, 1, 3]))    # 3

newTest2 = Solution()
print(newTest2.heightChecker([5, 1, 2, 3, 4]))    # 5

newTest3 = Solution()
print(newTest3.heightChecker([1, 2, 3, 4, 5]))    # 0

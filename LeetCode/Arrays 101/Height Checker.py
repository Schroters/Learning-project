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


print(Solution().heightChecker([1, 1, 4, 2, 1, 3]))     # 3
print(Solution().heightChecker([5, 1, 2, 3, 4]))     # 5
print(Solution().heightChecker([1, 2, 3, 4, 5]))    # 0

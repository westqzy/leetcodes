#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 动态规划超时
        # n = len(height)
        # dp = [[0 for i in range(n)] for j in range(n)]
        # for i in range(1, n):
        #     dp[i-1][i] = min(height[i], height[i-1])
        # for j in range(2, n):
        #     for i in range(j-2, -1, -1):
        #         if height[i] < height[j]:
        #             m = dp[i+1][j]
        #         else:
        #             m = dp[i][j-1]
        #         el = min(height[i], height[j])*(j-i)
        #         dp[i][j] = max(m, el)
        # return dp[0][n-1]
        p1 = 0
        p2 = len(height)-1
        area = 0
        while p1 < p2:
            a = min(height[p1], height[p2])*(p2 - p1)
            area = max(area, a)
            if height[p1] < height[p2]:
                p1 += 1
            else:
                p2 -= 1
        return area
# @lc code=end
n =3
dp = [[2 for i in range(n)] for j in range(n)]
print(max(dp))
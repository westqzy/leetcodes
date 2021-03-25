#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp =[ [0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = grid[0][0]
                elif i == 0 and j >= 1:
                    dp[i][j] = dp[i][j-1]+grid[i][j]
                elif j == 0 and i >= 1:
                    dp[i][j] = dp[i-1][j]+grid[i][j]
                else:
                    dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        print(dp)
        return dp[-1][-1]

# @lc code=end


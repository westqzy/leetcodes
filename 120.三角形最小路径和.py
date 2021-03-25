#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#

# @lc code=start
import copy
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[0] * n for _ in range(n)]
        dp[0][0] = triangle[0][0]
        for i in range(1, len(triangle)):
            dp[i][0] = dp[i-1][0]+triangle[i][0]
            dp[i][i] = dp[i-1][i-1]+triangle[i][i]
            for j in range(1, len(triangle[i])-1):
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j])+triangle[i][j]
        #print(dp)
        return min(dp[-1])
                
                
                


# @lc code=end
import copy
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
dp = copy.deepcopy(triangle)
dp[2][-1] = 1000
dp[1][-1] = 999
print(dp)
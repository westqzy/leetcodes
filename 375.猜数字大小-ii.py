#
# @lc app=leetcode.cn id=375 lang=python3
#
# [375] 猜数字大小 II
#

# @lc code=start
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0 for i in range(n)] for j in range(n)]
        for j in range(n):
            for i in range(j-1, -1, -1):
                dp[i][j] = min(max(dp[i][k-1], dp[k+1][j])+k+1 for k in range(i, j))
        return dp[0][-1] 

# @lc code=end
#%%
import numpy as np
n = 1
dp = [[0 for i in range(n)] for j in range(n)]
for j in range(n):
    for i in range(j-1, -1, -1):
        #dp[i][j] = float("inf")        
        dp[i][j] = min(max(dp[i][k-1], dp[k+1][j])+k+1 for k in range(i, j))
print(np.array(dp))

# 0,1
# 1,2

# 0 1 2 
# 1 2 3
#
# @lc app=leetcode.cn id=1025 lang=python3
#
# [1025] 除数博弈
#

# @lc code=start
import math
class Solution:
    def divisorGame(self, N: int) -> bool:
        dp = [0]*(N+1)
        dp[1] = 0
        for i in range(2, N+1):
            for j in range(1, int(math.sqrt(i))+1):
                if i % j == 0:
                    if dp[i-j] == 0:
                        dp[i] = 1
                        break
            else:
                dp[i] = 0
            
        print(dp)
        return dp[N] == 1

# @lc code=end

dp[1] = 0
dp[2] = 1
dp[3] = 0
dp[4] = 1
dp[5] = 0
dp[6] = 1
dp[7] = 0
dp[8] = 1 
dp[9] = 0 
#
# @lc app=leetcode.cn id=343 lang=python3
#
# [343] 整数拆分
#

# @lc code=start
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0]*(n+1)
        for i in range(2, n+1):
            for j in range(i):
                dp[i] = max(dp[j]*(i-j), j*(i-j), dp[i])
        #print(dp)
        return dp[-1]
# @lc code=end


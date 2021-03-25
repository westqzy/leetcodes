#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start
class Solution:
    def fib(self, N: int) -> int:
        dp = [0]*(N+1)
        if N == 0:
            dp[0] = 0
        elif N == 1:
            dp[1] = 1
        else:
            dp[0] = 0
            dp[1] = 1 
            for i in range(2,N+1):
                dp[i] = dp[i-1]+dp[i-2]
        return dp[N]
            

# @lc code=end


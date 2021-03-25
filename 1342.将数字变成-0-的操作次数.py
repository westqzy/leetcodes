#
# @lc app=leetcode.cn id=1342 lang=python3
#
# [1342] 将数字变成 0 的操作次数
#

# @lc code=start
class Solution:
    def numberOfSteps (self, num: int) -> int:
        res = 0
        while num != 0:
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
            res += 1
        return res
        #动态规划超时
        # dp = [0]*(num+1)
        # for i in range(1, num+1):
        #     if i % 2 == 0:
        #         dp[i] = dp[i//2] + 1
        #     else:
        #         dp[i] = dp[i-1] + 1
        # return dp[num]

# @lc code=end


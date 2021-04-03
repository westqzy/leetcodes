#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp0 = 0
        dp1 = -prices[0]
        dp2 = float("-inf")
        for i in range(1, len(prices)):
            dp0 = 0
            dp1 = max(dp1, dp0 - prices[i])
            dp2 = max(dp2, dp1 + prices[i])
        return max(dp0, dp2)
# @lc code=end


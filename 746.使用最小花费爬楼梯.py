#
# @lc app=leetcode.cn id=746 lang=python3
#
# [746] 使用最小花费爬楼梯
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp = [0]*(len(cost)+1)
        # for i in range(2, len(cost)+1):
        #     dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        # #print(dp)
        # return dp[-1]

        pre = 0
        cur = 0
        for i in range(2, len(cost)+1):
            cur, pre = min(cur+cost[i-1], pre+cost[i-2]), cur
        #print(dp)
        return cur
# @lc code=end

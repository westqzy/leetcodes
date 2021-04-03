#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        # if len(nums) == 0:
        #     return 0
        # dp = [0]*(len(nums)+1)
        # dp[1] = nums[0]
        # for i in range(2, len(nums)+1):
        #     dp[i] = max(dp[i-1],  dp[i-2]+nums[i-1])
        #     #print(dp)
        # return dp[-1]
        if len(nums) == 0:
            return 0
        pre2 = 0
        pre1 = nums[0]
        cur = nums[0]
        for i in range(1, len(nums)):
            cur, pre2=max(pre2 + nums[i], pre1), pre1
            pre1 = cur
        return cur
# @lc code=end

a = []
print(a[0])
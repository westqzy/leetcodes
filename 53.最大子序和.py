# @before-stub-for-debug-begin
from python3problem53 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if nums == 1:
            return nums[0]
        dp = [0]*(len(nums))
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
        return max(dp)
# @lc code=end
a = 1
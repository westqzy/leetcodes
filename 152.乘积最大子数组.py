#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [None]*len(nums)
        dp[0] = nums[0]
        dpm = [None]*len(nums)
        dpm[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]*nums[i], dpm[i-1]*nums[i], nums[i])
            dpm[i] = min(dp[i-1]*nums[i], dpm[i-1]*nums[i], nums[i])
        return max(dp)
# @lc code=end
[1,-2,3,-4,-4,-5,1,0]
[1,-2,3,24
[1,-2,-6,-12]

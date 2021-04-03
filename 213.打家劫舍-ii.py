#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def steal(nums):
            dp = [0]*(len(nums)+1)
            dp[1] = nums[0]
            for i in range(2, len(nums)+1):
                dp[i] = max(dp[i-2]+nums[i-1], dp[i-1])
            return dp[-1]
        return max(steal(nums[:-1]), steal(nums[1:]))
        # if len(nums) == 1:
        #     return nums[0]
        # def jubumax(nums_index):
        #     dp = [0]*(len(nums_index)+1)
        #     dp[1] = nums_index[0]
        #     for i in range(2, len(nums_index)+1):
        #         dp[i] = max(dp[i-1],  dp[i-2]+nums_index[i-1])
        #     #print(dp)
        #     return dp[-1]
        # return max(jubumax(nums[:-1]), jubumax(nums[1:]))
        
# @lc code=end


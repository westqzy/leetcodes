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
        def jubumax(nums_index):
            dp = [0]*(len(nums_index)+1)
            dp[1] = nums_index[0]
            for i in range(2, len(nums_index)+1):
                dp[i] = max(dp[i-1],  dp[i-2]+nums_index[i-1])
            #print(dp)
            return dp[-1]
        return max(jubumax(nums[:-1]), jubumax(nums[1:]))
        
# @lc code=end

2 3 

0 2 3  
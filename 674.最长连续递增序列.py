#
# @lc app=leetcode.cn id=674 lang=python3
#
# [674] 最长连续递增序列
#

# @lc code=start
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        # if len(nums) == 0:
        #     return 0
        # dp = [1]*len(nums)
        # for i in range(1, len(nums)):
        #     if nums[i] > nums[i-1]:
        #         dp[i] = dp[i-1]+1
        # return max(dp)
        
        if nums == []:
            return 0
        cur = 1
        res = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                cur =  cur + 1
            else:
                cur = 1
            res = max(res, cur)
        return res

# @lc code=end


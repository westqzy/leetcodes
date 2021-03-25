#
# @lc app=leetcode.cn id=1413 lang=python3
#
# [1413] 逐步求和得到正数的最小值
#

# @lc code=start
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = dp[i-1] + nums[i]
        print(dp)
        return -min(dp)+1 if min(dp)<0 else 1
                        
# @lc code=end

a = [1,3,-1,4,5,7,88]
print(min(a))
#
# @lc app=leetcode.cn id=643 lang=python3
#
# [643] 子数组最大平均数 I
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum_k = 0
        for i in range(k):
            sum_k += nums[i]
        max_s = sum_k
        for i in range(k,len(nums)):
            sum_k = sum_k-nums[i-k]+nums[i]
            max_s = max(max_s, sum_k)
        return max_s/k
# @lc code=end


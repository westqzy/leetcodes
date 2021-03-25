#
# @lc app=leetcode.cn id=1403 lang=python3
#
# [1403] 非递增顺序的最小子序列
#

# @lc code=start
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        while sum(res) <= sum(nums):
            res.append(nums.pop())
        return res
# @lc code=end


#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#

# @lc code=start
import collections
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = collections.Counter(nums)
        for i,j in a.items():
            if j == 1:
                return i
# @lc code=end


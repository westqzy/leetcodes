#
# @lc app=leetcode.cn id=1608 lang=python3
#
# [1608] 特殊数组的特征值
#

# @lc code=start
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for i in range(len(nums)+1):
            n = sum(ele >= i for ele in nums)
            if n == i:
                return n
        return -1
# @lc code=end


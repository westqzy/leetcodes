#
# @lc app=leetcode.cn id=896 lang=python3
#
# [896] 单调数列
#

# @lc code=start
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        return sorted(A) == A or sorted(A) == list(reversed(A))

# @lc code=end


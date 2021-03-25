#
# @lc app=leetcode.cn id=796 lang=python3
#
# [796] 旋转字符串
#

# @lc code=start
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        A_t = A + A
        return B in A_t and len(B) == len(A)
# @lc code=end


#
# @lc app=leetcode.cn id=908 lang=python3
#
# [908] 最小差值 I
#

# @lc code=start
class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        cha = max(A) - min(A)
        res = max(cha-2*K, 0)
        return res
# @lc code=end


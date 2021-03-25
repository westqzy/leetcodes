#
# @lc app=leetcode.cn id=598 lang=python3
#
# [598] 范围求和 II
#

# @lc code=start
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        mini = m
        minj = n
        for i in ops:
            mini = min(mini, i[0])
            minj = min(minj, i[1])
        return mini*minj
# @lc code=end


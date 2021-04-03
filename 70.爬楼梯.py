#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        cur = 1
        pre = 1
        for i in range(2, n+1):
            cur, pre = cur + pre, cur
        return cur
# @lc code=end

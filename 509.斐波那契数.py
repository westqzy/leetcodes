#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start
class Solution:
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        pre = 0
        cur = 1
        for i in range(2, N+1):
            pre, cur = cur, pre + cur
        return cur

# @lc code=end


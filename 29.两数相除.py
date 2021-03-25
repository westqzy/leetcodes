#
# @lc app=leetcode.cn id=29 lang=python3
#
# [29] 两数相除
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res = 0
        flag1, flag2 = 1, 1
        if  divisor == 1:
            return dividend
        if divisor == -1:
            if dividend > -2^31:
                return -dividend
            else:
                return 2147483647
        if dividend < 0:
            flag1 = -1
        if divisor < 0:
            flag2 = -1
        divisor = abs(divisor)
        dividend = abs(dividend)
        while dividend >= divisor:
            cur = divisor
            mul = 1
            while cur+cur < dividend:
                cur += cur
                mul += mul
            dividend -= cur
            res += mul
        return res*flag1*flag2
# @lc code=end


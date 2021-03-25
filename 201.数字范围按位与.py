#
# @lc app=leetcode.cn id=201 lang=python3
#
# [201] 数字范围按位与
#

# @lc code=start
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        res = n
        for i in range(m, n):
            res = res & i
        return res
# @lc code=end
a = 5 & 6 & 7 & 1
print(a)

a, b    na, nb
0, 0    0, 1
#
# @lc app=leetcode.cn id=1009 lang=python3
#
# [1009] 十进制整数的反码
#

# @lc code=start
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        N_bin = bin(N)[2:]
        res = ["0" if i == "1" else "1" for i in N_bin]
        res = "".join(res)
        return int(res, 2) 
# @lc code=end


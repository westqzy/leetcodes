#
# @lc app=leetcode.cn id=693 lang=python3
#
# [693] 交替位二进制数
#

# @lc code=start
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bin_n = bin(n)[2:]
        if  n == 0 or n == 1:
            return True
        for i in range(1,len(bin_n)):
            if bin_n[i] == bin_n[i-1]:
                return False
        return True
# @lc code=end

print(bin(10))
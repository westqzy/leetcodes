#
# @lc app=leetcode.cn id=504 lang=python3
#
# [504] 七进制数
#

# @lc code=start
class Solution:
    def convertToBase7(self, num: int) -> str:
        abs_num = abs(num)
        res = ""
        while(abs_num >= 7):
            a = abs_num % 7
            abs_num //= 7
            res += str(a)
        res += str(abs_num)
        if num < 0:
            res += "-"
        return res[::-1]
# @lc code=end

print(6//7)
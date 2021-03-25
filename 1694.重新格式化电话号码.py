#
# @lc app=leetcode.cn id=1694 lang=python3
#
# [1694] 重新格式化电话号码
#

# @lc code=start
class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace(" ", "").replace("-", "")
        l = len(number)
        p = 0
        while l >= 4:
            if l > 4:
                l = l-3    
                number = number[:p+3]+"-"+number[p+3:]
                p += 4
            if l == 4:
                l = l-2
                number = number[:p+2]+"-"+number[p+2:]
                p += 3
        return number
# @lc code=end


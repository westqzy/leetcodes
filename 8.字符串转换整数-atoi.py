#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0:
            return 0
        def yuejie(res:str)->int:
            try:
                res = int(res)
            except:
                return 0
            if res < 0:
                return max(res, -2147483648)
            else:
                return min(res, 2147483647)
        if s[0].isnumeric() or s[0] == "-" or s[0] == "+":
            res = s[0]
            for i in range(1, len(s)):
                if  s[i].isnumeric():
                    res += s[i]
                else:
                    break
            return yuejie(res)
        else:
            return 0
# @lc code=end
import re
s = "-91283472332"
a = int(*re.findall('^[\+\-]?\d+', s.lstrip()))
##正则万岁
print(a)

            
#
# @lc app=leetcode.cn id=166 lang=python3
#
# [166] 分数到小数
#

# @lc code=start
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator*denominator < 0:
            xiu = "-"
        else:
            xiu = ""
        numerator = abs(numerator)
        denominator = abs(denominator)
        zhen, b = divmod(numerator, denominator)
        yu = {}
        xiaoshu = []
        index = 0
        while b:
            yu[b] = index
            index += 1
            b = b * 10
            a, b = divmod(b, denominator)
            xiaoshu.append(str(a))
            if b in yu.keys():
                xiaoshu.append(")")
                xiaoshu.insert(yu[b], "(")
                break
        if xiaoshu == []:
            res = str(zhen)
        else:
            res = str(zhen) + "." + "".join(xiaoshu)
        return xiu + res

# @lc code=end

a, b = divmod(670, 333)
print(a, b)
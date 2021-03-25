#
# @lc app=leetcode.cn id=1556 lang=python3
#
# [1556] 千位分隔数
#

# @lc code=start
class Solution:
    def thousandSeparator(self, n: int) -> str:
        res = list(str(n))
        res.reverse()
        i = 0
        length = len(res)
        k = 0
        while i < length:
            i += 1
            if i % 3 == 0:
                res.insert(i+k, ".")
                k += 1
        print(res)
        if res[-1] == ".":
            res.pop()
        res.reverse()
        return "".join(res)
# @lc code=end


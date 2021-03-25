#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        l = len(s)
        if l == 0:
            return []

        def backtrace(s):
            if s == "":
                ress.append(res[:])
            else:
                for i in range(len(s)):
                    t = s[:i + 1]
                    if t != t[::-1]:
                        continue
                    res.append(t)
                    backtrace(s[i+1:])
                    res.pop()

        res = []
        ress = []
        backtrace(s)
        return ress
# @lc code=end


#
# @lc app=leetcode.cn id=1614 lang=python3
#
# [1614] 括号的最大嵌套深度
#

# @lc code=start
class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        n = 0
        for i in s:
            if i == "(":
                n += 1
                res = max(res, n)
            elif i == ")":
                n -= 1
        return res

# @lc code=end


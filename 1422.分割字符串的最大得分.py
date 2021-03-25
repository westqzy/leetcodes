#
# @lc app=leetcode.cn id=1422 lang=python3
#
# [1422] 分割字符串的最大得分
#

# @lc code=start
class Solution:
    def maxScore(self, s: str) -> int:
        res = 0
        for i in range(len(s)-1):
            s0 = s[:i+1]
            s1 = s[i+1:]
            res = max(res, s0.count("0")+s1.count("1"))
        return res
# @lc code=end


#
# @lc app=leetcode.cn id=1408 lang=python3
#
# [1408] 数组中的字符串匹配
#

# @lc code=start
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        s = ",".join(words)
        res = []
        for i in words:
            count = s.count(i)
            if count > 1:
                res.append(i)
        return res

# @lc code=end

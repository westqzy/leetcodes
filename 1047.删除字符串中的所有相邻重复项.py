#
# @lc app=leetcode.cn id=1047 lang=python3
#
# [1047] 删除字符串中的所有相邻重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, S: str) -> str:
        res = []
        for i in range(len(S)):
            if len(res) == 0:
                res.append(S[i])
            else:
                if res[-1] == S[i]:
                    res.pop()
                else:
                    res.append(S[i])
        return "".join(res)
# @lc code=end


#
# @lc app=leetcode.cn id=187 lang=python3
#
# [187] 重复的DNA序列
#

# @lc code=start
import collections
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        # listall = {}
        # for i in range(len(s)-9):
        #     listall[s[i:i+10]] = listall.get(s[i:i+10], 0) + 1
        # res = []
        # for key, value in listall.items():
        #     if value > 1:
        #         res.append(key)
        # return res
        listall = collections.Counter(s[i:i+10] for i in range(len(s)-9))
        res = list(filter(lambda x: listall[x]>1, listall))
        return res
# @lc code=end


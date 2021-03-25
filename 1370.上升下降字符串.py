#
# @lc app=leetcode.cn id=1370 lang=python3
#
# [1370] 上升下降字符串
#

# @lc code=start
import collections
class Solution:
    def sortString(self, s: str) -> str:
        hash1 = collections.Counter(s)
        res = ""
        while hash1 != {}:
            for i in sorted(hash1.keys()):
                res += i
                hash1[i] -= 1
                if hash1[i] == 0:
                    del hash1[i]
            for i in sorted(hash1.keys(), reverse=True):
                res += i
                hash1[i] -= 1
                if hash1[i] == 0:
                    del hash1[i]
        return res
# @lc code=end

hash1 = {1}
print(hash1 == {})
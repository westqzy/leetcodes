#
# @lc app=leetcode.cn id=1576 lang=python3
#
# [1576] 替换所有的问号
#

# @lc code=start
import collections
import string
class Solution:
    def modifyString(self, s: str) -> str:
        shash = collections.Counter(s)
        qn = shash["?"]
        print(qn)
        lists = set(shash.keys())
        listsa = set(string.ascii_lowercase)
        nos = listsa - lists
        nos = list(nos)
        print(nos)
        j = 0
        for i in range(qn):
            s = s.replace("?", nos[j],1)
            j += 1
            if j == len(nos)-1:
                j = 0
        return s
# @lc code=end
import string
lists = string.ascii_lowercase
print(set("12345")-set("123"))
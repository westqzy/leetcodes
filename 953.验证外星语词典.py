#
# @lc app=leetcode.cn id=953 lang=python3
#
# [953] 验证外星语词典
#

# @lc code=start
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        s_str = "abcdefghijklmnopqrstuvwxyz"
        dict1 = dict(zip(order, s_str))
        def change(word):
            out = ""
            for i in word:
                out += dict1[i]
            return out
        dict1 = [change(i) for i in words]
        return dict1 == sorted(dict1)
# @lc code=end
words = ["word","world","row"]
s_str = "abcdefghijklmnopqrstuvwxyz"
order = "worldabcefghijkmnpqstuvxyz"
dict1 = dict(zip(order, s_str))

def change(word):
            out = ""
            for i in word:
                out += dict1[i]
            return out
dict1 = [change(i) for i in words]
print(dict1)
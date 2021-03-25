#
# @lc app=leetcode.cn id=1624 lang=python3
#
# [1624] 两个相同字符之间的最长子字符串
#

# @lc code=start
import collections
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        res = -1
        for i in range(len(s)):
            res = max(res, s.rfind(s[i])-i-1)
        return res 
            
# @lc code=end

a = "aaadasd"
b = a.index("1")
print(b)
#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        p1 = 0
        p2  = 0        
        while p1+p2 < len(haystack) and p2 < len(needle):
            if haystack[p1+p2] == needle[p2]:
                p2 += 1
            else:
                p2 = 0
                p1 += 1 
        if p2 == len(needle):
            return p1 
        else:
            return -1
# @lc code=end

haystack = ""
needle = ""
p1 = 0
p2  = 0
while p1 < len(haystack) and p2 < len(needle):
    if haystack[p1] == needle[p2]:
        p2 += 1
    else:
        p2 = 0
    p1 += 1
print(p1-p2)
    
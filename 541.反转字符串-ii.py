#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        lens = len(s)
        start = 0
        res = ""
        while lens - 2*k > 0:
            jiequ = s[start:start+k]
            jiequ = jiequ[::-1]
            res += jiequ + s[start+k:start+2*k]
            lens = lens - 2*k
            start = start + 2*k
        if lens >= k:
            jiequ = s[start:start+k]
            jiequ = jiequ[::-1]
            res += jiequ + s[start+k:]
        else:
            jiequ = s[start:]
            jiequ = jiequ[::-1]
            res += jiequ
        
        return res
# class Solution(object):
#     def reverseStr(self, s, k):
#         a = list(s)
#         for i in xrange(0, len(a), 2*k):
#             a[i:i+k] = reversed(a[i:i+k])
#         return "".join(a)


# @lc code=end

a = "aaavvvv"
b = a[0:4] 
print(b[0:4:-1])
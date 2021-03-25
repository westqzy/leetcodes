#
# @lc app=leetcode.cn id=1071 lang=python3
#
# [1071] 字符串的最大公因子
#

# @lc code=start
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str2 not in str1 and str1 not in str2:
            return ""
        for i in range(min(len(str1), len(str2)), 0, -1):
            if len(str1) % i == 0 and len(str2) % i == 0:
                if str2[:i]*(len(str2)//i) == str2 and str1[:i]*(len(str1)//i) == str1:
                    return str1[:i]
        return ""
# @lc code=end
str1 = "ABCCABCC"
s1 = {}
for i in str1:
    s1[i] = s1.get(i, 0) + 1
print(s1)
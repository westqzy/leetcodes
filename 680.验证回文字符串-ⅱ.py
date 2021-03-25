#
# @lc app=leetcode.cn id=680 lang=python3
#
# [680] 验证回文字符串 Ⅱ
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        lens = len(s)
        for i in range(len(s)):
            p2 = lens - i - 1
            if s[i] != s[p2]:
                s1 = s[0:i]+s[i+1:]
                s2 = s[:p2]+s[p2+1:]
                if s1 == s1[::-1] or s2 == s2[::-1]:
                    return True
                else:
                    return False
            
# @lc code=end

s="aadvb"
print(s[:4]+s[5:])
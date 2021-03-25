#
# @lc app=leetcode.cn id=459 lang=python3
#
# [459] 重复的子字符串
#

# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        len_s = len(s)
        for i in range(1,len_s//2+1):
            if len_s % i == 0:
                if s[:i]*(len_s // i) == s:
                    return True
        return False
            
# @lc code=end

def repeatedSubstringPattern( s: str) -> bool:
        len_s = len(s)
        for i in range(1,len_s//2+1):
            if len_s % i == 0:
                if s[:i]*(len_s // i) == s:
                    return True
        return False
            


print(repeatedSubstringPattern("abab"))
print(11//2)
s="aaaaddcf"
s1 = s[2:5]
print(s1)
"aaaaaaaaaaaaaaaaaaaaaaaaaa"
"aaaaabbbbbaaaaabbbbbb"
"a"
"ababa"
"ababababab"
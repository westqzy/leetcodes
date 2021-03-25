#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp =[[0 for i in range(n)] for j in range(n)]
        if len(s) == 0:
            return ""
        maxl = 1
        start = 0
        for i in range(n):
            dp[i][i] = 1
        for j in range(n):
            for i in range(j):
                if s[i] == s[j]:
                    if j - i < 3:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = 0
                
                
                if dp[i][j] == 1:
                    if j - i + 1 > maxl:
                        maxl = j -i + 1
                        start = i
        return s[start: start+maxl ]
        

                
# @lc code=end


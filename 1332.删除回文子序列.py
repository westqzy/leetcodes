#
# @lc app=leetcode.cn id=1332 lang=python3
#
# [1332] 删除回文子序列
#

# @lc code=start
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if s[::-1] == s:
            return 1
        else:
            return 2
        
# @lc code=end
s= [1,2,3]
s = s[::-1]
print(s)
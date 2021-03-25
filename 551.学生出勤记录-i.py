#
# @lc app=leetcode.cn id=551 lang=python3
#
# [551] 学生出勤记录 I
#

# @lc code=start
class Solution:
    def checkRecord(self, s: str) -> bool:
        num_A  = 0
        num_L = 0
        for i in range(len(s)):
            if s[i] == "A":
                num_A += 1
                num_L = 0
            elif s[i] == "L":
                num_L += 1
            else:
                num_L = 0
            if num_A >= 2 or num_L >= 3:
                return False
        return True
            
# @lc code=end


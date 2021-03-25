#
# @lc app=leetcode.cn id=434 lang=python3
#
# [434] 字符串中的单词数
#

# @lc code=start
class Solution:
    def countSegments(self, s: str) -> int:
        p2 = -1
        count = 0
        for p1 in range(len(s)):
            if s[p1] != " ":
                p2 = p1
            else:
                if p2 != -1:
                    count += 1
                    p2 = -1
            if p1 == len(s)-1 and p1 == p2:
                count += 1
        return count
# @lc code=end


s = "aaadsc asdf            awe"
print(s.split())              #


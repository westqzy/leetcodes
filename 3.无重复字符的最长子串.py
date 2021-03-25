#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p = 0
        hash1 = set()
        res = 0
        length = 0
        for i in range(len(s)):
            while s[i] in hash1:
                hash1.remove(s[p])
                p += 1
                length -= 1
            hash1.add(s[i])
            length += 1
            res = max(length, res)
        return res

# @lc code=end


#
# @lc app=leetcode.cn id=557 lang=python3
#
# [557] 反转字符串中的单词 III
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        new_s = ""
        list_s = s.split(" ")
        for i in range(len(list_s)):
            new_s += list_s[i][::-1] + " "
        return new_s[:-1]
# @lc code=end

s = "Let's take LeetCode contest"
new_s = ""
list_s = s.split(" ")
for i in range(len(list_s)):
    new_s += list_s[i][::-1] + " "
new_s.replace(" ","",-1)
print(new_s)
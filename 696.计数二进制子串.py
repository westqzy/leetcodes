#
# @lc app=leetcode.cn id=696 lang=python3
#
# [696] 计数二进制子串
#

# @lc code=start
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        list1 = []
        count = 1
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                list1.append(count)
                count = 1
        list1.append(count)   
        sum_res = 0
        for i in range(1, len(list1)):
            sum_res += min(list1[i], list1[i-1])
        return sum_res
# @lc code=end
list1 = []
count = 1
s = "00110"
for i in range(1,len(s)):
    if s[i] == s[i-1]:
        count += 1
    else:
        list1.append(count)
        count = 1
    print(list1)
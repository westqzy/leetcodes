#
# @lc app=leetcode.cn id=1446 lang=python3
#
# [1446] 连续字符
#

# @lc code=start
import re
class Solution:
    def maxPower(self, s: str) -> int:
        return max(len(i.group()) for i in re.finditer(r'([a-z])\1*',s))
# @lc code=end
import re
a = "aaaabbbbcccccdddddaaadssss"
a = re.findall(r"([a-z])\1*", a)
print(a)
#
# @lc app=leetcode.cn id=507 lang=python3
#
# [507] 完美数
#

# @lc code=start
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        count = 0
        if num == 1:
            return False
        for i in range(2,int(math.sqrt(num))+1):
            if num % i == 0:
                count += i + num // i
        return count+1 == num
# @lc code=end
import math
num = 28
count = 0
for i in range(2,int(math.sqrt(num))+1):
    if num % i == 0:
        count += i + num // i
print(count+1)
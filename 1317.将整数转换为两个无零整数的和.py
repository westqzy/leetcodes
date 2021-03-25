#
# @lc app=leetcode.cn id=1317 lang=python3
#
# [1317] 将整数转换为两个无零整数的和
#

# @lc code=start
import random
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        while True:
            ran = random.randint(1,n)
            ran2 = n - ran
            if "0" not in str(ran) and  "0" not in str(ran2): 
                break
        return [ran, ran2]
# @lc code=end


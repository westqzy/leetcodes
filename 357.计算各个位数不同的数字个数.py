#
# @lc app=leetcode.cn id=357 lang=python3
#
# [357] 计算各个位数不同的数字个数
#

# @lc code=start
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        dp = [0]*(n+1)
        if n < 1:
            return 1
        if n == 1:
            return 10
        if n == 2:
            return 91
        dp[1] = 9
        for i in range(2, n+1):
            dp[i] = dp[i-1]*(11-i)
        #print(dp)
        return sum(dp)+1
            

# @lc code=end

name = "qzy"
age = 25
print(f"我叫{name}，今年{age}岁")

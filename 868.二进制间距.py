#
# @lc app=leetcode.cn id=868 lang=python3
#
# [868] 二进制间距
#

# @lc code=start
class Solution:
    def binaryGap(self, n: int) -> int:
        n_ob = bin(n)[2:]
        res = 0
        j =  n_ob.find("1")
        if j == -1:
            return False
        for i in range(j+1, len(n_ob)):
            if n_ob[i] == "1":
                res = max(res, i - j)
                j = i
        return res

# @lc code=end
a ="00001100000"
n = a.find("1")
print(n)
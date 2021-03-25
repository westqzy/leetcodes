#
# @lc app=leetcode.cn id=461 lang=python3
#
# [461] 汉明距离
#

# @lc code=start
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        x_bin = bin(x)
        y_bin = bin(y)
        x_bin = x_bin[2:].zfill(32)
        y_bin = y_bin[2:].zfill(32)
        print(y_bin)
        for i in range(len(x_bin)):
            if x_bin[i] != y_bin[i]:
                count += 1
        return count
# @lc code=end

x_bin = bin(10)
print(x_bin)
x_bin = x_bin[2:].zfill(32)#补0,补成32位
print(x_bin)
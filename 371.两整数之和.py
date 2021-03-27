#
# @lc app=leetcode.cn id=371 lang=python3
#
# [371] 两整数之和
#

# @lc code=start
import numpy
class Solution:
    def getSum(self, a: int, b: int) -> int:
        return int(numpy.sum([a, b]))
# @lc code=end
import numpy
print(type(numpy.sum([1,3])))



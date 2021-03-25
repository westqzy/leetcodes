#
# @lc app=leetcode.cn id=137 lang=python3
#
# [137] 只出现一次的数字 II
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        X,Y=0,0
        for Z in nums:
            Yn = ~X&~Y&Z|~X&Y&~Z
            Xn = X&~Y&~Z|~X&Y&Z
            Y = Yn
            X = Xn
        return Y

# @lc code=end
from functools import reduce
nums = [2,2,3,5,3]
a = reduce(lambda x, y: x ^ y, nums)
print(a)
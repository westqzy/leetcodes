#
# @lc app=leetcode.cn id=1588 lang=python3
#
# [1588] 所有奇数长度子数组的和
#

# @lc code=start
import itertools
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = 0
        if len(arr) < 3:
            return sum(arr)
        for i in range(3, len(arr)+1, 2):
            for j in range(len(arr)+1-i):
                res += sum(arr[j:j+i])
        res += sum(arr)
        return res

# @lc code=end

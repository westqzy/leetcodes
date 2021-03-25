#
# @lc app=leetcode.cn id=1394 lang=python3
#
# [1394] 找出数组中的幸运数
#

# @lc code=start
import collections
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hash1 = collections.Counter(arr)
        res = -1
        for i,j in hash1.items():
            if i == j:
                res = max(res, i)
        return res
# @lc code=end


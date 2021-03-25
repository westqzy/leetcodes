#
# @lc app=leetcode.cn id=1436 lang=python3
#
# [1436] 旅行终点站
#

# @lc code=start
import collections
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start = []
        dest = []
        for i, j in paths:
            start.append(i)
            dest.append(j)
        for i in dest:
            if i not in start:
                return i
# @lc code=end


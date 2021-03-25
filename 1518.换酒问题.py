#
# @lc app=leetcode.cn id=1518 lang=python3
#
# [1518] 换酒问题
#

# @lc code=start
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        while numBottles >= numExchange:
            could_change = numBottles // numExchange
            res += could_change
            numBottles = numBottles % numExchange  
            numBottles += could_change
        return res
# @lc code=end


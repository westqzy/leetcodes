#
# @lc app=leetcode.cn id=1217 lang=python3
#
# [1217] 玩筹码
#

# @lc code=start
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        ou_l = len([i for i in position if i % 2 == 0])
        ji_l = len(position) - ou_l
        return min(ou_l, ji_l)
        
# @lc code=end
position = [2,2,2,3,3]
jiou = len([i for i in position if i % 2 == 0])
print(jiou)
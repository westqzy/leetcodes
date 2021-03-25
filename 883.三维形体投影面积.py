#
# @lc app=leetcode.cn id=883 lang=python3
#
# [883] 三维形体投影面积
#

# @lc code=start
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        #计算底部面积
        di = 0
        ce1 = 0
        ce2_list = [0]*len(grid)
        for i in range(len(grid)):
            ce1 += max(grid[i])
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    di += 1
                    ce2_list[j] = max(ce2_list[j], grid[i][j])
        ce2 = sum(ce2_list)
        print(di,ce1,ce2)
        return di+ce1+ce2
# @lc code=end


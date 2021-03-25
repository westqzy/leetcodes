#
# @lc app=leetcode.cn id=892 lang=python3
#
# [892] 三维形体的表面积
#

# @lc code=start
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        line = 0
        for i in range(len(grid)):
            line += grid[0][i]+grid[-1][i]
            for j in range(len(grid)):
                if j >= 1:  
                    line += abs(grid[j][i] - grid[j-1][i])
        for i in range(len(grid)):
            line += grid[i][0]+grid[i][-1]
            for j in range(len(grid)):
                if j >= 1:
                    line += abs(grid[i][j] - grid[i][j-1])
                if grid[i][j] != 0:
                    line += 2
        return line

# @lc code=end


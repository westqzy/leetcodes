#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, x, y):
            if x < 0 or x > len(grid)-1 or y < 0 or y > len(grid[0])-1:
                return 
            if grid[x][y] != "1":
                return
            grid[x][y] = "2"
            dfs(grid, x-1, y)
            dfs(grid, x+1, y)
            dfs(grid, x, y-1)
            dfs(grid, x, y+1)
        
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(grid, i, j)
                    res += 1
        return res
# @lc code=end

a = [0]
if a[3] == None:
    print("no")
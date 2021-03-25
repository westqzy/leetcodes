#
# @lc app=leetcode.cn id=463 lang=python3
#
# [463] 岛屿的周长
#

# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def count_water(i,j):
            count_water = 0
            if grid[i+1][j] == 0:
                count_water += 1
            if grid[i-1][j] == 0:
                count_water += 1
            if grid[i][j+1] == 0:
                count_water += 1 
            if grid[i][j-1] == 0:
                count_water += 1
            return count_water
        if len(grid) == 0:
            return 0
        #把周围围上水坑
        for i in range(len(grid)):
            grid[i].insert(0,0)
            grid[i].append(0)
        grid.insert(0,[0]*(len(grid[0])))
        grid.append([0]*(len(grid[0])))
        zhouchang = 0
        for i in range(1,len(grid)-1):
            for j in range(1,len(grid[i])-1):
                if grid[i][j] == 1:
                    #计算陆地周围水坑多少
                    zhouchang += count_water(i,j)
                    #print("i=",i,"j=",j,zhouchang)
        return zhouchang         
                    
                    
                    
# @lc code=end

grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
for i in range(len(grid)):
    grid[i].insert(0,0)
    grid[i].append(0)
print(grid)
grid.insert(0,[0]*(len(grid[0])))
grid.append([0]*(len(grid[0])))

print(grid)
#
# @lc app=leetcode.cn id=1252 lang=python3
#
# [1252] 奇数值单元格的数目
#

# @lc code=start
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        grid = [[0 for i in range(m)] for i in range(n)]
        for hang, lie in indices:
            for i in range(m):
                grid[hang][i] += 1
            for i in range(n):
                grid[i][lie] += 1
        return sum(elem % 2 == 1 for line in grid for elem in line)
# @lc code=end


#
# @lc app=leetcode.cn id=1030 lang=python3
#
# [1030] 距离顺序排列矩阵单元格
#

# @lc code=start
import collections
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        # grid = [[0 for i in range(C)] for j in range(R)]
        # res = []
        # def search(grid, seedi, seedj):
        #     if seedi < 0 or seedi > R-1 or seedj < 0 or seedj > C-1:
        #         return 
        #     if grid[seedi][seedj] == 1:
        #         return
        #     grid[seedi][seedj] = 1
        #     res.append([abs(seedi-r0)+abs(seedj-c0),seedi, seedj])
        #     search(grid, seedi-1, seedj)
        #     search(grid, seedi+1, seedj)
        #     search(grid, seedi, seedj-1)
        #     search(grid, seedi, seedj+1)
        #     return
        # search(grid, r0, c0)
        # res.sort()
        # return [i[1:] for i in res]
            bucket = collections.defaultdict(list)
            dist = lambda r1, c1, r2, c2: abs(r1 - r2) + abs(c1 - c2)

            for i in range(R):
                for j in range(C):
                    bucket[dist(i, j, r0, c0)].append([i, j])
            res = []
            for i in range(len(bucket)):
                res.extend(bucket[i])
            return  res
# @lc code=end


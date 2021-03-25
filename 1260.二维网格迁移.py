#
# @lc app=leetcode.cn id=1260 lang=python3
#
# [1260] 二维网格迁移
#

# @lc code=start
import numpy as np
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        x = np.array(grid)
        x = x.flatten()
        print(x[-1])
        for _ in range(k):
            x = np.concatenate(([x[-1]], x[:-1]))
        x = x.reshape([m, n])

        return x
# @lc code=end
grid = [[1,2,3],[4,5,6],[7,8,9]]

import numpy as np
x = np.array(grid)
x = x.flatten()
for _ in range(1):
    x = np.append(x[-1:], x[:-1])
x = x.reshape([3, 3])
print(x)

import numpy as np
a = np.array([9])
b = np.array([5, 6, 6,7,5,7,8,8,])
c = np.concatenate((a, b))
print(c)
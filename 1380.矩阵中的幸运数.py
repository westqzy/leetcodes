#
# @lc app=leetcode.cn id=1380 lang=python3
#
# [1380] 矩阵中的幸运数
#

# @lc code=start
import numpy as np
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        matrix = np.array(matrix)
        minhang = [min(i) for i in matrix]
        maxshu = [max(i) for i in matrix.swapaxes(0, 1)]
        return [int(i) for i in maxshu if i in minhang]
# @lc code=end
import numpy as np
a = np.array([1,2,3])
print(type(a[1]))
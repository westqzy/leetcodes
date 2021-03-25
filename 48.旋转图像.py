#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#

# @lc code=start
import copy
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix)
        mc = copy.deepcopy(matrix)
        for i in range(l):
            for j in range(l):
                matrix[j][l-1-i] = mc[i][j]


# @lc code=end

(x,y) -> (y,2-x)
#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        hang = set()
        lie = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    hang.add(i)
                    lie.add(j)
        for i in range(m):
            for j in range(n):
                if i in hang or j in lie:
                    matrix[i][j] = 0
        # for i in range(m):
        #     for j in lie:
        #         matrix[i][j] = 0
        print(matrix)
# @lc code=end


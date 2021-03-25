#
# @lc app=leetcode.cn id=1572 lang=python3
#
# [1572] 矩阵对角线元素的和
#

# @lc code=start
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        res = 0
        for i in range(n):
            res += mat[i][i] + mat[n-i-1][i]
        if n % 2 == 1:
            res -= mat[n//2][n//2]
        return res
            
# @lc code=end


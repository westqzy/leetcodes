#
# @lc app=leetcode.cn id=867 lang=python3
#
# [867] 转置矩阵
#

# @lc code=start
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        res = [[0 for i in range(len(A))] for j in range(len(A[0]))]
        for i in range(len(A)):
            for j in range(len(A[0])):
                res[j][i] = A[i][j]
        return res
        
# @lc code=end

a = [0 for i in range(5)]
print(a)
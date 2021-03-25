#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if matrix == []:
            return []
        l = len(matrix[0])
        h = len(matrix)
        i = 0
        j = 0
        res = []
        while True:
            while j < l and matrix[i][j] != None:
                res.append(matrix[i][j])
                matrix[i][j] = None
                j += 1
            j -= 1
            i += 1
            while i < h and matrix[i][j] != None:
                res.append(matrix[i][j])
                matrix[i][j] = None
                i += 1
            i -= 1
            j -= 1
            while j >= 0 and matrix[i][j] != None:
                res.append(matrix[i][j])
                matrix[i][j] = None
                j -= 1
            j += 1
            i -= 1
            while i >= 0 and matrix[i][j] != None:
                res.append(matrix[i][j])
                matrix[i][j] = None
                i -= 1
            i += 1
            j += 1
            if len(res) == l*h:
                break
        return res
# @lc code=end


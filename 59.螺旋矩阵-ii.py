#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        #一层一层填入
        res = [[0 for _ in range(n)] for i in range(n)]
        cun = range(1, n * n + 1)
        ceng = (n + 1) // 2
        k = 0
        for i in range(ceng):
            for j in range(i, n - i - 1):
                res[i][j] = cun[k]
                k += 1
            for j in range(i, n - i - 1):
                res[j][n - i - 1] = cun[k]
                k += 1
            for j in range(i, n - i - 1):
                res[n - i - 1][n - j - 1] = cun[k]
                k += 1
            for j in range(i, n - i - 1):
                res[n - j - 1][i] = cun[k]
                k += 1
        if n % 2 == 1:
            mid = n // 2
            res[mid][mid] = n*n
        return res
# @lc code=end


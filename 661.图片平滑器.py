#
# @lc app=leetcode.cn id=661 lang=python3
#
# [661] 图片平滑器
#

# @lc code=start
class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        oldM = [[M[i][j] for j in range(len(M[0]))] for i in range(len(M))]
        for i in M:
            i.insert(0,-1)
            i.append(-1)
        newl = [-1]*len(M[0])
        M.insert(0, newl)
        M.append(newl)
        row = len(M)
        column = len(M[0])
        for i in range(1, row-1):
            for j in range(1, column-1):
                
                ans_c =  abs(M[i+1][j]) + abs(M[i+1][j+1]) + abs(M[i+1][j-1]) + \
                            abs(M[i-1][j]) + abs(M[i-1][j+1]) + abs(M[i-1][j-1]) + \
                            abs(M[i][j+1]) + abs(M[i][j]) +abs(M[i][j-1])
                c =  M[i+1][j] + M[i+1][j+1] + M[i+1][j-1] + \
                            M[i-1][j] + M[i-1][j+1] + M[i-1][j-1] + M[i][j] + M[i][j-1] + M[i][j+1] 
                count = 9 - (ans_c -c) // 2
                real_c = (ans_c + c) // 2
                oldM[i-1][j-1] = real_c // count
        return oldM
# @lc code=end
a=[]
a.insert()
#
# @lc app=leetcode.cn id=999 lang=python3
#
# [999] 可以被一步捕获的棋子数
#

# @lc code=start
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        res = 0
        for i in range(8):
            for j in range(8):
                if board[i][j] == "R":
                    ju_i = i
                    ju_j = j
        for i in range(ju_i-1, -1, -1):
            if board[i][ju_j] == "B":
                break
            elif board[i][ju_j] == "p":
                res += 1
                break
        for i in range(ju_i+1, 8):
            if board[i][ju_j] == "B":
                break
            elif board[i][ju_j] == "p":
                res += 1
                break
        for j in range(ju_j-1, -1, -1):
            if board[ju_i][j] == "B":
                break
            elif board[ju_i][j] == "p":
                res += 1
                break
        for j in range(ju_j+1, 8):
            if board[ju_i][j] == "B":
                break
            elif board[ju_i][j] == "p":
                res += 1
                break
        return res
# @lc code=end


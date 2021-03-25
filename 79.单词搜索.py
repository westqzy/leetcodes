#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        l = len(board)
        w = len(board[0])
        marked = [[False for _ in range(w)] for _ in range(l)]
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        def backtrace(index: int, nowi, nowj):
            if  nowi >= l or nowi < 0 or nowj >= w or nowj < 0:
                return False
            if marked[nowi][nowj] == True:
                return False
            if board[nowi][nowj] != word[index]:
                return False
            if index == len(word)-1:
                return True

            marked[nowi][nowj] = True
            for dir in directions:
                newi = nowi + dir[0]
                newj = nowj + dir[1]
                if backtrace(index+1, newi, newj):
                    return True
            marked[nowi][nowj] = False


        for i in range(l):
            for j in range(w):
                if backtrace(0, i, j) == True:
                    return True

        return False
# @lc code=end
now = (0,0)

#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
import collections
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def change(l:list):
            hash1 = collections.defaultdict(int)
            for i in l:
                if i.isnumeric():
                    hash1[i] += 1
            return hash1
        # 判断横着
        for heng in board:
            heng_c = change(heng)
            #print(heng_c)
            for i in heng_c.values():
                if i != 1:
                    return False
        #判断竖着
        board_z = [list(row) for row in zip(*board)]
        for shu in board_z:
            shu_c = change(shu)
            #print(shu_c)
            for i in shu_c.values():
                if i != 1:
                    return False

        #判断九宫格
        jiu_list = []
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                for k in range(i, i+3):
                    for p in range(j, j+3):
                        jiu_list.append(board[k][p])
                c_jiu = change(jiu_list)
                print(c_jiu)
                for k in c_jiu.values():
                    if k != 1:
                        return False
                jiu_list = []
        return True
# @lc code=end
board = [[".",".","4",".",".",".","6","3","."],[".",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".","9","."],[".",".",".","5","6",".",".",".","."],["4",".","3",".",".",".",".",".","1"],[".",".",".","7",".",".",".",".","."],[".",".",".","5",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]
i = 0
j = 0
a = board[i:i+3][j:j+3]
print(a)
i = ""
i.isnumeric
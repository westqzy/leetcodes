#
# @lc app=leetcode.cn id=1275 lang=python3
#
# [1275] 找出井字棋的获胜者
#

# @lc code=start
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        Amove = [moves[i] for i in range(len(moves)) if i % 2 == 0] 
        Bmove = [moves[i] for i in range(len(moves)) if i % 2 == 1]
        Amove.sort()
        Bmove.sort()
        print(Amove)
        print(Bmove)
        for i in range(len(Amove)):
            for j in range(i+1, len(Amove)):
                sub0 = Amove[j][0] - Amove[i][0]
                sub1 = Amove[j][1] - Amove[i][1]
                if [Amove[j][0] + sub0, Amove[j][1] + sub1] in Amove:
                    return "A"
        for i in range(len(Bmove)):
            for j in range(i+1, len(Bmove)):
                sub0 = Bmove[j][0] - Bmove[i][0]
                sub1 = Bmove[j][1] - Bmove[i][1]
                if [Bmove[j][0] + sub0, Bmove[j][1] + sub1] in Bmove:
                    return "B"
        if len(moves) == 9:
            return "Draw"
        else:
            return "Pending"


# @lc code=end

a = set([(2,4), (23,32)])
b = [(1,2), (2,4), (23,32)]
b = set(b)

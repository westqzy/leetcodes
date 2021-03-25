#
# @lc app=leetcode.cn id=657 lang=python3
#
# [657] 机器人能否返回原点
#

# @lc code=start
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        dict1 = {"U":1, "D":-1}
        dict2 = {"L":1, "R":-1}
        ud = 0
        rl = 0
        for i in moves:
            ud += dict1.get(i,0)
            rl += dict2.get(i,0)
        return ud == rl == 0


# @lc code=end


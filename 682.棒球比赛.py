#
# @lc app=leetcode.cn id=682 lang=python3
#
# [682] 棒球比赛
#

# @lc code=start
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        listres = []
        for i in range(len(ops)):
            if ops[i].lstrip("-").isdigit():
                listres.append(int(ops[i]))
            if ops[i] == "C":
                listres.pop()
            if ops[i] == "D":
                listres.append(listres[-1]*2)
            if ops[i] == "+":
                listres.append(listres[-1]+listres[-2])        
        return sum(listres)

# @lc code=end


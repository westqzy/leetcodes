#
# @lc app=leetcode.cn id=1189 lang=python3
#
# [1189] “气球” 的最大数量
#

# @lc code=start
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dict1 ={"b":0, "a":0, "l":0, "o":0, "n":0}
        for i in text:
            if i in dict1.keys():
                dict1[i] += 1
        dict1["l"] //= 2
        dict1["o"] //= 2
        return min(dict1.values())
# @lc code=end


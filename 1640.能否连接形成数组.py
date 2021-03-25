#
# @lc app=leetcode.cn id=1640 lang=python3
#
# [1640] 能否连接形成数组
#

# @lc code=start
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        res = []
        for i in arr:
            for j in pieces:
                if i == j[0]:
                    res.extend(j)
        print(res)
        return res == arr
# @lc code=end


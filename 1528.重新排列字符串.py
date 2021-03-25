#
# @lc app=leetcode.cn id=1528 lang=python3
#
# [1528] 重新排列字符串
#

# @lc code=start
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        s_list = list(s)
        dict1 = dict(zip(indices, s_list))
        res_s = ""
        for i in range(len(s)):
            res_s += dict1[i]
        return res_s
# @lc code=end


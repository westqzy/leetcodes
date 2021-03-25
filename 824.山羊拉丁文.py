#
# @lc app=leetcode.cn id=824 lang=python3
#
# [824] 山羊拉丁文
#

# @lc code=start
class Solution:
    def toGoatLatin(self, S: str) -> str:
        s_list = S.split(" ")
        for i, j in enumerate(s_list):
            if j[0] in "aeiouAEIOU":
                s_list[i] += "ma" + "a"*(i+1)
            else:
                s_list[i] = s_list[i][1:] + s_list[i][0] + "ma" + "a"*(i+1)
        return " ".join(s_list)
# @lc code=end
S = "I speak Goat Latin"
s_list = S.split(" ")
print(s_list)
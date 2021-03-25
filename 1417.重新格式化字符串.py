#
# @lc app=leetcode.cn id=1417 lang=python3
#
# [1417] 重新格式化字符串
#

# @lc code=start
class Solution:
    def reformat(self, s: str) -> str:
        al_list = [i for i in s if i.isalpha()]
        num_list = [i for i in s if i.isnumeric()]
        print(al_list)
        print(num_list)
        res = ""
        if abs(len(al_list) - len(num_list)) != 1 and len(al_list) != len(num_list):
            return ""
        else:
            if len(al_list) >= len(num_list):
                long_l = al_list
                short_l = num_list
            else:
                long_l = num_list
                short_l = al_list
            for i in range(len(short_l)):
                res += long_l[i]
                res += short_l[i]
            if len(long_l) != len(short_l):
                res += long_l[-1]
        return res
# @lc code=end
i ="a"

print(i.isalpha())
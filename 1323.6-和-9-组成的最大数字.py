#
# @lc app=leetcode.cn id=1323 lang=python3
#
# [1323] 6 和 9 组成的最大数字
#

# @lc code=start
class Solution:
    def maximum69Number (self, num: int) -> int:
        # num_list = list(map(str, list(str(num))))
        # for i in range(len(num_list)):
        #     if num_list[i] == "6":
        #         num_list[i] = "9"
        #         break
        # return int("".join(num_list))
        return int(str(num).replace("6", "9", 1))

# @lc code=end

i = [9,9]
print(int("".join(i)))

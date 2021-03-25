#
# @lc app=leetcode.cn id=476 lang=python3
#
# [476] 数字的补数
#

# @lc code=start
class Solution:
    def findComplement(self, num: int) -> int:
        num_bin = bin(num)
        num_bin = num_bin[2:]
        list1 = ["1","0"]
        new_str = ""
        for i in range(len(num_bin)):
            new_str += list1[int(num_bin[i])]
        return int(new_str,2)
# @lc code=end
a = "00111100"
print(~a)
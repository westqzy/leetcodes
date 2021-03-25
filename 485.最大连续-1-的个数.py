#
# @lc app=leetcode.cn id=485 lang=python3
#
# [485] 最大连续1的个数
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        nm_list = "".join(map(str,nums))
        nm_list = nm_list.split("0")
        max_l = 0
        for i in range(len(nm_list)):
            max_l = max(max_l,len(nm_list[i]))
        return max_l
        #一行代码
        #return max(map(len,"".join(map(str,nums)).split("0")))
# @lc code=end
nums = [1,1,1,1,1,1]
nm_list = "".join(map(str,nums))
nm_list = nm_list.split("0")
max_l = 0
for i in range(len(nm_list)):
    max_l = max(max_l,len(nm_list[i]))
    
print(max_l)
print(max(["111","11","11111"]))

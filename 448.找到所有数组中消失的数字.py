#
# @lc app=leetcode.cn id=448 lang=python3
#
# [448] 找到所有数组中消失的数字
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        hash1 = set(nums)
        for i in range(1,len(nums)+1):
            if i not in hash1:
                res.append(i)
        return res

# @lc code=end


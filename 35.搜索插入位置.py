#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return sorted(nums+[target]).index(target)
# @lc code=end
nums = [1,3,5,6]
target = 5
print(nums.extend(5))
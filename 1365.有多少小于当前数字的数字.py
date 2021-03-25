#
# @lc app=leetcode.cn id=1365 lang=python3
#
# [1365] 有多少小于当前数字的数字
#

# @lc code=start
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sort = sorted(nums)  
        return [sort.index(i) for i in nums]
# @lc code=end
nums = [12,3,4,5]
sort = sorted(set(nums))
print*(sort)
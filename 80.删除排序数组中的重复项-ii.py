#
# @lc app=leetcode.cn id=80 lang=python3
#
# [80] 删除排序数组中的重复项 II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        len_num = len(nums)
        if len_num <= 2:
            return len_num
        p = 1
        p2 = 1 
        count = 1
        while  p <= len(nums)-1:
            if nums[p] == nums[p-1]:
                count += 1
            else:
                count = 1
            if count == 3:
                count -= 1
            else:
                nums[p2] = nums[p]
                p2 += 1
            p += 1
        return p2
# @lc code=end


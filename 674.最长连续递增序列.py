#
# @lc app=leetcode.cn id=674 lang=python3
#
# [674] 最长连续递增序列
#

# @lc code=start
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        count = 1
        count_h = 1
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                count_h += 1
            else:
                count = max(count, count_h)
                count_h = 1
        count = max(count, count_h)
        return count

# @lc code=end


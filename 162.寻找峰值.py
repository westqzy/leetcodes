#
# @lc app=leetcode.cn id=162 lang=python3
#
# [162] 寻找峰值
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if mid == 0 and nums[0] > nums[1] or mid == len(nums)-1 and nums[-1] > nums[-2]:
                return mid
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            if nums[mid] < nums[mid+1]:
                left = mid + 1
            elif nums[mid] < nums[mid-1]:
                right = mid - 1

        

# @lc code=end

a = []
a.index(1, 0)
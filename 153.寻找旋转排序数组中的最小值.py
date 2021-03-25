#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        right = len(nums)-1
        left = 0
        if nums[right] > nums[left] or len(nums) == 1:
            return nums[0]
        while right >= left:
                mid = (right+left)//2
                if nums[mid] > nums[mid+1]:
                    return nums[mid+1]
                if nums[mid-1] > nums[mid]:
                    return nums[mid]
                if nums[mid] > nums[left]:
                    left = mid + 1
                elif nums[mid] < nums[right]:
                    right = mid - 1
# @lc code=end

[0,1,2,3,4]
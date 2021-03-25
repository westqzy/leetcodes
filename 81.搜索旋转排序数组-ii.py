#
# @lc app=leetcode.cn id=81 lang=python3
#
# [81] 搜索旋转排序数组 II
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
<<<<<<< HEAD
        
=======
        #nums = list(set(nums))
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (right + left)//2
            if nums[mid] == target:
                return True
            if nums[mid] > nums[left]:# 表明左侧有序
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < nums[left]:# 表明you侧有序
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            elif nums[mid] == nums[left]:
                left += 1
            # elif nums[mid] == nums[right]:
            #     right -= 1
        return False
>>>>>>> c4ec29c564721b5d60cd91e637dd5452e1378850
# @lc code=end


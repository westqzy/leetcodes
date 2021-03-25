#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums)-1
        res = [-1 , -1]
        while left <= right:
            mid = (left+right)//2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                res = [mid, mid]
                r, l = mid, mid
                while l+1 <= len(nums)-1 and nums[l+1] == target:
                    res[1] = l + 1
                    l += 1
                while r-1 >= 0 and nums[r-1] == target:
                    res[0] = r - 1
                    r -= 1
                break
        return res
# @lc code=end

num = [1]
if num[1]:
    print("w")
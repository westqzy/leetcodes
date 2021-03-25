    #
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # copy_num_pos = dict(zip(nums, range(len(nums))))
        # print(copy_num_pos)
        # for i in range(1, len(nums)):
        #     if nums[i] < nums[i-1]:
        #         nums = nums[i:] + nums[:i]
        #         break
        # left = 0
        # right = len(nums)-1
        # while left <= right:
        #     mid = (left + right)//2
        #     if nums[mid] < target:
        #         left = mid + 1
        #     elif nums[mid] > target:
        #         right = mid - 1
        #     else:
        #         return copy_num_pos[nums[mid]]
        # return -1
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[len(nums) - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

        # try:
        #     return nums.index(target)
        # except:
        #     return -1
# @lc code=end
nums= [4,5,6,7,0,1,2]
s = "-".join(map(str, nums))

print(s)
#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-2 , -1, -1):
            if nums[i] < nums[i+1]:
                for j in range(len(nums)-1, i, -1):
                    if nums[j] > nums[i]:
                        nums[i], nums[j] = nums[j], nums[i]
                        print(nums[i+1:])
                        nums[i+1:] = reversed(nums[i+1:])
                        break
                break
        else:
            nums.reverse()
        # print(nums)


# @lc code=end


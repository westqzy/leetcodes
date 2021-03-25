#
# @lc app=leetcode.cn id=665 lang=python3
#
# [665] 非递减数列
#

# @lc code=start
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0 
        max_n = float("-inf")
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1] and nums[i+1] >= max_n:
                count += 1
                nums[i] = nums[i+1]
            if nums[i] > nums[i+1] and nums[i+1] < max_n:
                count += 1
                nums[i+1] = nums[i]
            if count >= 2:
                return False
            max_n = max(max_n, nums[i])
        return True
# @lc code=end

a= [1,2,3,4,5]
b = [2,3,4,5,1]
print(a-b)
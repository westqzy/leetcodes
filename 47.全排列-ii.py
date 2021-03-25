#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrace(index):
            if index == len(nums):
                zuhes.append(zuhe[:])
            else:
                for i in range(len(nums)):
                    if not used[i]:
                        if i > 0 and nums[i] == nums[i-1] and used[i-1] == False:
                            continue
                        used[i] = True
                        zuhe.append(nums[i])
                        backtrace(index+1)
                        zuhe.pop()
                        used[i] = False

        nums.sort()              
        zuhes = list()
        zuhe = list()
        used = [False for _ in range(len(nums))]
        backtrace(0)
        return zuhes

# @lc code=end


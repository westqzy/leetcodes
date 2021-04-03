#
# @lc app=leetcode.cn id=376 lang=python3
#
# [376] 摆动序列
#

# @lc code=start
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # if len(nums) <= 1:
        #     return len(nums)
        # dp = [[]]*len(nums)
        # for i in range(len(nums)):
        #     dp[i] = [nums[i]]
        # for i in range(1,len(nums)):
        #     for j in range(i-1, -1, -1):
        #         if len(dp[j]) == 1:
        #             if  nums[i] != nums[j]:
        #                 dp[i]= dp[j] + [nums[i]]
        #             else:
        #                 break
        #         else:
        #             if (nums[i]-dp[j][-1])*(dp[j][-1]-dp[j][-2])<0:
        #                 dp[i]= dp[j] + [nums[i]]
        #                 break
        # # return len(dp[-1])

        # down = 1
        # up = 1
        # if len(nums) <= 1:
        #     return len(nums) 
        # for i in range(1, len(nums)):
        #     if nums[i] > nums[i-1]:
        #         up = down + 1
        #     elif nums[i] < nums[i-1]:
        #         down = up + 1
        # return max(down, up)
        
        # 贪心
        if len(nums) <= 1:
            return len(nums) 
        cur = 0
        pre = 0
        res = 1
        for i in range(1, len(nums)):
            cur = nums[i] - nums[i-1]
            if (pre <= 0 and cur > 0) or (pre >= 0 and cur < 0):
                pre = cur
                res += 1
        return res
# @lc code=end

def wiggleMaxLength(nums):
        if len(nums) <= 1:
            return len(nums)
        dp = [[]]*len(nums)
        for i in range(len(nums)):
            dp[i] = [nums[i]]
        for i in range(1,len(nums)):
            for j in range(i-1, -1, -1):
                if len(dp[j]) == 1:
                    if  nums[i] != nums[j]:
                        dp[i]= dp[j] + [nums[i]]
                    else:
                        break
                else:
                    if (nums[i]-dp[j][-1])*(dp[j][-1]-dp[j][-2])<0:
                        dp[i]= dp[j] + [nums[i]]
                        break
        print(dp)
wiggleMaxLength( [1,2,3,4,5,6,7,8,9])
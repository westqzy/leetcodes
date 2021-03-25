#
# @lc app=leetcode.cn id=368 lang=python3
#
# [368] 最大整除子集
#

# @lc code=start
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # if len(nums) <= 1:
        #     return nums
        # nums.sort()
        # dp = []
        # for i in nums:
        #     dp.append([i])
        # for i in range(1, len(nums)):
        #     try:
        #         dp[i] = max([dp[j]  for j in range(i) if 
        #             nums[i] % dp[j][-1] == 0], key=len) + [nums[i]]
        #     except:
        #         pass
        # #print(dp)
        # max_res = max(dp, key=len)
        # return max_res
        subsets = {-1: set()}
        
        for num in sorted(nums):
            subsets[num] = max([subsets[k] for k in subsets if num % k == 0], 
                    key=len) | {num}
        
        return list(max(subsets.values(), key=len))


        
# @lc code=end
def largestDivisibleSubset(nums) :
        if len(nums) <= 1:
            return nums
        nums.sort()
        dp = []
        for i in nums:
            dp.append([i])
        for i in range(1, len(nums)):
            try:
                dp[i] = max([dp[j]  for j in range(i) if 
                    nums[i] % dp[j][-1] == 0], key=len) + [nums[i]]
            except:
                pass
        print(dp)
        max_res = max(dp, key=len)
        return max_res

print(largestDivisibleSubset([3,14]))

#1, 2, 3, 4, 6, 8
#[1] [1,2] [1,3] [1,2,4] [1,3,6], [1,2,4,8]
# 1 2 2 3 3 4

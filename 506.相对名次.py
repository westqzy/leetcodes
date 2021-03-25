#
# @lc app=leetcode.cn id=506 lang=python3
#
# [506] 相对名次
#

# @lc code=start
class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        res = [0]*len(nums)
        list2 = [i for i in range(len(nums))]
        dict1 = dict(zip(nums,list2))
        nums.sort()
        nums.reverse()
        for i in range(len(nums)):
            if i == 0:
                res[dict1[nums[i]]] = "Gold Medal"
            elif i == 1:
                res[dict1[nums[i]]] = "Silver Medal"
            elif i == 2:
                res[dict1[nums[i]]] = "Bronze Medal"
            else:
                res[dict1[nums[i]]] = str(i+1)
        return res
# @lc code=end
nums = [5,4,3,2,1]
nums.sort()
print(nums)
#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        seen = list()

        def traceback(start):
            ress.append(res[:])
            for i in range(start, len(nums)):
                if i != start and nums[i] == nums[i-1]:
                    continue
                res.append(nums[i])
                traceback(i+1)
                res.pop()

        ress = []
        res = []
        traceback(0)
        return ress
# @lc code=end


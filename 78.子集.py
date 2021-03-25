#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
import itertools
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrace(index:int, res:list, start:int):
            ress.append(res[:])
            for i in range(start, len(nums)):
                res.append(nums[i])
                backtrace(index+1, res, i+1)
                res.pop()
        ress = []
        
        backtrace(0, [], 0)
        #print(ress)
        return ress
        # ress = []
        # for i in range(len(nums)+1):
        #     ress.extend(list(itertools.combinations(nums, i)))
        # return ress
# @lc code=end


#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
import itertools
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 排列组合函数
        # return list(map(list, itertools.permutations(nums, len(nums))))

        #回溯
        def backtrace(index):
            if index == len(nums):
                zuhes.append(zuhe[:])
            else:
                for i in range(len(now)):
                    zuhe.append(now[i])
                    pop_z = now.pop(i)
                    backtrace(index + 1)
                    now.insert(i, pop_z)
                    zuhe.pop()
        zuhe = list()
        zuhes = list()
        now = nums[:]
        backtrace(0)
        return zuhes
# @lc code=end

print([1,2,3] + [2])
#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
import collections
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if sum(candidates) < target:
            return []
        if sum(candidates) == target:
            return [candidates]
        def backtrace(start, now, jie):
            if now < 0:
                return
            if now == 0:
                res.append(jie)
            else:
                for index in range(start, len(candidates)):
                    if index > start and candidates[index] == candidates[index-1]:
                        continue
                    backtrace(index+1, now-candidates[index], jie+[candidates[index]])
        candidates.sort()
        res = list()
        chong = list()
        backtrace(0, target, [])
        return res
# @lc code=end
chong = list()
jie = [1,2,5]
chong.append(set(jie))
jie2 = [2,2,5]
if set(jie2) in chong:
    print(0)
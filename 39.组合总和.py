#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrace(start):
            if sum(jie) > target:
                return
            elif sum(jie) == target:
                jie_c = jie[:]
                jies.append(jie_c)
                return
            else:
                new_can = candidates[start:]
                for i in range(len(new_can)):
                    jie.append(new_can[i])
                    backtrace(start+i)
                    jie.pop()
        jie = []
        jies = []
        backtrace(0)
        return jies
# @lc code=end


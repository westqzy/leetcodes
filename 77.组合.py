#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
import itertools
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:   
        return list(itertools.combinations(range(1, n+1), k))
        # list_all = range(1, n+1)
        # if n == 0 or k == 0:
        #     return []
        # def backtrace(index, start):
        #     if index == k:
        #         ress.append(res[:])
        #     else:
        #         for i in range(start, len(list_all)):
        #             res.append(list_all[i])
        #             backtrace(index+1, 1+i)
        #             res.pop()
                    
        # res = list()
        # ress = list()
        # backtrace(0, 0)
        # print(ress)
        # return ress
# @lc code=end
[1,2,3,4]

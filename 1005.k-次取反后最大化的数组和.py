#
# @lc app=leetcode.cn id=1005 lang=python3
#
# [1005] K 次取反后最大化的数组和
#

# @lc code=start
class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        for _ in range(K):
            min_A = min(A)
            min_i = A.index(min_A)
            A[min_i] = -min_A
        return sum(A)
        
# @lc code=end


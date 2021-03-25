#
# @lc app=leetcode.cn id=888 lang=python3
#
# [888] 公平的糖果交换
#

# @lc code=start
class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        sum_all = sum(A) + sum(B)
        sum_all //= 2
        sub_A = sum(A) - sum_all
        b_set = set(B)
        for i in A:
            change_A = i - sub_A
            if change_A in b_set:
                return [i, change_A]

# @lc code=end


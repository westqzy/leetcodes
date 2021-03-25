#
# @lc app=leetcode.cn id=1534 lang=python3
#
# [1534] 统计好三元组
#

# @lc code=start
import itertools
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        return sum(abs(i-j) <= a and abs(j-k) <= b and abs(i-k) <= c for i, j, k in itertools.combinations(arr, 3))
# @lc code=end


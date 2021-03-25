#
# @lc app=leetcode.cn id=441 lang=python3
#
# [441] 排列硬币
#

# @lc code=start
class Solution:
    def arrangeCoins(self, n: int) -> int:
        num = 0
        hang = 1
        while num <= n:
            num += hang
            hang += 1
        return hang -2 
# @lc code=end


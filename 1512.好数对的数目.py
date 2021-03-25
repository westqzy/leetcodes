#
# @lc app=leetcode.cn id=1512 lang=python3
#
# [1512] 好数对的数目
#

# @lc code=start
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hash1 = {}
        for i in nums:
            hash1[i] = hash1.get(i, 0)+1
        res = 0
        for i in hash1.values():
            if i > 1:
                res += (i*(i-1))//2
        return res
# @lc code=end


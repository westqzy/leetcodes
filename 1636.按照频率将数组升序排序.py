#
# @lc app=leetcode.cn id=1636 lang=python3
#
# [1636] 按照频率将数组升序排序
#

# @lc code=start
import collections
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        hash1 = collections.Counter(nums)
        sort = sorted(hash1.items(), key = lambda t: (t[1], -t[0]))
        res = []
        for i, j in sort:
            res.extend([i]*j)
        return res
# @lc code=end
import collections
nums = [2,3,1,3,2]
hash1 = collections.Counter(nums)
sort = sorted(hash1.items(), key = lambda t: (t[1], -t[0]))
print(sort)
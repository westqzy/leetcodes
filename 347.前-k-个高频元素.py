#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash1 = collections.Counter(nums)
        # listres = sorted(hash1.keys(), key = lambda x : hash1[x], reverse=True)
        # return listres[:k]
        return [i[0] for i in hash1.most_common(k)]
# @lc code=end


a = "123四"
print(a.isnumeric())
print(a.zfill(9))
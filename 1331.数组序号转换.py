#
# @lc app=leetcode.cn id=1331 lang=python3
#
# [1331] 数组序号转换
#

# @lc code=start
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sort = sorted(set(arr))
        hash1 = dict(zip(sort, range(len(arr))))
        print(hash1)
        return [hash1[i] + 1 for i in arr ]

# @lc code=end


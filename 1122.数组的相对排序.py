#
# @lc app=leetcode.cn id=1122 lang=python3
#
# [1122] 数组的相对排序
#

# @lc code=start
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        hash1 = {}
        for i in arr1:
            hash1[i] = hash1.get(i, 0)+1
        res = []
        for i in arr2:
            res.extend([i]*hash1[i])
            del hash1[i]
        for i in sorted(hash1.keys()):
            res.extend([i]*hash1[i])
        return res



        #############对元组排序
# @lc code=end


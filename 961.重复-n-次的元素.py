#
# @lc app=leetcode.cn id=961 lang=python3
#
# [961] 重复 N 次的元素
#

# @lc code=start
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        hash1 = {}
        for i in A:
            hash1[i] = hash1.get(i, 0)+1
        for i, j in hash1.items():
            if j == len(A)//2:
                return i
# @lc code=end


#
# @lc app=leetcode.cn id=905 lang=python3
#
# [905] 按奇偶排序数组
#

# @lc code=start
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i = 0
        j = len(A) - 1
        while i < j:
            while A[i] % 2 == 0 and i<j:
                i += 1
            while A[j] % 2 == 1 and i<j:
                j -= 1
            if i < j:
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1
        return A
# @lc code=end


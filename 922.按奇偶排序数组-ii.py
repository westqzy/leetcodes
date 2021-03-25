#
# @lc app=leetcode.cn id=922 lang=python3
#
# [922] 按奇偶排序数组 II
#

# @lc code=start
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        oucuo = []
        jicuo = []
        for i, j in enumerate(A):
            if i % 2 == 0: # 第偶数个
                if j % 2 != 0:
                    oucuo.append(i)
            else: # 第奇数个
                if j % 2 == 0:
                    jicuo.append(i)
        for i in range(len(jicuo)):
            A[jicuo[i]], A[oucuo[i]] = A[oucuo[i]], A[jicuo[i]]
        return A
# @lc code=end


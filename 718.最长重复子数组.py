#
# @lc app=leetcode.cn id=718 lang=python3
#
# [718] 最长重复子数组
# 

# @lc code=start
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        dp = [[0 for i in range(len(B))] for j in range(len(A))]
        res = 0
        # 初始化---------------------------
        for i in range(len(A)):
            if A[i] == B[0]:
                dp[i][0] = 1
        for j in range(len(B)):
            if B[j] == A[0]:
                dp[0][j] = 1
        #---------------------------------
        for i in range(1, len(A)):
            for j in range(1, len(B)):
                if A[i] == B[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                res = max(dp[i][j], res)
        return res
# @lc code=end
import numpy as np
def findLength(A, B):
        dp = [[0 for i in range(len(B))] for j in range(len(A))]
        for i in range(len(A)):
            if A[i] == B[0]:
                dp[i][0] = 1
        for j in range(len(B)):
            if B[j] == A[0]:
                dp[0][j] = 1
        for i in range(1, len(A)):
            for j in range(1, len(B)):
                if A[i] == B[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
        print(np.array(dp))
        return dp[-1][-1]
A = [0,1,1,1,1]
B = [1,0,1,0,1]
print(findLength(A,B))
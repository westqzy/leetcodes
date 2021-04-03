# @before-stub-for-debug-begin
from python3problem62 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
import numpy as np
from numpy.core.fromnumeric import shape
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = np.ones(shape=(m, n))
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return int(dp[-1][-1])
        # dp = [[1 for i in range(n)] for j in range(m)]
        # for i in range(1, m):
        #     for j in range(1, n):
        #         dp[i][j] = dp[i-1][j]+dp[i][j-1]
        # return dp[m-1][n-1]
# @lc code=end

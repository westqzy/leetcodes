#
# @lc app=leetcode.cn id=1619 lang=python3
#
# [1619] 删除某些元素后的数组均值
#

# @lc code=start
import numpy as np
class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n = int(len(arr)*(0.05))
        arr = arr[n:-n]
        #np.array(arr)
        print(arr)
    
        return np.mean(arr) 
# @lc code=end


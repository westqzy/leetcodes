#
# @lc app=leetcode.cn id=1089 lang=python3
#
# [1089] 复写零
#

# @lc code=start
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        while(i <= len(arr)-1):
            if arr[i] == 0:
                for j in range(len(arr)-1, i, -1):
                    arr[j] = arr[j-1]
                i += 1
            i += 1
                
            
# @lc code=end


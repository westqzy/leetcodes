#
# @lc app=leetcode.cn id=941 lang=python3
#
# [941] 有效的山脉数组
#

# @lc code=start
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        sub_p = arr.index(max(arr))
        if sub_p == len(arr)-1 or sub_p == 0:
            return False
        up = arr[:sub_p]
        down = arr[sub_p:]
        for i in range(1, len(up)):
            if up[i] <= up[i-1]:
                return False
        for i in range(1, len(down) ):
            if down[i] >= down[i-1]:
                return False
        return True
# @lc code=end


#
# @lc app=leetcode.cn id=1539 lang=python3
#
# [1539] 第 k 个缺失的正整数
#

# @lc code=start
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i = 1
        j = 0
        arr.extend([0]*k)
        print(arr)
        while k > 0:
            if i == arr[j]:
                j += 1
            else:
                k -= 1
            i += 1 
        return i-1
# @lc code=end


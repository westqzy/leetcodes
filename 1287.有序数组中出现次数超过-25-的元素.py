#
# @lc app=leetcode.cn id=1287 lang=python3
#
# [1287] 有序数组中出现次数超过25%的元素
#

# @lc code=start
import collections
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        hash1 = collections.Counter(arr)
        print(len(arr)//4)
        for i, j in hash1.items():
            if j > len(arr)//4:
                return i

# @lc code=end
import bisect
a = [1,2,2,4,3,4,5,6,3]
po = bisect.bisect(a,3)
print(po)
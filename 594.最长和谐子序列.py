#
# @lc app=leetcode.cn id=594 lang=python3
#
# [594] 最长和谐子序列
#

# @lc code=start
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        dict1 = dict()
        for i in nums:
            dict1[i] = dict1.get(i, 0)+1
        maxl = 0
        for i in dict1.keys():
            if dict1.get(i+1):
                maxl = max(maxl, dict1[i]+dict1.get(i+1, 0))
        return maxl
# @lc code=end

a = {"1":1,"2":3}
print(a.get("3"))
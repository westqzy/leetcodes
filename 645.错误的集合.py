#
# @lc app=leetcode.cn id=645 lang=python3
#
# [645] 错误的集合
#

# @lc code=start
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        hash1 = {}
        for i in nums:
            hash1[i] = hash1.get(i,0)+1
        n1 = 0
        n2 = 0
        for i in range(1, len(nums)+1):
            if hash1.get(i) == None:
                n2 = i
            if hash1.get(i) == 2:
                n1 = i
        return [n1, n2]
# @lc code=end

a= {1:1,2:2}
print(a.get(3))
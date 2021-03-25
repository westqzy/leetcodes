#
# @lc app=leetcode.cn id=697 lang=python3
#
# [697] 数组的度
#

# @lc code=start
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        #print("".join(map(str,nums)))
        hash1 = {}
        for i in nums:
            hash1[i] = hash1.get(i, 0)+1
        max_ = 0
        for i in hash1.values():
            max_ = max(i, max_)
        max_list = []
        for i,j in hash1.items():
            if j == max_:
                max_list.append(i)
        min_res = float("inf")
        #print(max_list)
        for i in max_list:
            nums2 = list(reversed(nums))
            min_res = min(min_res, len(nums)-nums2.index(i)-nums.index(i))
        return min_res
        
# @lc code=end
nums = [10,9,9,9]
nums2 = list(reversed(nums))
print(nums, nums2)
hash1 = {}
for i in nums:
    hash1[i] = hash1.get(i, 0)+1
max_ = 0
for i in hash1.values():
    max_ = max(i, max_)
max_list = []
for i,j in hash1.items():
    if j == max_:
        max_list.append(i)
min_res = float("inf")
print(max_list)
for i in max_list:
    nums2 = list(reversed(nums))
    min_res = min(min_res, nums2.index(i)-nums.index(i)+1)
print(min_res)
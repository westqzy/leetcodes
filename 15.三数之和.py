#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
import itertools
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 直接超时
        # res = set()
        # nums.sort()
        # for i in itertools.combinations(nums, 3):
        #     if sum(i) == 0:
        #         res.add(i)
        # print(res)
        # res = list(res)
        # return res
        res = []
        #先排序
        nums.sort()
        for i in range(len(nums)-2):
            #找到一个特值，需要在后面找到两个元素和等于它
            te = -nums[i]
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            p1 = i + 1
            p2 = len(nums) - 1
            while p1 < p2:
                if nums[p1] + nums[p2] < te:
                    p1 += 1
                    while p1 < p2 and nums[p1] == nums[p1-1]:
                        p1 += 1
                elif nums[p1] + nums[p2] > te :
                    p2 -= 1
                    while p1 < p2 and  nums[p2] == nums[p2+1]:
                        p2 -= 1
                else:
                    res.append([nums[i], nums[p1], nums[p2]])
                    p1 += 1
                    p2 -= 1
                    while p1 < p2 and nums[p1] == nums[p1-1]:
                        p1 += 1
                    while p1 < p2 and nums[p2] == nums[p2+1]:
                        p2 -= 1
        return res 
# @lc code=end
a = (1,2,3)
b = set()
b.add(a)
print(b)
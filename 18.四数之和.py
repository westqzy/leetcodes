#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                p1 = j+1
                p2 = n-1
                while p1 < p2:
                    s = nums[p1]+nums[p2]+nums[i]+nums[j]
                    if s < target:
                        p1 += 1
                        while p1 < p2 and nums[p1] == nums[p1-1]:
                            p1 += 1
                    elif s > target:
                        p2 -= 1
                        while p1 < p2 and nums[p2] == nums[p2+1]:
                            p2 -= 1
                    else:
                        res.append([nums[i], nums[j], nums[p1], nums[p2]])
                        p1 += 1
                        p2 -= 1
                        while p1 < p2 and nums[p2] == nums[p2+1]:
                            p2 -= 1
                        while p1 < p2 and nums[p1] == nums[p1-1]:
                            p1 += 1
        return res


# @lc code=end


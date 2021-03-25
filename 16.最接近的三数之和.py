#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = float("inf")
        for i in range(len(nums)):
            p1 = i+1
            p2 = len(nums)-1
            while p1 < p2:
                suma = nums[p1] + nums[p2] + nums[i]
                if abs(suma - target) < abs(res - target):
                    res = suma
                if suma > target:
                    p2 -= 1
                elif suma < target:
                    p1 += 1
                else:
                    return suma
        return res 
                        
            

# @lc code=end


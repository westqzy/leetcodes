#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        p1 = 0
        p2 = 0
        sum_all = 0
        res = len(nums) + 1
        while p2 <= len(nums) - 1:
            sum_all += nums[p2]
            while p1 <= len(nums) - 1 and sum_all >= target:
                res = min(res, p2 - p1 + 1)
                sum_all -= nums[p1]
                p1 += 1
            p2 += 1
        return 0 if res == len(nums) + 1 else res
# @lc code=end
import functools
@functools.lru_cache()
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

print(fibonacci(100))

print('\n'.join([''.join([('ZhaoMengZe'[(x-y)%10]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y in range(15,-15,-1)]))


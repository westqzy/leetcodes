#
# @lc app=leetcode.cn id=453 lang=python3
#
# [453] 最小移动次数使数组元素相等
#

# @lc code=start
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - len(nums) * min(nums)
                
# @lc code=end
def minMoves(nums) -> int:
        max_loc = 0
        count = 0
        while len(set(nums)) != 1:
            for i in range(len(nums)):
                if nums[max_loc] >= nums[i]:
                    max_loc = i
            print(max_loc)
            for i in range(len(nums)):
                if i != max_loc:
                    nums[i] += 1
            count += 1
        print(count)
minMoves([1,2,3])
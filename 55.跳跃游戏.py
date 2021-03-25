#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums)-1
        maxlen = 0
        for i in range(len(nums)):
            if i <= maxlen:
                maxlen = max(maxlen, i+nums[i])
            if maxlen >= target:
                return True
        return False

# @lc code=end


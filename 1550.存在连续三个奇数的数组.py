#
# @lc app=leetcode.cn id=1550 lang=python3
#
# [1550] 存在连续三个奇数的数组
#

# @lc code=start
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        ji = 0
        for i in arr:
            if i % 2 == 1:
                ji += 1
            else:
                ji = 0
            if ji == 3:
                return True
        return False
# @lc code=end


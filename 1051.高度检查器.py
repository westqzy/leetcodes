#
# @lc app=leetcode.cn id=1051 lang=python3
#
# [1051] 高度检查器
#

# @lc code=start
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        heights_s = sorted(heights)
        res = [i-j for i,j in zip(heights, heights_s)]
        print(res)
        return len(res)-res.count(0)
# @lc code=end

print(list(zip([1,2,3],[2,3,4])))
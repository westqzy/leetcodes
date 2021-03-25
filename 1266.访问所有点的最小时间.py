#
# @lc app=leetcode.cn id=1266 lang=python3
#
# [1266] 访问所有点的最小时间
#

# @lc code=start
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        return sum([max(abs(points[i][0]-points[i+1][0]), abs(points[i][1]-points[i+1][1])) for i in range(len(points)-1)])
# @lc code=end
a =sum([])
print(a)

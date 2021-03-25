#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda ele: (ele[0], ele[1]))
        i = 0
        while i < len(intervals)-1:
            if intervals[i][1] >= intervals[i+1][0]:
                intervals[i] = [intervals[i][0], max(intervals[i+1][1], intervals[i][1])]
                intervals.pop(i+1)
            else:
                i += 1
        return intervals   
# @lc code=end


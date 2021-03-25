#
# @lc app=leetcode.cn id=492 lang=python3
#
# [492] 构造矩形
#

# @lc code=start
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        lilun = math.sqrt(area)
        if int(lilun) == lilun:
            return ([int(lilun)]*2)
        else:
            lilun = int(lilun)
            while area % lilun != 0:
                lilun -= 1
            return ([int(area / lilun),lilun])
# @lc code=end

import math
area = 459
lilun = math.sqrt(area)
if int(lilun) == lilun:
    print([int(lilun)]*2)
else:
    lilun = int(lilun)
    while area % lilun != 0:
        lilun -= 1
    print([lilun,int(area / lilun)])

#
# @lc app=leetcode.cn id=1185 lang=python3
#
# [1185] 一周中的第几天
#

# @lc code=start
import datetime
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        return datetime.datetime(year,month,day).strftime("%A")
# @lc code=end

import datetime
n = datetime.datetime(1991,12,21).strftime("%j")
print(n)
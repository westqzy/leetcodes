#
# @lc app=leetcode.cn id=1154 lang=python3
#
# [1154] 一年中的第几天
#

# @lc code=start
from datetime import datetime
class Solution:
    def dayOfYear(self, date: str) -> int:
        return int(datetime.strptime(date, '%Y-%m-%d').strftime("%j"))
# @lc code=end

        # year = int(date.split("-")[0])
        # month =int(date.split("-")[1])
        # date = int(date.split("-")[2])
        # month_l = [0,31,28,31,30,31,30,31,31,30,31,30,31]
        # if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        #     month_l[2] = 29
        # res = 0
        # for i in range(month):
        #     res += month_l[i]
        # res += date


        # return res
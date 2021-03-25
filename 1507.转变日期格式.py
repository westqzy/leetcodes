#
# @lc app=leetcode.cn id=1507 lang=python3
#
# [1507] 转变日期格式
#

# @lc code=start
import datetime
class Solution:
    def reformatDate(self, date: str) -> str:
        day = int(date.split(" ")[0][:-2])
        mon_l = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"] 
        year = int(date.split(" ")[2])
        month = mon_l.index(date.split(" ")[1])+1    
        return datetime.datetime(year, month, day).strftime("%Y-%m-%d")
# @lc code=end
import re

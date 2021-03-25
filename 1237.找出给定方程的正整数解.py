#
# @lc app=leetcode.cn id=1237 lang=python3
#
# [1237] 找出给定方程的正整数解
#

# @lc code=start
"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:

        res = []
        for i in range(1, 1001):
            if customfunction.f(i, 1) > z:
                break
            left = 1
            right = 1000
            while left <= right:
                mid = (left + right) // 2
                if customfunction.f(i, mid) == z:
                    res.append([i, mid])
                    break
                elif customfunction.f(i, mid) > z:
                    right = mid-1
                else:
                    left = mid+1
                
        return res

        
# @lc code=end

class Ticket():
    def __init__(self,checi,fstation,tstation,fdate,ftime,ttime):
        self.checi=checi
        self.fstation=fstation
        self.tstation=tstation
        self.fdate=fdate
        self.ftime=ftime
        self.ttime=ttime
    def printinfo(self):
        print("车次：",self.checi)
        print("出发站：", self.fstation)
        print("到达站：", self.tstation)
        print("出发时间：", self.fdate)

a = Ticket("G11","xian","beijing",'2019-01-20','13:00','18:00')
a.printinfo()
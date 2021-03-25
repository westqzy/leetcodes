#
# @lc app=leetcode.cn id=690 lang=python3
#
# [690] 员工的重要性
#

# @lc code=start
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        list_e = {employee.id:employee for employee in employees}
        def zyx(eid):   
            return list_e[eid].importance + sum(zyx(i) for i in list_e[eid].subordinates)            
        return zyx(id)
# @lc code=end
sum2 = 1
def add(a,b,sum2):
    sum2 =  a+b + sum2
    return sum2
print(add(1,5,sum2))
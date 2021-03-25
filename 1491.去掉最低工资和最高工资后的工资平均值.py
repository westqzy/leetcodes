
# @lc app=leetcode.cn id=1491 lang=python3
#
# [1491] 去掉最低工资和最高工资后的工资平均值
#

# @lc code=start
import numpy as np
class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        salary = np.array(salary[1:-1])
        mean = np.mean(salary, 0)
        return float(mean)
# @lc code=end
import numpy as np
salary = [3000,2000,1000,4400]
salary.sort()
salary = np.array(salary)
mean = np.mean(salary, 0)
print(mean)
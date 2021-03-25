#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
import numpy
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # ma = numpy.array(matrix)
        # ma = ma.flatten()
        # return target in ma 
        
        # 全局二分
        存在 = True
        不存在 = False
        原始数组 = matrix
        目标 = target
        宽度 = len(原始数组)
        长度 = len(原始数组[0])
        总长度 = 长度*宽度
        左边 = 0
        右边 = 总长度 - 1
        while 左边 <= 右边:
            中间 = (左边 + 右边) // 2
            中间值 = 原始数组[中间 // 长度][中间 % 长度]
            if 中间值 == 目标:
                return 存在
            elif 中间值 < 目标:
                左边 = 左边 + 1
            else:
                右边 = 中间 - 1
        return 不存在

# @lc code=end
import numpy
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
ma = numpy.array(matrix)
ma = ma.flatten()
target = 3
a =  sorted(ma)
print(all(a == ma))
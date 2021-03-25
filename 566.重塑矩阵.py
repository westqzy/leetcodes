#
# @lc app=leetcode.cn id=566 lang=python3
#
# [566] 重塑矩阵
#

# @lc code=start
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        gen_list = []
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                gen_list.append(nums[i][j])
        if len(gen_list) != r*c:
            return nums
        res = [[0 for i in range(c)] for i in range(r)]
        n = 0
        for i in range(r):
            for j in range(c):
                res[i][j] = gen_list[n]
                n += 1    
        return res
        #以下为好方法啊！
        # m,n=len(nums),len(nums[0])
        # if m*n!=r*c:
        #     return nums
        # res=[i for j in nums for i in j]    
        # return [res[i:i+c] for i in range(0,len(res),c)]
# @lc code=end


#以下是错误的
c = 4
r = 4
res = [[0] * c] * r
n = 0
for i in range(r):
    for j in range(c):
        res[i][j] = n
        n += 1
print(res) 

res = [[0]]*5
for i in range(5):
    res[i][0] = i
print(res)

res = [[0] for i in range(5)]
for i in range(5):
    res[i][0] = i
print(res)


import numpy as np
nums = [[1,2],[3,4]]
nums = np.reshape(nums,(4,1))
print(nums)
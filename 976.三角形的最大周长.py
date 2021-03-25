#
# @lc app=leetcode.cn id=976 lang=python3
#
# [976] 三角形的最大周长
#

# @lc code=start
import itertools
class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        #超时间
        # res = 0
        # for i in itertools.combinations(A, 3):
        #     list1 = list(i)
        #     list1.sort()
        #     if list1[0] + list1[1] > list1[2]:
        #         res = max(res, sum(list1))
        # return res
        #A = list()
        A.sort()
        A.reverse()
        for i in range(2,len(A)):
            if A[i] + A[i-1] > A[i-2]:
                return A[i] + A[i-1] + A[i-2]
        return 0
# @lc code=end
import itertools
A = [3,6,2,3]
for i in itertools.combinations(A, 3):
    print(i)
a= (1,3,4)
al = list(a)
print(al)
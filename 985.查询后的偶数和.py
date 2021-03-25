#
# @lc app=leetcode.cn id=985 lang=python3
#
# [985] 查询后的偶数和
#

# @lc code=start
class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        oushu_sum = sum([i if i % 2 == 0 else 0 for i in A])
        for i, j in queries:
            if A[j] % 2 == 0: #添加位置偶数
                if i % 2 == 0:#添加的为偶数
                    oushu_sum = oushu_sum + i
                else:
                    oushu_sum = oushu_sum - A[j]
            else:
                if i % 2 == 0:#添加的为偶数
                    pass
                else:
                    oushu_sum = oushu_sum + A[j] + i
            res.append(oushu_sum)
            A[j] += i
        return res
# @lc code=end
A = [1,2,3,4]
queries = [[1,0],[-3,1],[-4,0],[2,3]]
for i,j in queries:
    A[j] += i
a = [i if i % 2 == 0 else 0 for i in A]
print(a)
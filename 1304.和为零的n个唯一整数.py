#
# @lc app=leetcode.cn id=1304 lang=python3
#
# [1304] 和为零的N个唯一整数
#

# @lc code=start
class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        n_zheng = n
        for i in range(n//2):
            res.extend([n_zheng, -n_zheng])
            n_zheng -= 1
        if n % 2 == 1:
            res.append(0)
        return res
# @lc code=end

a =[]
a.extend([1,2])
print(a)
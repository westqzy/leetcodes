#
# @lc app=leetcode.cn id=1337 lang=python3
#
# [1337] 方阵中战斗力最弱的 K 行
#

# @lc code=start
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        def zhanli(l:list)->int:
            return sum(l)
        zhanli_list = list(map(zhanli, mat))
        ans = list(range(len(mat)))
        sort = sorted(ans, key=lambda x: zhanli_list[x])
        print(sort)
        res = []
        for i in range(k):
            res.append(sort[i])
        return res
# @lc code=end


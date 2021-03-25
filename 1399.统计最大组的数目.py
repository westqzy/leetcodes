#
# @lc app=leetcode.cn id=1399 lang=python3
#
# [1399] 统计最大组的数目
#

# @lc code=start
import collections
class Solution:
    def countLargestGroup(self, n: int) -> int:
        list1 = [i for i in range(1, n+1)]
        def change(n:int):
            res = 0
            while n > 0:
                a = n % 10
                res += a
                n //= 10
            return res
        list1 = list(map(change, list1))
        hash1 = collections.Counter(list1)
        res = collections.Counter(hash1.values()) 
        return res[max(res.keys())]                         
# @lc code=end


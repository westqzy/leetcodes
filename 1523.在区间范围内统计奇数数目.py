#
# @lc app=leetcode.cn id=1523 lang=python3
#
# [1523] 在区间范围内统计奇数数目
#

# @lc code=start
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        res = 0
        if low % 2 == 1:
            res += 1
            low += 1
        if high % 2 == 1:
            res += 1
            high -= 1
        return (high -low)//2 + res
        
# @lc code=end


import collections
d = {"banana":3,"apple":2,"pear":1,"orange":4}
a = sorted(d.items(), key=lambda t: t[1], reverse=True)
# a = collections.Counter(a)
print(a)

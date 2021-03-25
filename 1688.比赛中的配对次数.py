#
# @lc app=leetcode.cn id=1688 lang=python3
#
# [1688] 比赛中的配对次数
#

# @lc code=start
class Solution:
    def numberOfMatches(self, n: int) -> int:
        # res = 0
        # while n != 1:
        #     if n % 2 == 0:
        #         n //= 2
        #         res += n
        #     else:
        #         n = (n-1)//2
        #         res += n
        #         n += 1
        # return res
        return n-1
# @lc code=end


#
# @lc app=leetcode.cn id=1010 lang=python3
#
# [1010] 总持续时间可被 60 整除的歌曲
#

# @lc code=start
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        #超时
        # dp = [0]*len(time)
        # for i in range(1, len(time)):
        #     count = 0
        #     for j in range(i):
        #         if (time[i] + time[j]) % 60 == 0:
        #             count += 1 
        #     dp[i] = dp[i-1] + count
        # print(dp)
        # return dp[-1]
   
# @lc code=end


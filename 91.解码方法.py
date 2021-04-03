#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0]*(len(s)+1)
        if s[0] == "0":
            return 0
        dp[0] = 1  # 无实际作用
        dp[1] = 1  # 第一个数若不为0，则第一个数映射方法为1，作为入口
        for i in range(2, len(s)+1):
            if s[i-1] == "0":
                if s[i-2] != "1" and s[i-2] != "2":
                    return 0
                else:
                    dp[i] = dp[i-2]
            else:
                if s[i - 2] == "1" or (s[i - 2] == "2" and "1" <= s[i-1] <= "6"):
                    dp[i] += dp[i-2]
                dp[i] += dp[i-1]
        return dp[-1]



        # dp = [0]*(len(s)+1)
        # if s[0] == "0":
        #     return 0
        # dp[0] = 1
        # dp[1] = 1
        # for i in range(2, len(s)+1):
        #     if s[i-1] == "0" :
        #         if s[i-2] == "1" or s[i-2] == "2":
        #             dp[i] = dp[i-2]
        #         else:
        #             return 0
        #     else:
        #         if s[i-2] == "1":
        #             dp[i] = dp[i-2]+dp[i-1]
        #         elif s[i-2] == "2" and "1" <= s[i-1] <= "6":
        #             dp[i] = dp[i-2]+dp[i-1]
        #         else:
        #             dp[i] = dp[i-1]
        # return dp[-1]

# @lc code=end

#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp = [False]*(len(s)+1)
        # dp[0] = True
        # for i in range(len(s)):
        #     if dp[i] == True:
        #         for j in range(i+1, len(s)+1):
        #             if s[i:j] in wordDict:
        #                 dp[j] = True
        # return dp[-1]
        import functools
        @functools.lru_cache(None)
        def backtrace(s):
            if s == "":
                return True
            for i in range(1, len(s)+1):
                if s[:i] in wordDict:
                    if backtrace(s[i:]):
                        return True
            return False
        return backtrace(s)
# @lc code=end

a= "aaaaddda"
a = a.replace("v","")
print(a)
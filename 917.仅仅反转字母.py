#
# @lc app=leetcode.cn id=917 lang=python3
#
# [917] 仅仅反转字母
#

# @lc code=start
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        zimu = "abcdefghijklmnopqrstuvwxyz"
        zimu += zimu.upper()
        i = 0
        j = len(S) - 1
        res = list(S)
        while i <= j:
            while res[i] not in zimu and i < j:
                i += 1
            while res[j] not in zimu and i < j:
                j -= 1 
            if i <= j:
                res[i], res[j] = res[j], res[i]
                i += 1
                j -= 1
        return "".join(res)

    ##可以利用堆栈
# @lc code=end
S = "a-bC-dEf-ghIj"
zimu = "abcdefghijklmnopqrstuvwxyz"
zimu += zimu.upper()
print(len(zimu))

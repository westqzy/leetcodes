#
# @lc app=leetcode.cn id=821 lang=python3
#
# [821] 字符的最短距离
#

# @lc code=start
class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        # list_len = []
        # for i in range(len(S)):
        #     if S[i] == C:
        #         list_len.append(i)
        # res = []
        # for i in range(len(S)):
        #     res.append(min([abs(i-k) for k in list_len]))
        # return res
        prev = float("-inf")
        res1 = []
        res2 = []
        for i in range(len(S)):
            if S[i] == C:
                prev = i
            res1.append(i-prev)
        next = float("inf")
        for i in range(len(S)-1, -1, -1):
            if S[i] == C:
                next = i
            res2.append(next-i)
        res2.reverse()

        res = []
        for i in range(len(res1)):
            res.append(min(res2[i], res1[i]))
        return res
# @lc code=end
[3,5,6,11]

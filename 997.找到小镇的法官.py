#
# @lc app=leetcode.cn id=997 lang=python3
#
# [997] 找到小镇的法官
#

# @lc code=start
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N == 1:
            return 1
        hash1 = {}
        voter = set()
        for i, j in trust:
            hash1[j] = hash1.get(j, 0) + 1
            voter.add(i)
        for i, j in hash1.items():
            if j == N-1 and i not in voter:
                return i
        return -1
# @lc code=end
haha1 = {1,2}


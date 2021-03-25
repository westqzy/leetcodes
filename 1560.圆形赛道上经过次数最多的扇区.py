#
# @lc app=leetcode.cn id=1560 lang=python3
#
# [1560] 圆形赛道上经过次数最多的扇区
#

# @lc code=start
import collections
class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        hash1 = collections.defaultdict(int)
        hash1[rounds[0]] += 1
        for i in range(1, len(rounds)):
            if rounds[i] > rounds[i-1]:
                for j in range(rounds[i-1]+1, rounds[i]+1):
                    hash1[j] += 1
            else:
                for j in range(rounds[i-1]+1, n+1):
                    hash1[j] += 1
                for j in range(1, rounds[i]+1):
                    hash1[j] += 1
        print(hash1)
        maxv = max(hash1.values())
        return sorted([i for i, j in hash1.items() if j == maxv])
# @lc code=end


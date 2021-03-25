#
# @lc app=leetcode.cn id=1496 lang=python3
#
# [1496] 判断路径是否相交
#

# @lc code=start
import collections
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        pos = (0, 0)
        hash1 = collections.defaultdict(int)
        hash1[pos] += 1
        for i in path:
            if i == 'N':
                pos = (pos[0]+1, pos[1])
            elif i == 'S':
                pos = (pos[0]-1, pos[1])
            elif i =='E':
                pos = (pos[0], pos[1]+1)
            else:
                pos = (pos[0], pos[1]-1)
            hash1[pos] += 1
        print(hash1)
        for i in hash1.values():
            if i >= 2:
                return True
        return False


# @lc code=end


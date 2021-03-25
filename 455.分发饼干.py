#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0
        s.sort()
        g.sort()
        p1 = 0
        p2 = 0
        while p1 <= len(g)-1 and p2 <= len(s)-1:
            if g[p1] <= s[p2]:
                count += 1
                p1 += 1
                p2 += 1
            else:
                p2 += 1
        return count
# @lc code=end

def findContentChildren( g, s) -> int:
        count = 0
        s.sort()
        g.sort()
        p1 = 0
        p2 = 0
        while p1 <= len(g)-1 and p2 <= len(s)-1:
            if g[p1] <= s[p2]:
                count += 1
                p1 += 1
                p2 += 1
            else:
                p2 += 1
            print(p1,p2)
        print(count) 
findContentChildren([1,2,3],
[1,1])
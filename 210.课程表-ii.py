#
# @lc app=leetcode.cn id=210 lang=python3
#
# [210] 课程表 II
#

# @lc code=start
import collections
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        tu = collections.defaultdict(list)
        rudu = [0]*numCourses
        for ele in prerequisites:
            tu[ele[1]].append(ele[0])
            rudu[ele[0]] += 1
        ku = [i for i in range(numCourses) if rudu[i] == 0]
        #print(ku)
        total = 0
        res = []
        while ku:
            total += 1
            chu = ku.pop()
            res.append(chu)
            for i in tu[chu]:
                rudu[i] -= 1
                if rudu[i] == 0:
                    ku.append(i)
        return res if total == numCourses else []
                    
# @lc code=end


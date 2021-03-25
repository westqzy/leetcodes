#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#

# @lc code=start
import collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = collections.defaultdict(list)
        indeg = [0]*numCourses
        for ele in prerequisites:
            edges[ele[1]].append(ele[0])
            indeg[ele[0]] += 1
        que = collections.deque([i for i in range(numCourses) if indeg[i] == 0])
        #print(que)
        res = 0
        while que:
            u = que.popleft()
            res += 1
            for i in edges[u]:
                indeg[i] -= 1
                if indeg[i] == 0:
                    que.append(i)
        return res == numCourses
# @lc code=end


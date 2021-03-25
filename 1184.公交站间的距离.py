#
# @lc app=leetcode.cn id=1184 lang=python3
#
# [1184] 公交站间的距离
#

# @lc code=start
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        # i = start
        # j = start
        # dis = 0
        # dis2 = 0
        # if start == destination:
        #     return 0
        # while i != destination:
        #     dis += distance[i]
        #     i += 1
        #     if i == len(distance):
        #         i = 0
        # while j != destination:
        #     j -= 1
        #     if j == -1:
        #         j = len(distance)-1
        #     dis2 += distance[j]
        # mind = min(dis, dis2)
        # return mind
        d1 = sum(distance[min(start, destination): max(start, destination)])
        all_d = sum(distance)
        return min(d1, all_d-d1)
# @lc code=end


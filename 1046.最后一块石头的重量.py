#
# @lc app=leetcode.cn id=1046 lang=python3
#
# [1046] 最后一块石头的重量
#

# @lc code=start
import heapq 
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # while len(stones) > 1:
        #     stones.sort()
        #     a1 = stones.pop()
        #     a2 = stones.pop()
        #     print(stones)
        #     if a1 - a2 != 0:
        #         stones.append(a1-a2)
        # stones.append(0)
        # return stones[0]
        heap = [-i for i in stones]
        heapq.heapify(heap)
        while len(heap)>1:
            heapq.heappush(heap, heapq.heappop(heap) - heapq.heappop(heap))
        print(heap)
        return -heap[0]
# @lc code=end
import heapq
heap = [2,7,4,1,8,1]
heapq.heapify(heap)
print(heapq.heappop(heap))



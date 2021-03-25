#
# @lc app=leetcode.cn id=703 lang=python3
#
# [703] 数据流中的第 K 大元素
#

# @lc code=start
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.list = nums
        self.k = k
    def add(self, val: int) -> int:
        self.list.append(val)
        self.list.sort()
        return self.list[-self.k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end

list1 = [4, 5, 8, 2]
import heapq
heapq.heapify(list1)
heapq.heappop(list1)
print(list1)
#
# @lc app=leetcode.cn id=1356 lang=python3
#
# [1356] 根据数字二进制下 1 的数目排序
#

# @lc code=start
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key = lambda i: (bin(i).count("1"), i))

# @lc code=end
print(sum(map(int, list(bin(512)[2:]))))

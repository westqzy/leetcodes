#
# @lc app=leetcode.cn id=944 lang=python3
#
# [944] 删列造序
#

# @lc code=start
class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        res = 0
        for i in range(len(A[0])):
            list1 = [p[i] for p in A]
            list2 = list1[:]
            list1.sort()
            print(list1)
            if list2 != list1:
                res += 1
        return res


# @lc code=end
A = ["cba", "daf", "ghi"]
for i in zip(*A):
    if list(i) == sorted(i):
        print(sorted(i))
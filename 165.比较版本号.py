#
# @lc app=leetcode.cn id=165 lang=python3
#
# [165] 比较版本号
#

# @lc code=start
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int,version1.split(".")))
        v2 = list(map(int,version2.split(".")))
        minl = min(len(v1), len(v2))
        for i in range(minl):
            if v1[i] > v2[i]:
                return 1
            elif v1[i] < v2[i]:
                return -1
        for i in v1[minl:]:
            if i != 0:
                return 1
        for i in v2[minl:]:
            if i != 0:
                return -1
        return 0
# @lc code=end
version1 = "1.01"
v1 = map(int,version1.split("."))
print(v1[0])
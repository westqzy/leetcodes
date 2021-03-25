#
# @lc app=leetcode.cn id=89 lang=python3
#
# [89] 格雷编码
#

# @lc code=start
class Solution:
    def grayCode(self, n: int) -> List[int]:
        have = set([0])
        def backtrace(path):
            if len(path) == 2**n:
                return path
            for i in range(n):
                nxt = 1 << i ^ path[-1]
                if nxt in have:
                    continue
                path.append(nxt)
                have.add(nxt)
                if backtrace(path):
                    return path
                have.remove(path.pop())
        ress = backtrace([0])
        return ress
# @lc code=end
res = [0]
n = 3
nxt = bin(res[-1])[2:].zfill(n)

print(nxt)
# 000   0
# 001   1
# 011   3
# 010   2
# 110   6
# 111   7
# 101   5
# 100   4
path=[0]
nxt = 1 << 1 ^ path[-1]
print(nxt)
head = 1
head <<= 1
print(head)
#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        #遍历字符串，放到对应的行，放满了则反向
        res = ["" for _ in range(numRows)]
        p = 0
        flag = 1
        for i in s:
            res[p] += i
            if p == numRows-1:
                flag = -1
            elif p == 0:
                flag = 1
            p += flag
        return "".join(res)

# @lc code=end
numRows = 1
s = "Ab" 
one = 2*numRows - 2
news = []
for i in range(0, len(s), one):
    news.append(s[i:i+one])

def change(pers):
    out = ["" for i in range(numRows)]
    for p in range(min(numRows, len(pers))):
        out[p] += pers[p]
    k = 2
    for p in range(numRows, len(pers)):
        out[p-k] += pers[p]
        k += 2
    return out
a = [change(i) for i in news]

a = [list(row) for row in zip(*a)]

a = "".join(["".join(i) for i in a])
print(a)
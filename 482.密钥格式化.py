#
# @lc app=leetcode.cn id=482 lang=python3
#
# [482] 密钥格式化
#

# @lc code=start
class Solution:
    def licenseKeyFormatting(self, s: str, K: int) -> str:
        s = s.replace("-","")
        s = s.upper()
        count = 0
        s = list(s)
        for i in range(len(s)-1,-1,-1):
            count += 1 
            if count == K and i != 0:
                count = 0
                s.insert(i,"-")
                i = i - 1

        s = "".join(s)
        return s
# @lc code=end

s = "---"

s = s.replace("-","")
s = s.upper()
k = 3
count = 0
s = list(s)
for i in range(len(s)-1,-1,-1):
    count += 1 
    if count == k:
        count = 0
        s.insert(i,"-")
        i = i - 1
try :
    if s[0] == "-":
        s.pop(0)
except:
    pass
s = "".join(s)
print(s)
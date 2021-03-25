#
# @lc app=leetcode.cn id=942 lang=python3
#
# [942] 增减字符串匹配
#

# @lc code=start
class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        i = 0
        j = len(S)
        res = []
        for k in S:
            if k == "I":
                res.append(i)
                i += 1
            else:
                res.append(j)
                j -= 1
        print(i,j)
        res.append(i)
        return res
            
# @lc code=end
S= "IDID"
shuzu = list(range(len(S)+1))
print(shuzu )
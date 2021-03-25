#
# @lc app=leetcode.cn id=1021 lang=python3
#
# [1021] 删除最外层的括号
#

# @lc code=start
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res = 0
        out_r = [0]
        for i,j in enumerate(S):
            if j == "(":
                res += 1
            else:
                res -= 1
            if res == 0:
                out_r.append(i)
                out_r.append(i+1)
        out_r.pop()
        print(out_r)
        s = ""
        for i in range(0,len(out_r),2):
            s += S[out_r[i]+1:out_r[i+1]]
        return s

        
# @lc code=end


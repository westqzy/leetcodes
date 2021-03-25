#
# @lc app=leetcode.cn id=1652 lang=python3
#
# [1652] 拆炸弹
#

# @lc code=start
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0]*len(code)
        codemotify = code*(abs(k)+1)
        for i in range(len(code)):
            if k > 0:
                code[i] = sum(codemotify[i+1:i+1+k])
            else:
                lent = abs(k)*len(code)
                code[i] = sum(codemotify[lent+k+i:lent+i])
        return code
# @lc code=end
code = [5,7,1,4]
codemotify = code*(3+1)
code[0] = sum(codemotify[0+1:0+4])
print(code)
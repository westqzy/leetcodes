#
# @lc app=leetcode.cn id=717 lang=python3
#
# [717] 1比特与2比特字符
#

# @lc code=start
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        p = 0
        while p < len(bits)-1:
            if bits[p] == 1:
                bits[p+1] = 1
                p+=1
            p+=1
        return bits[-1] == 0
# @lc code=end


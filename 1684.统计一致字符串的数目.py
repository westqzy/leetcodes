#
# @lc app=leetcode.cn id=1684 lang=python3
#
# [1684] 统计一致字符串的数目
#

# @lc code=start
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = 0
        reg = set(allowed)
        for i in words:
            for j in i:
                if j not in reg:
                    break
            else:
                res += 1
        return res

# @lc code=end

a = set("12324")
b = set("123")
print(b in a )
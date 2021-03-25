#
# @lc app=leetcode.cn id=1668 lang=python3
#
# [1668] 最大重复子字符串
#

# @lc code=start
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        k = 0
        while True:
            index = sequence.find(word*(k+1))
            if index == -1:
                return k
            else:
                k += 1

# @lc code=end

a = "aaa"
res = a.find("a")
print(res)
#
# @lc app=leetcode.cn id=844 lang=python3
#
# [844] 比较含退格的字符串
#

# @lc code=start
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def change(s1):
            i = 0
            while i <= len(s1)-1:
                if s1[i] == "#":
                    if i == 0:
                        s1 = s1[1:]
                        i -= 1
                    else:
                        s1 = s1[:i-1] + s1[i+1:]
                        i -= 2
                i += 1
            return s1
        return change(S) == change(T)
# @lc code=end

def change(s1):
    i = 0
    while i <= len(s1)-1:
        if s1[i] == "#":
            if i == 0:
                s1 = s1[1:]
                i -= 1
            else:
                s1 = s1[:i-1] + s1[i+1:]
                i -= 2
        i += 1
    return s1

print(change("a##c"))
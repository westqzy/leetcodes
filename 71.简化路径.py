#
# @lc app=leetcode.cn id=71 lang=python3
#
# [71] 简化路径
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        if len(path) == 1:
            return path
        s = path
        pre = s.split("/")
        if pre[-1] == "":
            pre.pop()
        res = []
        for i in pre[1:]:
            if i == "..":
                if res != []:
                    res.pop()
            elif i == "." or i == "":
                pass
            else:
                res.append("/"+i)
        print(res)
        if res == []:
            return "/"
        return "".join(res) 
# @lc code=end

s = "/a//b////c/d//././/.."

pre = s.split("/")
pre.pop()
print(pre)
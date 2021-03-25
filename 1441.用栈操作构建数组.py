#
# @lc app=leetcode.cn id=1441 lang=python3
#
# [1441] 用栈操作构建数组
#

# @lc code=start
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        for i in range(1, n+1):
            if i not in target:
                res.extend(["Push", "Pop"])
            else:
                res.append("Push")
                if i == target[-1]:
                    break
        return res
        

        
# @lc code=end


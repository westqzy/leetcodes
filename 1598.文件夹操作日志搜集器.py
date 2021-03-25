#
# @lc app=leetcode.cn id=1598 lang=python3
#
# [1598] 文件夹操作日志搜集器
#

# @lc code=start
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res = 0
        for i in logs:
            if i == "../":
                if res != 0:
                    res -= 1
            elif i =="./":
                pass
            else:
                res += 1
        return res
# @lc code=end


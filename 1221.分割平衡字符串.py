#
# @lc app=leetcode.cn id=1221 lang=python3
#
# [1221] 分割平衡字符串
#

# @lc code=start
import collections
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        hash1 = collections.defaultdict(int)
        res = 0
        for i in s:
            hash1[i] += 1
            if hash1["R"] == hash1["L"]:
                hash1.clear()
                res += 1
        return res
# @lc code=end


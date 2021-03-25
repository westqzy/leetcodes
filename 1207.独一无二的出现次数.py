#
# @lc app=leetcode.cn id=1207 lang=python3
#
# [1207] 独一无二的出现次数
#

# @lc code=start
import collections
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return len(set(collections.Counter(arr).values())) == len(collections.Counter(arr).values())
# @lc code=end


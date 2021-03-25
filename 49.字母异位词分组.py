#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash1 = collections.defaultdict(list)
        for i in strs:
            hash1["".join(sorted(i))].append(i)
        return list(hash1.values())

# @lc code=end
import collections
strs =["eat", "tea", "tan", "ate", "nat", "bat"]
hash1 = collections.defaultdict(list)
for i in strs:
    hash1[tuple(collections.Counter(sorted(i)))].append(i)
print(hash1.values())
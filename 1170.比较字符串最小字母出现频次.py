#
# @lc app=leetcode.cn id=1170 lang=python3
#
# [1170] 比较字符串最小字母出现频次
#

# @lc code=start
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s):
            return s.count(sorted(s)[0])
        queries = [f(s) for s in queries]
        words = [f(s) for s in words]
        count = 0
        res = []
        for i in queries:
            for j in words:
                if i < j:
                    count += 1
            res.append(count)
            count = 0
        return res
            
# @lc code=end
s = "ccnnbbd"
print(s.count(sorted(s)[0]))


#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
import itertools
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        dict1 = {1: '', 2: 'abc', 3: 'def', 4: 'ghi',
                 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
        return list(map(lambda ele: "".join(ele), itertools.product(*[dict1[int(i)] for i in digits])))


# @lc code=end
import itertools
digits= "23"
dict1 = {1: '', 2: 'abc', 3: 'def', 4: 'ghi',
                 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
ele for ele in itertools.product(*[dict1[int(i)] for i in digits])
print(list(a))
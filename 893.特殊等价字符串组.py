#
# @lc app=leetcode.cn id=893 lang=python3
#
# [893] 特殊等价字符串组
#

# @lc code=start
class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        def change(s:str):
            ji = {}
            ou = {}
            for i, j in enumerate(s):
                if i % 2 == 0:
                    ou[j] = ou.get(j, 0) + 1
                else:
                    ji[j] = ji.get(j, 0) + 1
            return [ji, ou]
        change = list(map(change, A))
        res = []
        for i in change:
            if i not in res:
                res.append(i)
        return len(res)


##这里考虑直接将奇数偶数排列后放入哈希表中更好

# @lc code=end

print(set([1,32,4,4]))
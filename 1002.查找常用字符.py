#
# @lc app=leetcode.cn id=1002 lang=python3
#
# [1002] 查找常用字符
#

# @lc code=start
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        #set运算  
        if len(A) == 1:
            return list(A[0])
        def gethash(s):
            res_hash = {}
            for i in s:
                res_hash[i] = res_hash.get(i, 0) + 1
            return res_hash
        dict_A = [gethash(i) for i in A]
        common = set("abcdefghijklmnopqrstuvwxyz")
        res = {}
        for i in range(len(dict_A)):
            common = dict_A[i].keys() & common
            res = {yuansu:min(res.get(yuansu, 101), dict_A[i][yuansu]) for yuansu in common}
        print(common)
        print(res)
        out = []
        for i, j in res.items():
            for _ in range(j):
                out.append(i)
        return out

        
        
# @lc code=end
a = {1:2, 2:3}
b = {1:2, 2:4}
print(a.keys() & b.keys())

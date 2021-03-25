#
# @lc app=leetcode.cn id=748 lang=python3
#
# [748] 最短补全词
#

# @lc code=start
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        licensePlate = licensePlate.lower()
        list1 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] 
        hash1 = {}
        for i in licensePlate:
            if i in list1:
                hash1[i] = hash1.get(i, 0) + 1
        hash2 = {}
        res = []
        for i in words:
            for j, k in hash1.items():
                #print(i.count(j), j , k)
                if i.count(j) < k:
                    break
            else:
                res.append(i)
        if res == []:
            return None
        #print(res)
        minlen = min(list(map(len, res)))
        for i in res:
            if len(i) == minlen:
                return i
# @lc code=end

#
# @lc app=leetcode.cn id=884 lang=python3
#
# [884] 两句话中的不常见单词
#

# @lc code=start
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        list_A = A.split(" ")
        list_B = B.split(" ")
        hashA = set()
        hashB = set()
        delete_list = set()
        for i in list_A:
            if i not in hashA:
                hashA.add(i)
            else:
                delete_list.add(i)


        for i in list_B:
            if i not in hashB:
                hashB.add(i)
            else:
                delete_list.add(i)
        for i in delete_list:
            if i in hashB:
                hashB.remove(i)
            if i in hashA:
                hashA.remove(i)  
        print(hashA)
        print(hashB)    
                
   
        res = (hashA | hashB) - (hashA & hashB)
        print(res)
        return list(res)
# @lc code=end

list_A = {1,3,4,5}
list_B = {1,3}
res = (list_A | list_B) - (list_A & list_B)
for i in res:
    print(i)
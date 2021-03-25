#
# @lc app=leetcode.cn id=1544 lang=python3
#
# [1544] 整理字符串
#

# @lc code=start 
import re
class Solution:
    def makeGood(self, s: str) -> str:
        res = s
        while True:
            matchlist = re.findall(r'[A-Z][a-z]', s)
            de = []
            for ele in matchlist:
                if ele[0].upper() == ele[1].upper():
                    de.append(ele)
            matchlist = re.findall(r'[a-z][A-Z]', s)        
            for ele in matchlist:
                if ele[0].upper() == ele[1].upper():
                    de.append(ele)
            if de == []:
                break
            for i in de:
                res = s.replace(i, "")
                s = res
        return res
# @lc code=end

import re
s = "jeSsEJ"
a = re.findall(r'[A-Z][a-z]|[a-z][A-Z]', s)
print(a)
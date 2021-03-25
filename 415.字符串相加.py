#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        jingwei = 0
        res = ""
        maxlen = max(len(num1),len(num2))
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i in range(maxlen):
            try:
                n1 = int(num1[i])
            except:
                n1 = 0
            try:
                n2 = int(num2[i])
            except:
                n2 = 0
            wei = n1 + n2 + jingwei
            jingwei = 0
            if wei >= 10:
                jingwei = 1
                wei = wei % 10
            res = res + str(wei)
        if jingwei == 1:
            res = res + "1"
        return res[::-1]
                    
# @lc code=end
def addStrings(num1: str, num2: str) -> str:
        jingwei = 0
        res = ""
        maxlen = max(len(num1),len(num2))
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i in range(maxlen):
            try:
                n1 = int(num1[i])
            except:
                n1 = 0
            try:
                n2 = int(num2[i])
            except:
                n2 = 0
            wei = n1 + n2 + jingwei
            print(wei)
            if wei >= 10:
                jingwei = 1
                wei = wei % 10
            res = res + str(wei)
        if jingwei == 1:
            res = res + "1"
        return res[::-1]
print(addStrings("1","9"))
#11.7
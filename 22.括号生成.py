#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
import collections
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        kuo_list = ["(", ")"]
        def traceback(index): 
            jiance1 = kuo.count("(")
            jiance2 = kuo.count(")")
            jiance = jiance1 -jiance2
            if jiance < 0 or jiance1 > n:
                pass
            elif index == 2*n:
                kuos.append("".join(kuo))
            else:
                for i in range(2):
                    kuo.append(kuo_list[i]) 
                    traceback(index+1)
                    kuo.pop()

        jiance = 0
        kuo = list()
        kuos = list()
        traceback(0)
        return kuos
            
# @lc code=end


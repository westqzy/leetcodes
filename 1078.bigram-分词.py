#
# @lc app=leetcode.cn id=1078 lang=python3
#
# [1078] Bigram 分词
#

# @lc code=start
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text_list = text.split(" ")
        res = []
        for i in range(len(text_list)-2):
            if text_list[i] == first and text_list[i+1] == second:
                res.append(text_list[i+2])
            
        return res

# @lc code=end


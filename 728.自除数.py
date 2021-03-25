#
# @lc app=leetcode.cn id=728 lang=python3
#
# [728] 自除数
#

# @lc code=start
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        list_n = list(range(left, right+1))
        list_n = list(map(str, list_n))
        res = []
        for i in list_n:
            for j in i:
                if j == "0":
                    break
                if int(i) % int(j) != 0:
                    break
            else:
                res.append(i)
        return res
# @lc code=end

list_n = list(range(1, 23))
print(list_n)
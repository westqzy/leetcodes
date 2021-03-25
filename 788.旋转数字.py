#
# @lc app=leetcode.cn id=788 lang=python3
#
# [788] 旋转数字
#

# @lc code=start
class Solution:
    def rotatedDigits(self, N: int) -> int:
        set_good = {'1':'1', '2':'5', '5':'2', '6':'9', '9':'6', '0':'0', '8':'8'}
        str_list = [str(i) for i in range(1, N+1)]
        res = 0
        for i in str_list:
            good = ""
            for j in i:
                if j in set_good.keys():
                    good += set_good[j]
            if good != i and len(good) == len(i):
                res += 1

        return res
        # ans = 0
        # # For each x in [1, N], check whether it's good
        # for x in range(1, N+1):
        #     S = str(x)
        #     # Each x has only rotateable digits, and one of them
        #     # rotates to a different digit
        #     ans += (all(d not in '347' for d in S)
        #             and any(d in '2569' for d in S))
        # return ans


# @lc code=end
S = "1225"
a = all(d not in '347' for d in S)
print(a)

#
# @lc app=leetcode.cn id=860 lang=python3
#
# [860] 柠檬水找零
#

# @lc code=start
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        lingqian = {}
        for i, j in enumerate(bills):
            lingqian[j] = lingqian.get(j, 0) + 1
            if j == 5:
                pass
            elif j == 10:
                lingqian[5] = lingqian.get(5, 0) - 1
                if lingqian[5] < 0:
                    return False
            elif j == 20:
                if lingqian.get(10, 0) - 1 < 0:
                    if lingqian.get(5, 0) - 3 < 0:
                        return False
                    else:
                        lingqian[5] = lingqian.get(5, 0) - 3
                else:
                    if lingqian.get(5, 0) - 1 < 0:
                        return False
                    else:
                        lingqian[5] = lingqian.get(5, 0) - 1
                        lingqian[10] = lingqian.get(10, 0) - 1
        return True
                

# @lc code=end


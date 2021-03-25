#
# @lc app=leetcode.cn id=1103 lang=python3
#
# [1103] 分糖果 II
#

# @lc code=start
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        should = 1 #第一个小孩应该分得1颗糖
        res = [0]*num_people
        boy = 0
        while candies >= should:
            res[boy] += should
            candies -= should
            should += 1
            boy += 1
            if boy == num_people:
                boy = 0
        res[boy] += candies
        return res
# @lc code=end


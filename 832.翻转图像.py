#
# @lc app=leetcode.cn id=832 lang=python3
#
# [832] 翻转图像
#

# @lc code=start
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        res = list(map(reversed, A))
        res = list(map(list, res))
        def change(list1):
            for i in range(len(list1)):
                if list1[i] == 0:
                    list1[i] = 1
                else:
                    list1[i] = 0
            return list1
        return [change(i) for i in res]

# @lc code=end
A = [[1,1,0],[1,0,1],[0,0,0]]
res = list(map(reversed, A))
res = list(map(list, res))

print(res)
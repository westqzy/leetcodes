#
# @lc app=leetcode.cn id=733 lang=python3
#
# [733] 图像渲染
#

# @lc code=start
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        seed = image[sr][sc]
        if image == [[]]:
            return image
        if seed == newColor:
            return image
        def search(sr, sc):
            if sr < 0 or sc < 0 or sr > len(image)-1 or sc > len(image[0])-1:
                return
            if image[sr][sc] == seed:
                image[sr][sc] = newColor
            else:
                return
            search(sr, sc-1)
            search(sr-1, sc)
            search(sr+1, sc)
            search(sr, sc+1)
        search(sr, sc)
       
        return image
# @lc code=end


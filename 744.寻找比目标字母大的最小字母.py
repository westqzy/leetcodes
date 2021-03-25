#
# @lc app=leetcode.cn id=744 lang=python3
#
# [744] 寻找比目标字母大的最小字母
#

# @lc code=start
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        listres = []
        for i in letters:
            if i > target:
                listres.append(i)
        if len(listres) == 0:
            return  min(letters)
        return min(listres)
# @lc code=end


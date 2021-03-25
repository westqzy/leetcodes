#
# @lc app=leetcode.cn id=520 lang=python3
#
# [520] 检测大写字母
#

# @lc code=start
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.lower() == word or word.upper() == word or \
            word[1:].lower() == word[1:] and word[0].upper() == word[0]:
            return True
      

# @lc code=end


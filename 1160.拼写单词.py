#
# @lc app=leetcode.cn id=1160 lang=python3
#
# [1160] 拼写单词
#

# @lc code=start
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        def change(s):
            hash1 = {}
            for i in s:
                hash1[i] = hash1.get(i, 0)+1
            return hash1
        char_list = change(chars)
        know_list = [change(s) for s in words]
        print(know_list)
        print(char_list)
        res = 0
        for q, d in enumerate(know_list):
            for i in d.keys():
                if i not in char_list.keys():
                    break
                elif d[i] > char_list[i]:
                    break
            else:
                res += len(words[q])
        return res

# @lc code=end

print(set("a") in set("atach"))
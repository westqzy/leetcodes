#
# @lc app=leetcode.cn id=720 lang=python3
#
# [720] 词典中最长的单词
#

# @lc code=start
class Solution:
    def longestWord(self, words: List[str]) -> str:
        res = ""
        words_set = set(words)
        for i in range(len(words)):
            j = 0
            while j < len(words[i]):
                if words[i][0:j + 1] not in words_set:
                    break
                else:
                    j+=1
            if j == len(words[i]):
                if len(words[i]) > len(res):
                    res = words[i]
                if len(words[i]) == len(res):
                    res = min(res, words[i])
        return res





# @lc code=end
words = ["yo","ew","fc","zrc","yodn","fcm","qm","qmo","fcmz","z","ewq","yod","ewqz","y"]
words.sort()
print(words)
res = {}
p = -1
for i in words:
    if len(i) != 1:
        if len(i) > len(res[p]) and res[p] in i:
            res[p] = i
    else:
        p += 1
        res[p] = i
print(res)

for i in range(5):
    break
else:
    print("bee")    

print(max("apple", "applf"))      
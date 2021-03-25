#
# @lc app=leetcode.cn id=500 lang=python3
#
# [500] 键盘行
#

# @lc code=start
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        hash1 = {'q','w','e','r','t','y','u','i','o','p'}
        hash2 = {'a','s','d','f','g','h','j','k','l'}
        hash3 = {'z','x','c','v','b','n','m'}
        count = -1
        hashlist = [hash1,hash2,hash3]
        wordscopy = words.copy()
        for i in words:
            if i:
                if i[0].lower() in hash1:
                    count = 0
                elif i[0].lower() in hash2:
                    count = 1
                else:
                    count = 2
            for j in i.lower():
                if j not in hashlist[count]:
                    wordscopy.pop(wordscopy.index(i))
                    break
        return wordscopy
# @lc code=end
words = ["abdfs","cccd","a","qwwewm"]
hash1 = {'q','w','e','r','t','y','u','i','o','p'}
hash2 = {'a','s','d','f','g','h','j','k','l'}
hash3 = {'z','x','c','v','b','n','m'}
count = -1
hashlist = [hash1,hash2,hash3]
wordscopy = words.copy()

for i in words:
    if i:
        if i[0].lower() in hash1:
            count = 0
        elif i[0].lower() in hash2:
            count = 1
        else:
            count = 2
    for j in i.lower():
        if j not in hashlist[count]:
            print(words.index(i))
            wordscopy.pop(wordscopy.index(i))
            break

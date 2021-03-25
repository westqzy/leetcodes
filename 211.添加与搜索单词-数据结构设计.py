#
# @lc app=leetcode.cn id=211 lang=python3
#
# [211] 添加与搜索单词 - 数据结构设计
#

# @lc code=start
import collections
class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = collections.defaultdict(list)

    def addWord(self, word: str) -> None:
        self.list[len(word)].append(word)

            
    def search(self, word: str) -> bool:
        def bijiao(w):
            for i,j in enumerate(word):
                if j == ".":
                    pass
                else:
                    if j != w[i]:
                        return False
            else:
                return True
        l = len(word)
        for w in self.list[l]:
            if bijiao(w) == True:
                return True
        return False
            

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end
word = "bad"
res = ""
def backtrace(start,res):
        if start == len(word):
            return
        ress.append(res[:])
        for i in range(start, len(word)):
            res += word[i]
            backtrace(i+1, res)
            res = res[:-1]
ress = []

backtrace(0,res)
print(ress)

word = "bad"
def bijiao(w):
    for i,j in enumerate(w):
        print(i, j)
        if j == ".":
            pass
        else:
            if j != word[i]:
                return False
    else:
        return True
print(bijiao("b.."))
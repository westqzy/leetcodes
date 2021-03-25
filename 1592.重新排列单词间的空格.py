#
# @lc app=leetcode.cn id=1592 lang=python3
#
# [1592] 重新排列单词间的空格
#

# @lc code=start
class Solution:
    def reorderSpaces(self, text: str) -> str:
        #主要得判断单词的个数
        num_space = 0
        word = ""
        words_list = []
        for i in text:
            if i == " ":
                num_space += 1
                if word != "":
                    words_list.append(word)
                    word = ""
            else:
                word += i
        if word != "":
            words_list.append(word)
            word = ""
        num_words = len(words_list)
        if num_words != 1:#只有一个单词。避免除数为0
            per_space_num = num_space // (num_words-1)
            last_space_num = num_space % (num_words-1)
        else:
            last_space_num = num_space  
            per_space_num = 0
        per_space = " " * per_space_num
        last_space = " " * last_space_num
        res = ""
        for i in range(num_words):
            if i != num_words - 1:
                res += words_list[i] + per_space
            else:
                res += words_list[i] + last_space
        return res

            
# @lc code=end
text = "  this   is  a sentence "
li = text.strip().split()
print(li)


#强啊啊
class Solution:
    def reorderSpaces(self, text: str) -> str:
        c = text.count(" ")
        li = text.strip().split()
        if len(li) == 1:
            return li[0] + " " * c
        s, s1 = divmod(c, len(li) - 1) 
        return (" " * s).join(li)  + " " * s1


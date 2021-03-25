#
# @lc app=leetcode.cn id=937 lang=python3
#
# [937] 重新排列日志文件
#

# @lc code=start
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def change(s:str):
            head = s.split(" ")[0]
            head_len = len(head)
            context = s[head_len+1:]
            dict_out = (context ,head)
            return dict_out

        logs_context = [change(i) for i in logs]
        num_list = []
        word_list = []
        for i, j in logs_context:
            if i[0].isalpha():
                word_list.append((i,j))
            else:
                num_list.append((i,j))


        word_list.sort()
        word_list.extend(num_list)
        
        res = []
        for i,j in word_list:
            res.append(j+" "+i)        
        return res
# @lc code=end
# class Solution(object):
#     def reorderLogFiles(self, logs):
#         def f(log):
#             id_, rest = log.split(" ", 1)
#             return (0, rest, id_) if rest[0].isalpha() else (1,)

#         return sorted(logs, key = f)

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/reorder-data-in-log-files/solution/zhong-xin-pai-lie-ri-zhi-wen-jian-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
#
# @lc app=leetcode.cn id=806 lang=python3
#
# [806] 写字符串需要的行数
#

# @lc code=start
class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        s_list = list("abcdefghijklmnopqrstuvwxyz")
        hash1 = dict(zip(s_list, widths))
        count = 0
        hang = 1
        for i in s:
            #计算一行的元素
            count += hash1[i]
            if count > 100:
                count = hash1[i]
                hang += 1
        return [hang, count]
# @lc code=end


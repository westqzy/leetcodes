#
# @lc app=leetcode.cn id=599 lang=python3
#
# [599] 两个列表的最小索引总和
#

# @lc code=start
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hash1 = {}
        for i in list1:
            if i in list2:
                index = list1.index(i) + list2.index(i)
                hash1[index] = hash1.get(index,[])
                hash1[index].append(i)
        return hash1[min(hash1.keys())]
# @lc code=end
a={1:["qqq",2,3]}
a[2] = a.get(2,[])
print(a[2] )

#
# @lc app=leetcode.cn id=1200 lang=python3
#
# [1200] 最小绝对差
#

# @lc code=start
import collections
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        ###先排序
        # arr.sort()
        # hash = {}
        # for i in range(len(arr)-1):
        #     hash[arr[i+1]-arr[i]] = hash.get(arr[i+1]-arr[i], []) + [[arr[i], arr[i+1]]]
        # return hash[min(hash.keys())]
        arr.sort()
        hash1 = collections.defaultdict(list)
        for i in range(len(arr)-1):
            hash1[arr[i+1]-arr[i]].append([arr[i], arr[i+1]])
        return hash1[min(hash1.keys())]


        
# @lc code=end
a = {1:[[1,2]]}
a[1].append([1,23])
print(a.get(1, [])+[12,3])
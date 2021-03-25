#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # def merge(n1,n2):
        #     res = []
        #     n1l = len(n1)
        #     n2l = len(n2)
        #     p1 = 0
        #     p2 = 0
        #     while p1 < n1l and p2 < n2l:
        #         if n1[p1] > n2[p2]:
        #             res.append(n1[p1])
        #             p1 += 1
        #         else:
        #             res.append(n2[p2])
        #             p2 += 1
        #     if p2 >= n2l:
        #         res.extend(n1[p1:])
        #     elif p1 >= n1l:
        #         res.extend(n2[p2:])
        #     return res
        # def fenzhi(nums):
        #     if len(nums) <= 1:
        #         return nums
        #     l = len(nums)
        #     mid = l//2
        #     left = nums[:mid]
        #     right = nums[mid:]
        #     return merge(fenzhi(left), fenzhi(right))
        # return fenzhi(nums)[k-1]
        return sorted(nums)[-k]
# @lc code=end

def merge(n1,n2):
            res = []
            n1l = len(n1)
            n2l = len(n2)
            p1 = 0
            p2 = 0
            while p1 < n1l and p2 < n2l:
                if n1[p1] > n2[p2]:
                    res.append(n1[p1])
                    p1 += 1
                else:
                    res.append(n2[p2])
                    p2 += 1
            if n1l > n2l:
                res.extend(n1[n2l:])
            else:
                res.extend(n2[n1l:])
            return res
print(merge([3,2,1],[5,3,1,0,-3]))
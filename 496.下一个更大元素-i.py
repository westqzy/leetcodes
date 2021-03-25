#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # res = []
        # for i in range(len(nums1)):
        #     for j in range(nums2.index(nums1[i]),len(nums2)):
        #         if nums2[j] > nums1[i]:
        #             res.append(nums2[j])
        #             break
        #     else:
        #         res.append(-1)
        # return res
        #单调栈
        hash1 = {}
        stack = []
        for i in nums2:
            while stack and stack[-1] < i:
                hash1[stack.pop()] = i
            stack.append(i)
        res = [hash1.get(i,-1) for i in nums1]
        return res

# @lc code=end

a = [1,2,3,34]
a.index(1)
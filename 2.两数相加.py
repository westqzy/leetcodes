#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
# @lc code=start 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        jing = 0
        head = res = ListNode(None)
        while l1 or l2:
            p1 = l1.val if l1 else 0
            p2 = l2.val if l2 else 0
            if p1 + p2 + jing >= 10:
                a = p1 +p2 + jing - 10
                jing = 1
            else:
                a = p1 +p2 + jing
                jing = 0
            res.next = ListNode(a)
            res = res.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if jing == 1:
            res.next = ListNode(1)  

        return head.next
# @lc code=end

jing = int((5+8) >= 10)
print(jing)
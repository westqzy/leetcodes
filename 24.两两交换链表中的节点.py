#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        pre = ListNode(0, head)
        tem  = pre
        while head and head.next != None:
            mid = head.next
            head.next = head.next.next
            mid.next = head
            pre.next = mid
            head = head.next
            pre = pre.next.next
        return tem.next
# @lc code=end


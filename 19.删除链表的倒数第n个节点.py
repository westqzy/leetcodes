#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # if head == None:
        #     return head
        # pre = ListNode(None)
        # pre.next = head
        # num = 0
        # maxl = float("inf")
        # while head:
        #     num += 1
        #     if head.next == None:
        #         head = pre
        #         maxl = num + num - n
        #     if num == maxl:
        #         head.next = head.next.next
        #         break
        #     head = head.next
        # return pre.next
        
        # 快慢指针
        pre = ListNode(0, head)
        second = pre
        first = head
        for i in range(n):
            first = first.next
        
        while first:
            first = first.next
            second = second.next
        
        second.next = second.next.next
        return pre.next
# @lc code=end


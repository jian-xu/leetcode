# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        stack = list()
        while head:
            stack.append(head)
            head = head.next
        cur = init = ListNode(0)
        while stack:
            tmp = stack.pop()
            init.next = tmp
            init = init.next
        init.next = None
        return cur.next
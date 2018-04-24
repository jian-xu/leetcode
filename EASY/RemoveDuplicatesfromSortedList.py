# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (not head):
            return None
        first = tmp = ListNode(0)
        tmp.next = head
        head = head.next
        tmp = tmp.next
        while(head):
            if (head.val == tmp.val):
                head = head.next
            else:
                tmp.next = head
                head = head.next
                tmp = tmp.next
        tmp.next = None
        return first.next
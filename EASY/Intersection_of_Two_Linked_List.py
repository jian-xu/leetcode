# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headB is None or headA is None:
            return None

        pa = headA
        pb = headB

        while pa is not pb:

            pa = pa.next if pa else headB
            pb = pb.next if pb else headA

        return pa

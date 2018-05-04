# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        #if p == q:
        #    return p
        while(root):
            if q.val == root.val:
                return q
            if p.val == root.val:
                return p
            if (p.val < root.val and q.val > root.val) or (p.val > root.val and q.val < root.val):
                return root
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack, res = [], []
        while(True):
            while(root):
                stack.append(root)
                root = root.left
            if len(res) == k:
                return res[k-1]
            node = stack.pop()
            res.append(node.val)
            root = node.right

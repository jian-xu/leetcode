# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack, result = [], []
        while(True):
            while(root):
                result.append(root.val)
                stack.append(root.right)
                root = root.left
            if not stack:
                return result
            root = stack.pop()
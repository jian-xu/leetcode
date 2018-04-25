# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        """
        #preorder traversal(right tree first), then reverse the result
        stack, result = [], []
        while(True):
            while(root):
                result.append(root.val)
                stack.append(root.left)
                root = root.right
            if not stack:
                return result[::-1]
            root = stack.pop()
        """
        result, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    result.append(node.val)
                else:
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
        return result

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res, level = [], [root]
        while level:
            res.append(level[-1].val)
            tmp = []
            for node in level:
                tmp.extend([node.left, node.right])
            level = [leaf for leaf in tmp if leaf]
        return res
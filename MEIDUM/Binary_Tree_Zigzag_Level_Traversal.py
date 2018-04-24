# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res, level = [], [root]
        beacon = 1
        while level:
            if beacon == 1:
                res.append([node.val for node in level])
                beacon = 0
            else:
                res.append([node.val for node in reversed(level)])
                beacon = 1
            tmp = []
            for node in level:
                tmp.extend([node.left, node.right])
            level = [leaf for leaf in tmp if leaf]
        return res
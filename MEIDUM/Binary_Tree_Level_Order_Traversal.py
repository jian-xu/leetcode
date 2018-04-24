# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        """
        res = []
        queue = []
        if root == None:
            return res
        queue.append(root)
        queue.append('Finish')
        while (len(queue) >= 2):
            level = []
            while (queue[0] != 'Finish'):
                node = queue.pop(0)
                if node != None:
                    level.append(node.val)
                    queue.extend([node.left, node.right])
                    #queue.append(node.left)
                    #queue.append(node.right)
            if (level != []):
                res.append(level)
            queue.append('Finish')
            queue.pop(0)
        return res
        """
        if not root:
            return []
        res, level = [], [root]
        while level:
            res.append([node.val for node in level])
            tmp = []
            for node in level:
                tmp.extend([node.left, node.right])
            level = [leaf for leaf in tmp if leaf]
        return res

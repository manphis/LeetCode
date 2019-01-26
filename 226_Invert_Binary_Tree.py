'''Invert a binary tree.'''

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return
        self.invertTree(root.left)
        self.invertTree(root.right)
        tmp = root.left
        root.left = root.right
        root.right = tmp
        
        return root
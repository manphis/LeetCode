'''
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        box = []
        if root == None:
            return box
        path = str(root.val)
        self.extend(box, path, root)
        return box
    
    def extend(self, box, path, node):
        if node.left == None and node.right == None:
            box.append(path)
            return
        
        if node.left != None:
            p = path + '->' + str(node.left.val)
            self.extend(box, p, node.left)
        if node.right != None:
            p = path + '->' + str(node.right.val)
            self.extend(box, p, node.right)
        
        return
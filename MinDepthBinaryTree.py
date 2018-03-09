"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        if root.left == None and root.right == None: #we have reached leaf node
            return 1
        
        if root.left == None: #only right subtree is present
            return 1 + self.minDepth(root.right)
        
        if root.right == None: #only left subtree is present
            return 1 + self.minDepth(root.left)  
        
        
        # add 1 to final result since depth of root-only tree will be 1
        return 1 + min( self.minDepth(root.left), self.minDepth(root.right) )
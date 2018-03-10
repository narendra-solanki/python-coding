"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        """
        First append root node to the nodes
        while nodes is not empty
            pop the first node from list
            add value of node in tmpList
            if there are left and right child of the node, then append childs to nodes
            continue till all elements at this level are traversed
        
        """

        final = [] #this list will contain final list containing one list for each level
        queue = []
        if root:
            queue.append(root) #append root element        
        while queue:            
            qSize = len(queue) #number of nodes at this level
            level = [] #list to store elements at this level
            for elem in range(qSize):
                node = queue.pop(0)                             
                level.append(node.val)
                #append any left or right childs to the nodes, these will be nodes for next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            final.append(level)
        return final
            
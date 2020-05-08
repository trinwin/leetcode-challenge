# ----------------------------------------------------------------------
# Name:        Cousins in Binary Tree
# Author(s):   Trinity Nguyen
# ----------------------------------------------------------------------

"""
    In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

    Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

    We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

    Return true if and only if the nodes corresponding to the values x and y are cousins.

    Example 1:
    Input: root = [1,2,3,4], x = 4, y = 3
    Output: false


    Example 2:
    Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
    Output: true

    Example 3:
    Input: root = [1,2,3,null,4], x = 2, y = 3
    Output: false

    Note:

    The number of nodes in the tree will be between 2 and 100.
    Each node has a unique integer value from 1 to 100.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def findParentNDepth(self, root, p, depth, target):
        if root:
            # based case
            if root.val == target:
                return (p, depth)

            # Return parent value and depth if Node is present in left subtree
            parent_depth = self.findParentNDepth(root.left, root.val, depth+1, target)
            if parent_depth:
                return parent_depth

            # Search in right subtree
            return self.findParentNDepth(root.right, root.val, depth+1, target)

    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        x_par, x_depth = self.findParentNDepth(root, -1, 0, x)
        y_par, y_depth = self.findParentNDepth(root, -1, 0, y)

        if x_par != y_par and x_depth == y_depth:
            return True

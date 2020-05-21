# ----------------------------------------------------------------------
# Name:        Kth Smallest Element in a BST
# Author(s):   Trinity Nguyen
# ----------------------------------------------------------------------

"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

 

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest 
frequently? How would you optimize the kthSmallest routine?

 
Constraints:
    - The number of elements of the BST is between 1 to 10^4.
    - You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Hint:
    1. Try to utilize the property of a BST.
    2. Try in-order traversal. 
    3. What if you could modify the BST node's structure?
    4. The optimal runtime complexity is O(height of BST).
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        res = []

        def inOrder(root):
            if root:
                inOrder(root.left)
                res.append(root.val)
                inOrder(root.right)

        inOrder(root)
        return res[k - 1]

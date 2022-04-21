# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # Approach 1 : middle order the tree;time complexity  O(n) ,space O(n)
        # if it is the ascent list it is a binary search tree
        # Approach 2 : recursive O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Approach 1 : recursive and add the level until the left and right node is null
        # maintain a variable maxlevel to store the maximum level
        # time complexity :O(n)
        # space complexity :O(log n) to o(n)
        
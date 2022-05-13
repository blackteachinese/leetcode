# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # Approach 1 : BFS iterative  time O(n) space O(n)
        # BFS Usage scenario： 1 the shortest path  2 layer by layer traveral
        # the shortest path topic:  542_01-matrix, 994_rotting-oranges
        # layer by layer traversal: 103_zigzag-level-order-traversal,199_binary-tree-right-side-view,515_
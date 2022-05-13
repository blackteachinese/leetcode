# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Approach 1: iterative two times,find p and q
        # time:2*O(n) space:O(n)
        # dfs and store all the father node of tow target node into two list
        # compare two list
        # ！！！ 要李远二叉搜索树特性优化search
        #  search p and q ,  
        # if node.val == p.val bingo 
        # elif node.val > p.val then search p from node.left 
        # else search p from node.right
        # Approach 2: iterative one times,
        # use binary search tree
        # if node.val > p.val and node.val > p.val: search node.left
        # elif node.val < p.val and node.val < p.val: search node.right
        # else  node if the result or node if one of p or q
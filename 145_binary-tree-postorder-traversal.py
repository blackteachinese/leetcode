# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 后续遍历
        def dfs(root,list):
            if not root: return
            dfs(root.left,list)
            dfs(root.right,list)
            list.append(root.val)
        list=[]
        dfs(root,list)
        return list
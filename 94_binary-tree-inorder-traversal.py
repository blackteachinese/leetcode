# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List

class Solution1:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # recursion time:O(n)
        res=[]
        def dfs(node:TreeNode,res:List):
            if node == None:
                return
            dfs(node.left,res)
            res.append(node.val)
            dfs(node.right,res)
        dfs(root,res)
        return res

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # iteration time:O(n)
        stack,res = [],[]
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right # 错误点
        return res



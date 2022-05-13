# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None: return root
        queue = [root]
        while len(queue) > 0:
            node=queue.pop(0)
            if node == None:
                continue
            # 左右节点交换即可
            node.left,node.right = node.right,node.left
            queue.append(node.right)
            queue.append(node.left)
        return root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:            
        # interation time O(n)
        # 返回多维数组，要用两层循环
        # 依次遍历每层，所以外层是queue；每层的所有子节点遍历要逆序，所以内层是stack
        res=[]
        queue=[[(root,False)]]
        while len(queue) > 0: # 外层是queue
            currentStack=queue.pop(0)
            level=[]
            nextStack=[]
            while len(currentStack) > 0: # 内层是stack
                root,fromLeft = currentStack.pop()
                if root == None:
                    continue
                level.append(root.val)
                nextStack.append((root.right if fromLeft else root.left,not fromLeft))
                nextStack.append((root.left if fromLeft else root.right,not fromLeft))
            if len(nextStack) == 0:
                break
            queue.append(nextStack)
            res.append(level)
        return res
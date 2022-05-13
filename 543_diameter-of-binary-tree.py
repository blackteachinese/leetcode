# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxPath = 0

    def diameterOfBinaryTree1(self, root: TreeNode) -> int:
        #思路：第一次自己思考
        # 经过某一个节点的最大直径长度，等于它的左子树深度+右子树深度+1
        # 计算出经过每一个点节点的最大直径最大，经过比较得到直径最长的路径
        # 树的深度=max(depth(left),depth(right))
        # maxPath=0
        def depth(root:TreeNode)->int:
            if not root:
                return 0
            left = depth(root.left)
            right = depth(root.right)
            # 简化最大值逻辑
            self.maxPath(self.maxPath,left+right)
            return max(left,right) + 1
        depth(root)
        return self.maxPath
    
class Solution:
    def __init__(self):
        self.maxNodes = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # 思路：重新理解提议优化逻辑
        # 忽略点1：直径长度是边的数量，所以直径长度=节点数-1
        # 经过某一个节点的最多节点数=它的左子树深度+右子树深度+1
        # 深度遍历每一个节点，并计算经过该一个节点的最多节点数
        # 比较，并记录遍历过的最多节点数
        # 以root为根的子树深度=max(depth(root.left),depth(root.right))+1
        def depth(root:TreeNode)->int:
            if not root:
                return 0
            left = depth(root.left)
            right = depth(root.right)
            # 简化最大值逻辑
            self.maxNodes = max(self.maxNodes,left+right+1) # 注意1：经过某一个节点的最多节点数=它的左子树深度+右子树深度+1
            return max(left,right) + 1 # 注意2：以root为根的子树深度=max(depth(root.left),depth(root.right))+1
        depth(root)
        return self.maxNodes - 1 # 注意2：直径长度=节点数-1
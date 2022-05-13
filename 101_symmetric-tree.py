# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # 思路：自己想
        # 判断轴对称的逻辑，根节点的左子树和右子树左右相反
        # 遍历root的左子树和右子树，子树的每一个left 都等于 right就是抽对称
        # 递归调用
        # 时间复杂O(n),n是节点数
        # 空间复杂度，递归的空间复杂度，和使用的栈的深度有关系，最差的情况是当二叉树是链表，深度最多为n,所以复杂度是O（n）
        return self.dfs(root.left,root.right)
        
    def dfs(self,node1,node2)->bool:
        if not node1 and not node2:
            return True
        elif not node1 or not node2:
            return False
        elif node1.val != node2.val:
            return False
        else:
            return self.dfs(node1.left,node2.right) and self.dfs(node1.right,node2.left)

class Solution2:
    def isSymmetric(self, root: TreeNode) -> bool:
        # 迭代法，常用用队列将递归改造成迭代
        # 每次提取两个结点，要求值相等
        # 将两个结点的子节点，按相反的顺序插入队列，确保连续两个结点是镜像对称的
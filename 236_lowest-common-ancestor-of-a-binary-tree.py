# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from contextlib import nullcontext


class Solution1:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not p or not q or not root:
            return None
        pList,qList = [],[]
        self.helper(root,p,pList)
        self.helper(root,q,qList)
        last = None
        while pList and qList:
            a = pList.pop()
            b = qList.pop()
            if a.val == b.val:
                last = a
                continue
            else:
                break
        return last


    def helper(self,root,target,result) -> bool:
        if not root:
            return False
        # 递归左子树，如果找到目标节点，直接返回True,其他分支不走
        isTarget = self.helper(root.left,target,result)
        if isTarget:
            result.append(root)
            return True
        # 左子树找不到，递归右子树，如果找到目标节点，直接返回True,其他分支不走
        isTarget = self.helper(root.right,target,result)
        if isTarget:
            result.append(root)
            return True
        # 左右子树都找不到，判断当前是否目标节点，如果是返回True,否则返回false
        if root.val == target.val:
            result.append(root)
            return True
        else:
            return False
        
class Solution2:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return None
        # 自己想的
        # 思路：查找两个节点的公共祖先，可以转化为查找两个节点是否都在子树里
        # 从根节点的左右子树开始遍历，递归查找是否两个节点都在子树里。如果不存在则跳出递归；如果存在，则记录子树深度，然后继续判断左右子树。

class Solution3:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return None
        # 题解思路：存储每个节点的父节点
        # 一个节点会多个父节点，如果可以获取p和q的所有父节点，只要反向遍历判断哪个父节点是最早的公共父节点即可
        # 因此，首现要具备反向遍历父节点的能力，可以通过哈希表来实现。从root开始遍历所有节点，将所有父子关系存储在哈希表中，key是子节点，val是父节点。
        # 然后只要反方向遍历q的父节点，判断其是否也是p的父节点，判断是否存在可以用集合set存储p的所有父节点。

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #题解思路：递归
        # 先定义出判断最近公共节点的逻辑
        # 定义：如果root左子树是p或q的祖先，root右子树是p或q的祖先，那么root就是p或q的公共祖先
        # 根据定义，只需要判断左右子树是否p或q其中一个节点的祖先，不需要是否判断公共祖先，逻辑就可以大大简化
        # 推导出最小子问题为，“判断这个子树是否p或q的父节点”
        # 时间复杂度O(n),n是节点数量，递归过程每个节点都会遍历一次；
        # 空间复杂度O(2n)递归过程每个节点都会有left和right两个变量
        # Fix空间复杂度:递归调用的栈深度取决于二叉树的高度，二叉树最坏情况下为一条链，此时高度为 NN，因此空间复杂度为 O(N)O(N)。
        # 边界情况：当root = null，不符合子问题，返回null
        if not root : return None
        # 当root等于q或p,满足最小子问题“判断这个子树是否p或q的父节点”，返回root
        if root == p or root == q :return root  # 这是递归到最底部的判断逻辑
        # 用递归实现逐层遍历子树逻辑，递归的结果是“判断这个子树是否p或q的父节点”
        # 递归的思想：因为是递归，使用函数后可认为左右子树已经算出结果
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        # 当root.left和root.right都是p或q的祖先,因为左右子树都是，只可能是一边一个，root肯定就是公共祖先
        if left and right :
             return root
        # 如果root.left不是p或q的祖先，但root.right是p或q的祖先，说明root左子树一定不是p或q的公共祖先，root.right满足子问题，可能是p或q的公共祖先，返回root.right
        elif  not left and right : 
            return right
        elif not right and left : 
            return left
        # 当root.left和root.right都不是p或q的祖先，说明root里不存在p和q的公共祖先，直接返回Null
        # 只剩下 not left and not right 
        else:
            return None

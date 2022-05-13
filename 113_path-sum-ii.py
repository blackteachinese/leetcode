# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from unittest import result
import numpy as np
import copy

class Solution1:
    target=0
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # 思路：root到每一个叶子节点都只有一种组合，因此通过遍历整个二叉树，可以找到所有组合
        # 再判断每个组合的节点值之和是否等于目标即可
        # 遍历方法可用深度遍历、广度遍历，深度遍历用递归，广度遍历用迭代。
        # 时间复杂度：O(n^2),遍历所有节点是O(n),判断路径综合要遍历组合的元素，最坏的情况也是O(n)
        # 边界
        # 初始化
        self.target = targetSum
        results=[]
        # 核心
        self.dfs(root,[],results)
        return results

    def dfs(self,node:TreeNode,paths:List,results):
        visited = copy.deepcopy(paths)
        # 结束条件
        if not node:
            return
        visited.append(node.val)
        if not node.left and not node.right:
            # 判断是否有效结果
            if np.sum(visited) == self.target:
                results.append(visited)
            return
        self.dfs(node.left,visited,results)
        self.dfs(node.right,visited,results)
        # 清除上下文
class Solution2:
    target=0
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # 代码简化
        self.target = targetSum
        results=[]
        # 内嵌函数
        def dfs(node:TreeNode,paths:List):
            visited = copy.deepcopy(paths)
            # 结束条件
            if not node:
                return
            visited.append(node.val)
            if not node.left and not node.right:
                # 判断是否有效结果
                if np.sum(visited) == self.target:
                    results.append(visited)
                return
            dfs(node.left,visited)
            dfs(node.right,visited)
            # 清除上下文
        # 核心
        dfs(root,[])
        return results

class Solution3:
    target=0
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # 不用深拷贝，改用递归清除上下文
        self.target = targetSum
        results=[]
        # 内嵌函数
        def dfs(node:TreeNode,visited:List):
            # 结束条件
            if not node:
                return
            visited.append(node.val)
            if not node.left and not node.right:
                # 判断是否有效结果
                if np.sum(visited) == self.target:
                    #!!!注意，这里至少需要深拷贝第一层，使用[:]切片，可以浅拷贝整个列表。同样的，只对第一层实现深拷贝
                    results.append(visited[:]) 
                # return 
            dfs(node.left,visited)
            dfs(node.right,visited)
            # 递归调用后再清除上下文
            # 注意：上面遍历到叶子节点时不能return，否则清除上下文会运行不到。
            visited.pop()
        # 核心
        dfs(root,[])
        return results


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # 优化：不计算数组之和，用target减去节点数，判断是否为0
        results=[]
        visited=[]
        # 内嵌函数
        def dfs(node:TreeNode,targetSum:int):
            # 结束条件
            if not node:
                # 这里没有运行visited.append,不需要清除上下文，可以return
                return
            visited.append(node.val)
            targetSum -= node.val
            if not node.left and not node.right:
                # 判断是否有效结果
                if targetSum == 0:
                    #!!!注意，这里至少需要深拷贝第一层，使用[:]切片，可以浅拷贝整个列表。同样的，只对第一层实现深拷贝
                    results.append(visited[:]) 
                # 这里已经运行visited.append,需要清除上下文，不可以return
            dfs(node.left,targetSum)
            dfs(node.right,targetSum)
            # 递归调用后再清除上下文
            # 注意：上面遍历到叶子节点时不能return，否则清除上下文会运行不到。
            visited.pop()
        # 核心
        dfs(root,targetSum)
        return results
    
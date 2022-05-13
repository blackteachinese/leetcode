"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
from typing import List


class Solution1:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        # 二叉搜索树中序遍历是递增序列
        # 方法1：中序遍历后放到数组里，遍历数组构建循环双向链表
        # time:O(n) space o(n)
        # 边界
        if root == None or root.right == None:return root
        # logic
        def dfs(root,res:List):
            if not root:
                return
            dfs(root.left,res)
            res.append(root)
            dfs(root.right,res)
        list = []
        dfs(root,list)
        # print(list)
        i = 0
        while i + 1 < len(list):
            left,right=list[i],list[i+1]
            left.right = right
            right.left = left
            i+=1
        first = list[0]
        last = list[-1]
        last.right = first
        first.left = last
        return list[0]


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        # 二叉搜索树中序遍历是递增序列
        # 方法2：去掉数组，用一个pre指针保存上一个节点
        # time:O(n) space o(n)
        # 边界
        if root == None :return root
        # logic
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            if self.pre:
                self.pre.right,root.left = root,self.pre
            else: # 最小值， 是头结点
                self.head = root 
            self.pre = root #错误点：为什么是root不是root.right?因为递归过程，是左中有一个一个节点遍历，root就可以
            dfs(root.right)
        list = []
        self.pre = None
        dfs(root)
        self.head.left,self.pre.right = self.pre,self.head
        return self.head
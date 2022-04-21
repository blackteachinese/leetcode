# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution1:
    def isCompleteTree(self, root: TreeNode) -> bool:
        # 思路：自己想的
        # 逐层遍历，每层从左到右遍历
        # 当节点为空，剩余队列也为空时，符合完全二叉树，否则不符合
        # 使用一个队列来存储需要遍历的节点
        return self.walk([root],False)

    def walk(self, queue: List,hasNone) ->bool:
        nextQueue = []
        while len(queue) > 0:
            node = queue.pop(0)
            if node.left and hasNone == True:
                return False
            if node.left:
        
                nextQueue.append(node.left)  
            else:
                hasNone = True  
            if node.right and hasNone == True:
                return False
            if node.right:
                print(node.right.val)
                nextQueue.append(node.right)  
            else:
                hasNone = True 
        if len(nextQueue) > 0:
            return self.walk(nextQueue,hasNone)
        else:
            return True

class Solution2:
    def isCompleteTree(self, root: TreeNode) -> bool:
        #思路：题解
        # 用到一个表示深度和位置的规律：用 1 表示根节点，对于任意一个节点 v，它的左孩子为 2*v 右孩子为 2*v + 1
        # 在这个规则下，一颗二叉树是完全二叉树当且仅当节点编号依次为 1, 2, 3, ... 且没有间隙。
        # 因此，记录节点数和节点编号，如果节点数和编号相等，则是完全二叉树，如果不相等，说明中间有叶子节点为Null。
        # 可以采用元组记录节点和编号，这样可以少写一个类
        # 用广度优先遍历法，每层的节点按顺序加入队列中，遍历队列
        nodes = [(root,1)]
        maxIndex = 0 # 最大编号
        i = 0 #节点数
        # 判断条件错误
        # while len(nodes): 
        while i < len(nodes):
            # 简化元组取值
            # obj = nodes[i]
            # node = obj[0]
            # index = obj[1]
            node,index = nodes[i]
            i += 1 #节点序号自增要放在退出分支前
            if not node:
                # break
                continue
            maxIndex = max(maxIndex,index)
            nodes.append((node.left,2*index))
            nodes.append((node.right,2*index+1))
        return len(nodes) == nodes[-1][1]

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        #思路：题解
        # 简化逻辑
        # 改为自己更好理解的思路：叶子节点不为空时才放进去遍历
        nodes = [(root,1)]
        i = 0 #节点数
        # 判断条件错误
        while i < len(nodes):
            node,index = nodes[i] #快速取出元组元素
            i += 1 
            if node.left:
                nodes.append((node.left,2*index))
            if node.right:
                nodes.append((node.right,2*index+1))
        return i == nodes[-1][1]
    
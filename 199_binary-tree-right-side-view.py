# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        return self.dfs(root,set(),1)
        # 思路：遍历所有右节点的值,如果左节点有更深层的子节点也需要遍历,直到左节点没有更深层为止
        # 关键点：
        # 要记录深度，并判断当前深度是否已经访问过最右节点的值
        # 从右节点开始遍历，然后回溯遍历左节点，最终所有节点都要遍历到才行 => 遍历顺序是“中右左”
       
    def dfs(self,root: TreeNode,visited:set[int],level : int)-> List[int]:
        if not root:
            return []
        list = [] 
        if level not in visited: #如果当深度还没有节点值被记录，记录当前深度的值
            list = [root.val]
            visited.add(level)
        # 优先级：父节点 + 右子树 + 左子树
        return list + self.dfs(root.right, visited,level+1) + self.dfs(root.left,visited,level+1)

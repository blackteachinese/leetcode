# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # left=2K,right=2k+1
        # calculate every row width = rigtest node - leftest node
        if not root : return root
        list=[(root,1)]
        max_w=0
        while len(list) > 0:
            rows = list.copy()
            if len(rows) >= 2:
                l,l_index = rows[0]
                r,r_index = rows[-1]
                max_w = max(max_w, r_index-l_index+1)
            else:
                max_w = max(max_w,len(rows))
            # clear last row
            list.clear()
            # append next row
            while len(rows) > 0:
                n,index = rows.pop(0)
                if n.left: list.append((n.left,2*index))
                if n.right: list.append((n.right,2*index+1))
        return max_w

class Solution: # tips implementation, less code
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root : return root
        list=[(root,0,0)] # error: pos number have to start with 0,otherwise,the first row is wrong
        cur_depth = left = max_w=0
        for node,depth,pos in list:
            if not node :   # warning: skip empty node ,then the code will be simple
                continue
            list.append((node.left,depth+1,pos*2))
            list.append((node.right,depth+1,pos*2+1))
            if cur_depth != depth:
                cur_depth = depth # refresh the depth
                left = pos # store the first node of new row
            max_w = max(max_w,pos-left+1)
        return max_w
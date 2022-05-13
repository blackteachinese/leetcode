from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 方法1：暴力搜搜 O(n^2)
        # 方法2：O(2m+n)，左上角开始，走对角线遍历，直到m[i][] < target位置，此时target在m[i]所在位置的行或列
        # 方法3：O(n),右上角开始，如果m[i]<target,去掉一列，如果m[i]>target,去掉一行
        x,y=len(matrix)-1,0
        while x>=0 and y<=len(matrix[0])-1:
            print(x,y)
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] > target:
                x -= 1
            else:
                y += 1
        return False
            
# print(Solution().searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],5))
# print(Solution().searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],20))
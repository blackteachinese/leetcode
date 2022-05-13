from typing import List


class Solution1:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 方法1：顺时针遍历，当格子被访问过或超出边界，旋转90度继续遍历。旋转后的值也被访问过，则结束。
        def isOut(x,y,row,column,visited):
            return x < 0 or x >= row or y < 0 or y >= column or visited[y][x] == 1 #错误点 row column搞反
        # border
        if len(matrix) == 0 or len(matrix[0]) == 0: return matrix
        # initial
        column,row=len(matrix),len(matrix[0])
        visited=[[0 for i in range(0,row)] for j in range(0,column)]
        print(visited)
        direction=[(1,0),(0,1),(-1,0),(0,-1)]
        p=(0,0)
        index=0
        res=[]
        while True:
            res.append(matrix[p[1]][p[0]]) #错误点 row column搞反
            visited[p[1]][p[0]] = 1 #错误点 row column搞反
            # walk
            x=p[0]+direction[index][0]
            y=p[1]+direction[index][1]
            print(x,y,visited)
            # judge
            if isOut(x,y,row,column,visited):
                # change direction
                index = (index + 1) %4
                x=p[0]+direction[index][0]
                y=p[1]+direction[index][1]
                if isOut(x,y,row,column,visited): # finish
                    break
                else:
                    p=(x,y)    
            else:
                p=(x,y)
        return res

class Solution2: # 1代码数组初始化逻辑2修复row和column概念错误
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 方法1：顺时针遍历，当格子被访问过或超出边界，旋转90度继续遍历。旋转后的值也被访问过，则结束。
        def isOut(nextRow,nextCol,rows,columns,visited):
            return nextRow < 0 or nextRow >= rows or nextCol < 0 or nextCol >= columns or visited[nextRow][nextCol] == 1 #错误点 row column搞反
        # border
        if len(matrix) == 0 or len(matrix[0]) == 0: return matrix
        # initial
        # row 行；column 列
        rows,columns=len(matrix),len(matrix[0])
        visited=[[0]*columns for _ in range(rows)]
        print(visited)
        # direction=[(1,0),(0,1),(-1,0),(0,-1)]
        direction=[(0,1),(1,0),(0,-1),(-1,0)]
        row,col=0,0
        index=0
        res=[]
        while True:
            res.append(matrix[row][col]) #错误点 row column搞反
            visited[row][col] = 1 #错误点 row column搞反
            # walk
            nextRow=row+direction[index][0]
            nextCol=col+direction[index][1]
            # print(x,y,visited)
            # judge
            if isOut(nextRow,nextCol,rows,columns,visited):
                # change direction
                index = (index + 1) %4
                nextRow=row+direction[index][0]
                nextCol=col+direction[index][1]
                if isOut(nextRow,nextCol,rows,columns,visited):
                    break
                else:
                    row,col=nextRow,nextCol    
            else:
                row,col=nextRow,nextCol
        return res

class Solution: # 1代码数组初始化逻辑2修复row和column概念错误
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 方法1：顺时针遍历，当格子被访问过或超出边界，旋转90度继续遍历。旋转后的值也被访问过，则结束。
        def isOut(nextRow,nextCol,rows,columns,visited):
            return nextRow < 0 or nextRow >= rows or nextCol < 0 or nextCol >= columns or visited[nextRow][nextCol] == 1 #错误点 row column搞反
        # border
        if len(matrix) == 0 or len(matrix[0]) == 0: return matrix
        # initial
        # row 行；column 列
        rows,columns=len(matrix),len(matrix[0])
        visited=[[0]*columns for _ in range(rows)]
        direction=[(0,1),(1,0),(0,-1),(-1,0)]
        row,col=0,0
        index=0
        res=[]
        total = rows*columns
        i = 0
        while i < total:
            i+=1
            # print(row,col)
            res.append(matrix[row][col]) #错误点 row column搞反
            visited[row][col] = 1 #错误点 row column搞反
            # walk
            nextRow=row+direction[index][0]
            nextCol=col+direction[index][1]
            # judge
            if isOut(nextRow,nextCol,rows,columns,visited):
                # change direction
                index = (index + 1) %4
            row=row+direction[index][0]
            col=col+direction[index][1]  
        return res

print(Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(Solution().spiralOrder([]))
print(Solution().spiralOrder([[]]))
print(Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))


# m=[[1,2,3],[4,5,6],[7,8,9]]
# print(m[1])


# 方法2：从外层到内层，按层遍历，每一层的边界是queding
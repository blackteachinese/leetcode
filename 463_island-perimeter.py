from typing import List


class Solution:
    def islandPerimeter1(self, grid: List[List[int]]) -> int:
        # Approach 1 : iterate + , time O(MN)*4 space O(1)
        #  iterate [[0,0],[i][j]]
        # if grid[i][j] == 1 ,  search top bottom left right
        # if each direction is 0 or out of border, result += 1
        # d = [(0,-1),(0,1),(-1,0),(1,0)] # top,bottom,left,right

        
        # Approach 2 : DFS
        # 将这个“相邻关系”对应到 DFS 遍历中，就是：每当在 DFS 遍历中，从一个岛屿方格走向一个非岛屿方格，就将周长加 1
        x_max,y_max = len(grid),len(grid[0])
        print('x_max row_number:',x_max,'y_max column_number:',y_max)
        def dfs(grid,x,y) -> int:
            # print('**',x,y)
            # if (x,y) is out of border or position is water, perimeter add 1
            if x < 0 or x > x_max - 1 or y < 0 or y > y_max - 1:
                return 1
            if  grid[x][y] == 0:
                return 1
            # if (x,y) is iterated, skip
            if grid[x][y] == 2:
                return 0
            # set the position(x,y) is iterated
            grid[x][y] = 2
            # if (x,y) is insland excute dfs;top,bottom,left,right
            return dfs(grid,x,y-1) + dfs(grid,x,y+1) + dfs(grid,x-1,y) + dfs(grid,x+1,y)
        
        for x in range(0,x_max):
            for y in range(0,y_max):
                if grid[x][y] == 1:
                    return dfs(grid,x,y) # only one island


    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # Approach 2 : DFS 修复x轴和y轴的错误
        y_max,x_max = len(grid),len(grid[0])
        print('x_max row_number:',x_max,'y_max column_number:',y_max)
        def dfs(grid,y,x) -> int:
            if x < 0 or x > x_max - 1 or y < 0 or y > y_max - 1:
                return 1
            if  grid[y][x] == 0:
                return 1
            if grid[y][x] == 2:
                return 0
            grid[y][x] = 2
            return dfs(grid,y,x-1) + dfs(grid,y,x+1) + dfs(grid,y-1,x) + dfs(grid,y+1,x)
        # 遍历矩阵的正确顺序顺序是先y轴后x轴
        for y in range(0,y_max):
            for x in range(0,x_max):
                if grid[y][x] == 1:
                    return dfs(grid,y,x) 



grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
grid = [[1,0]]
# grid = [[1]]
print(len(grid),len(grid[0]))
print(Solution().islandPerimeter(grid))
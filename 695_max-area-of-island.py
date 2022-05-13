from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Approach 1 : DFS
        # 1.many island,2. find out max-area
        # iterate the grid,if grid[x][y] == 1 dfs to search the area of island
        # maintian a variable to store the max_area
        # if the island had searched , set the value = 2
        def dfs(grip,x,y) -> int:
            if x < 0 or x > x_max - 1 or y < 0 or y > y_max - 1 or grid[x][y] != 1:
                return 0 
            grid[x][y] = 2
            return 1 + dfs(grip,x,y-1) + dfs(grip,x,y+1) + dfs(grip,x+1,y) + dfs(grip,x-1,y)
        x_max,y_max=len(grid),len(grid[0])
        max_area=0
        for x in range(0,x_max):
            for y in range(0,y_max):
                if grid[x][y] == 1:
                    print('ss')
                    max_area = max(max_area,dfs(grid,x,y))
        return max_area



# grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,s1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# print(len(grid),len(grid[0]))
# grid = [[0,0,0,0,0,0,0,0]]
# grid=[[1]]
# print(Solution().maxAreaOfIsland(grid))
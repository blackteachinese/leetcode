class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Approach 1 : BFS
        # traverse the two-dimension array O(m*n)
        # maintain a visited array to specify the
        # if grid[i] is not visited and equal to 1 ,islands number add 1
        # and BFS search the island 
        # break the BFS 1 is  the grid[i] equal to 0  ; 2 is visited[i] is true
        # if grid[i] is visited ,skip the BFS search
        # 优化1，不创建visited记录，搜索过程直接吧grid[i]为1的改为0，只有grid[i]为1才搜索
        # Approach 2 :DFS
        # Approach 3 :并查集
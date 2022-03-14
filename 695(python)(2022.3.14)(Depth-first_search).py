class Solution: 
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int: 
        rows = len(grid) 
        cols = len(grid[0]) 
         
        def dfs(x, y): 
            if 0 <= x < rows and 0 <= y < cols and grid[x][y] == 1: 
                grid[x][y] = 0 
                return 1 + dfs(x - 1, y) + dfs(x + 1, y) + dfs(x, y - 1) + dfs(x, y + 1) 
            else: 
                return 0 
         
        output = 0 
        for i in range(rows): 
            for j in range(cols): 
                if grid[i][j] == 1: 
                    output = max(output, dfs(i, j)) 
         
                 
        return output

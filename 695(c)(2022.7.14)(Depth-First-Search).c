#define max(X, Y) ((X) > (Y) ? (X) : (Y))


int maxAreaOfIsland(int** grid, int gridSize, int* gridColSize){
    
    int** visited;
    visited = (int **) malloc(gridSize*sizeof(int *));
    
    for (int i = 0; i < gridSize; i++){
        visited[i] = (int *) malloc(*gridColSize*sizeof(int));
        for (int j = 0; j < *gridColSize; j++)
            visited[i][j] = 0;
    }
    
    int res = 0;
    int tmp = 0;
    for(int i=0; i < gridSize; i++){
        for(int j=0; j < *gridColSize; j++){
            tmp = dfs(grid, i, j, gridSize, *gridColSize, visited);
            res = max(res, tmp);
        }
    }
    return res;
}


int dfs(int**grid, int x, int y, int rows, int columns, int** visited){
    if (x < 0 || x >= rows || y < 0 || y >=columns) return 0;
    if (grid[x][y] == 0 || visited[x][y] == 1) return 0;
    
    visited[x][y] = 1;
    return 1
        + dfs(grid, x+1, y, rows, columns, visited)
        + dfs(grid, x-1, y, rows, columns, visited)
        + dfs(grid, x, y+1, rows, columns, visited)
        + dfs(grid, x, y-1, rows, columns, visited);
}

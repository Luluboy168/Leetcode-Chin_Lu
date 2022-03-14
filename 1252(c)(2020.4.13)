int oddCells(int n, int m, int** indices, int indicesSize, int* indicesColSize){
    int ans=0;
    int mat[50][50]={{0}};
    for(int i=0;i<indicesSize;i++){
        for(int j=0;j<m;mat[indices[i][0]][j++]++);
        for(int j=0;j<n;mat[j++][indices[i][1]]++);
    }
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            if(mat[i][j]%2!=0){
                ans++;
            }
        }
    }
    return ans;

}

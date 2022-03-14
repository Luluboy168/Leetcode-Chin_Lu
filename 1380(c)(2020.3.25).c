/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* luckyNumbers (int** matrix, int matrixSize, int* matrixColSize, int* returnSize){
    int *ans;
    ans = (int*) malloc(1 * sizeof(int));
    int small;
    int big=-1;
    for(int i=0;i<matrixSize;i++){
        small=matrix[i][0];
        for(int j=1;j<*matrixColSize;j++){
            if(matrix[i][j]<small){
                small=matrix[i][j];
            }
        }
        if(small>big){
            big=small;
        }
    }
    ans[0]=big;
    *returnSize=1;
    return ans;

}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* replaceElements(int* arr, int arrSize, int* returnSize){
    int i, j ;
    int *ans = malloc(arrSize * sizeof(int));
    for(i=0;i<arrSize-1;i++){
        ans[i] = arr[i+1];
        for(j=i+1;j<arrSize;j++){
            if(ans[i]<arr[j]){
                ans[i] = arr[j];
            }
        }
    }
    ans[arrSize-1] = -1;
    *returnSize = arrSize;
    
    return ans;

}

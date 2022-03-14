/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sortArrayByParity(int* A, int ASize, int* returnSize){
    int *ans;
    ans = (int*) malloc((ASize) * sizeof(int));
    int left=0,right=1;
    for(int i=0;i<ASize;i++){
        if(A[i]%2==0){
            ans[left]=A[i];
            left++;
        }else{
            ans[ASize-right]=A[i];
            right++;
        }
    }
    *returnSize=ASize;
    return ans;

}

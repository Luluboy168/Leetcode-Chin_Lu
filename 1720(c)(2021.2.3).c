/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* decode(int* encoded, int encodedSize, int first, int* returnSize){
    *returnSize = encodedSize+1;
    int * ans= (int*) malloc((*returnSize) * sizeof(int));
    ans[0]=first;
    ans[1]=ans[0]^encoded[0];
    for(int i=2;i<*returnSize;i++){
        ans[i]=encoded[i-1]^ans[i-1];
    }
    return ans;
    
}

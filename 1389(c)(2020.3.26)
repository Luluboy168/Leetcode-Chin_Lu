/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* createTargetArray(int* nums, int numsSize, int* index, int indexSize, int* returnSize){
    int *ans;
    ans = (int*) malloc(numsSize * sizeof(int));
    int tmp;
    for(int m=0;m<numsSize;m++){
        ans[m]=-1;
    }
    for(int i=0;i<numsSize;i++){
        if(ans[index[i]]==-1){
            ans[index[i]]=nums[i];
        } else {
            for(int j=numsSize-1;j>index[i];j--){
                if(ans[j]==-1){
                    ans[j]=ans[j-1];
                    ans[j-1]=-1;
                } 
            
            }
            ans[index[i]]=nums[i];
        }
    }
    *returnSize=numsSize;
    return ans;

}

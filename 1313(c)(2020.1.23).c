/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* decompressRLElist(int* nums, int numsSize, int* returnSize){
    int pos=0, num, a, b, ansSize=0;
    int *ans;
    for(int x=0;x<=numsSize/2-1;x++){
        ansSize += nums[x*2];
    }
    ans = (int*) malloc(ansSize * sizeof(int));
    for(int i=0;i<numsSize;i++){
        if(i%2==0) {
            a=nums[i];
        } else {
            b=nums[i];
            for(int j=0;j<=a-1;j++){
                ans[pos]=b;
                pos++;
            }
        }
        
    }
    
    *returnSize=ansSize;
    return ans;
}

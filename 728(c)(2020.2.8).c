/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* selfDividingNumbers(int left, int right, int* returnSize){
    int pos=0 ,a=10 ,i ,j ;
    int *ans;
    ans = (int*) malloc(10000 * sizeof(int));
    
    for(i=left;i<=right;i++){
        j=i;
        if(j<10){
            ans[pos++]=i;
        } else {
            while(j>1){
                if(j%10==0){
                    j=-1;
                } else if(i%(j%10)!=0){
                    j=-1;
                } else {
                    j=j/10;
                }
            }
            if(j>=0){
                ans[pos++]=i;
            }
        }
    }
        *returnSize = pos;
    return ans;
}

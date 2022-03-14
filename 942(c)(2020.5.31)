/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* diStringMatch(char * S, int* returnSize){
    int len= strlen(S);
    int m=0;
    int n=len;
    int *ans;
    ans = (int*) malloc((len+1) * sizeof(int));
    for(int i=0;i<len;i++){
        if(S[i]=='I'){
            ans[i]=m;
            m++;
        }else{
            ans[i]=n;
            n--;
        }
    }
    ans[len]=m;
    *returnSize=len+1;
    return ans;

}

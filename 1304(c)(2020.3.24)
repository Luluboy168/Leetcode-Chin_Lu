/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sumZero(int n, int* returnSize){
    int *ans;
    int x=1;
    int num=1;
    int pos=0;
    ans = (int*) malloc(10000 * sizeof(int));
    if (n%2==0){
        for(int i=1;i<=n/2;i++){
            for(int j=1;j<=2;j++){
                ans[pos]=num*x;
                x=x*-1;
                pos++;
            }
            num++;
        }
    } else {
        for(int i=1;i<=n/2;i++){
            for(int j=1;j<=2;j++){
                ans[pos]=num*x;
                x=x*-1;
                pos++;
            }
            num++;
        }
        ans[n-1]=0;
    }
    *returnSize=n;
    return ans;

}

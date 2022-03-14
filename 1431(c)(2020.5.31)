/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
bool* kidsWithCandies(int* candies, int candiesSize, int extraCandies, int* returnSize){
    bool *ans;
    ans = (bool*) malloc(candiesSize * sizeof(bool));
    int temp;
    for(int i=0;i<candiesSize;i++){
        ans[i]=true;
    }
    for(int j=0;j<candiesSize;j++){
        temp=candies[j]+extraCandies;
        for(int k=0;k<candiesSize;k++){
            if(temp<candies[k]){
                ans[j]=0;
                k=candiesSize+1;
            }
        }
    }
    *returnSize=candiesSize;
    return ans;

}

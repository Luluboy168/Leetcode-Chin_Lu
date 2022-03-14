
int arrayPairSum(int* nums, int numsSize){
    int ans=0;
    int t;
    void sort(int i,int j,int* nums);
    sort(0,numsSize-1, nums);
    for(int k=0;k<numsSize/2;k++){
        ans=ans+nums[k*2];
    }
    return ans;

}
void sort(int i,int j,int* nums){
    int low=i;
    int high=j;
    int key=nums[i];
    int temp=0;
    
    if(i>j){
        return ;
    }
    while(i<j){
        while(nums[j]>key&&i<j){
            j--;
        }
        nums[i]=nums[j];
        while(nums[i]<=key&&i<j){
            i++;
            
        }
        nums[j]=nums[i];
        
    }
    
    nums[i]=key;
    sort(low,i-1,nums);
    sort(i+1,high,nums);
    
}


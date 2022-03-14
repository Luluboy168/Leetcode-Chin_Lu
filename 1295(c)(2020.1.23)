int findNumbers(int* nums, int numsSize){
    int dig=1,ans=0;
    for(int i=0;i<numsSize;i++){
        while(nums[i]/10>0){
            nums[i]=nums[i]/10;
            dig++;
        }
        if(dig%2==0){
            ans++;
        }
        dig=1;
    }
    return ans;

}

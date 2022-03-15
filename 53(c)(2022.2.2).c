int maxSubArray(int* nums, int numsSize){
    int largest = nums[0];
    if(numsSize < 2) return largest;
    for(int i = 1; i < numsSize;i++){
        if(nums[i-1] + nums[i] > nums[i]){
            nums[i] = nums[i-1] + nums[i];
        }
        if(nums[i] > largest){
            largest = nums[i];
        }
    }
    return largest;
}

int cmpfunc(const int * a, const int * b){
    return (*a - *b);
}
bool containsDuplicate(int* nums, int numsSize){
    qsort(nums, numsSize, sizeof(int), cmpfunc);
    
    for(int i=1;i<numsSize;i++){
        if(nums[i] == nums[i-1]){
            return 1;
        }
    }
    
    return 0;

}

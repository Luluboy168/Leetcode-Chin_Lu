/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* numbers, int numbersSize, int target, int* returnSize){
    int *ans;
    *returnSize = 2;
    ans = (int*) malloc((*returnSize) * sizeof(int));
    int left = 0;
    int right = numbersSize - 1;
        int sum;
    while(left < right){
        sum = numbers[left] + numbers[right];
        if(sum == target){
            ans[0] = left + 1;
            ans[1] = right + 1;
            return ans;
        }else if(sum > target){
            right--;
        } 
        else {
            left++;
        }
    }
    return ans;

}

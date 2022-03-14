/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sortArrayByParityII(int* A, int ASize, int* returnSize){
    int even=0,odd=1;
    int temp;
    *returnSize=ASize;
    while(1){
        while(even<ASize&&A[even]%2==0){
            even=even+2;
        }
        if(even==ASize){
            return A;
        }
        while(A[odd]%2==1){
            odd=odd+2;
        }
        temp=A[even];
        A[even]=A[odd];
        A[odd]=temp;
    }

}

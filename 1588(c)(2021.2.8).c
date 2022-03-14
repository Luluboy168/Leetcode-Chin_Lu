int sumOddLengthSubarrays(int* arr, int arrSize){
    int ans=0;
    for(int i=1;i<=arrSize;i+=2){
        for(int j=0;j<=arrSize-i;j++){
            for(int k=0;k<i;k++){
                ans+=arr[j+k];
            }
        }
    }
    return ans;

}

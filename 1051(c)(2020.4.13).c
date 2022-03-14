int heightChecker(int* heights, int heightsSize){
    int ans=0;
    int t;
    int arr[heightsSize];
    for(int m=0;m<heightsSize;m++){
        arr[m]=heights[m];
    }
    for(int i=0;i<heightsSize-1;i++){
        for(int j=i;j<heightsSize-1;j++){
            if(arr[j+1]<arr[j]){
                t=arr[j];
                arr[j]=arr[j+1];
                arr[j+1]=t;
            }
        }
    }
    for(int k=0;k<heightsSize;k++){
        if(arr[k]!=heights[k]){
            ans++;
        }
    }
    return ans;

}

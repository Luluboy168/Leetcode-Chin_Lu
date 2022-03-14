bool uniqueOccurrences(int* arr, int arrSize){
    int t;
    int* a;
    a = (int*) malloc(2001 * sizeof(int));
    for(int m=0;m<2001;m++){
        a[m]=0;
    }
    for(int i=0;i<arrSize;i++){
        a[arr[i]+1000]++;
        
    }
    for(int j=0;j<2000;j++){
        if(a[j]!=0){
            for(int k=j+1;k<2001;k++){
                if(a[k]==a[j]){
                    return 0;
                }
            }
        }
        
    }
    return 1;
    
}

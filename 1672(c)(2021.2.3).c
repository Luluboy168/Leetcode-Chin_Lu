int maximumWealth(int** accounts, int accountsSize, int* accountsColSize){
    int ans=0,sum=0;
    for(int i=0;i<accountsSize;i++){
        for(int j=0;j<*accountsColSize;j++){
            sum=sum+accounts[i][j];
            
        }
        if(sum>ans)ans=sum;
        sum=0;
    }
    return ans;

}

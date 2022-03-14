int subtractProductAndSum(int n){
    int ans , i , pro=1 , sum=0 ;
    for(i=0;n!=0;i++){
        pro = pro * (n%10) ;
        sum = sum + (n%10) ;
        n=n/10;
    }
        ans = pro-sum;
    return ans;

}

int numberOfSteps (int num){
    int ans , i , n=num ;
    for(i=0;n!=0;i++){
        if(n%2==0){
            n = n/2;
        } else {
            n--;
        }
    }
    ans = i;
    return ans;

}

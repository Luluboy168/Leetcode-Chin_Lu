int maximum69Number (int num){
    int ans , i , j , n=num , pos=-1 , plus=1 ;
    for(i=0;n>0;i++){
        if(n%10==6){
            pos = i;
        }
        n=n/10;
    }
    if(pos==-1){
        return num;
    }
    for(j=pos;pos>0;pos--){
        plus = plus*10;
    }
    ans = num + (3*plus);
    return ans;
}

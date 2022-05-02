bool isHappy(int n){
    int ret;
    int sum = 0;
    
    if (n==1 || n==7){
        return true;
    } else if(n < 10){
        return false;
    }
    
    while(n > 0){
        sum = sum + ((n % 10) * (n % 10));
        n = n / 10;
    }
    
    ret = isHappy(sum);
    
    if (ret==1 || ret==7){
        return true;
    }
    
    return false;
    
    
    
}

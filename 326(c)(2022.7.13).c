bool isPowerOfThree(int n){ 
    //solution 1
    // pow(3,19) (= 1,162,261,467) is the max int which is less than INT_MAX. 
    return (n > 0) && ((int)(pow(3,19)) % n == 0);
    
    //solution 2 
    //if (n < 1) return false; 
    //while(n % 3 == 0) n = n / 3; 
    //return (n == 1); 
     
    //solution 3 
    // long x = 1; 
    // while(x <= n){ 
    //     if (x != n) x = x * 3; 
    //     else return true; 
    // } 
    // return false; 
}

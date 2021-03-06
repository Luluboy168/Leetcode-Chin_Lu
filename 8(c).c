#include <limits.h>

int myAtoi(char * s){
    
    if(s == NULL) return 0;
    int neg = 1;
    char c = s[0];
    int i = 0;
    
    while(c != '\0'){
        if(isdigit(c)) break;
        char nextchar = s[i+1];
        if(nextchar == '\0'){
            return 0;
        }else if(c == '.' && isdigit(nextchar)){
            return 0;
        }else if(c == '-' || c == '+'){
            if(isalpha(nextchar)) return 0;
            i++;
            if(c == '-') neg = -1;
            break;
        }
        else if(isalpha(c)){
            return 0;
        }
        c = s[++i];
    }
    
    int res = 0;
    while(isdigit(s[i])){
        int d = neg * (s[i] - '0');
        if(res > INT_MAX/10 ||(res == INT_MAX/10 && d > 7)) return INT_MAX;
        if(res < INT_MIN/10 || (res == INT_MIN/10 && d < -8)) return INT_MIN;
        res = res * 10 + d;
        i++;
    }
    return res;
}

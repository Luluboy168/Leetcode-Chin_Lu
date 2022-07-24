bool isSubsequence(char * s, char * t){ 
     
    int j = 0; 
     
    for(int i=0; i < strlen(t); i++){ 
        if (j == strlen(s)) return true; 
        if (t[i] == s[j]) j++; 
    } 
     
    return (j == strlen(s)); 
}

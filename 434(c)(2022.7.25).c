int countSegments(char * s){ 
    if (strlen(s) == 0) return 0; 
    int seg = 0; 
    bool space = true; 
    for(int i=0; i < strlen(s); i++){ 
        if (s[i] != ' ' && space) { 
            seg++; 
            space = false; 
        }else if (s[i] == ' ') space = true; 
    } 
    return seg; 
}

int strStr(char * haystack, char * needle){
    int start = 0;
    int same = 0;
    int hlen, nlen;
    for(hlen = 0;haystack[hlen] != '\0';++hlen);  //hlen = strlen(haystack);
    for(nlen = 0;needle[nlen] != '\0';++nlen);  //nlen = strlen(needle);
    if(nlen == 0){
        return 0;
    }
    if(nlen > hlen){
        return -1;
    }
    for(int i = 0;i<hlen;i++){
        if(haystack[i]==needle[0]){
            start = i;
            if((start + nlen)>hlen){
                return -1;
            }
            for(int j = 0;j<nlen;j++){
                if(haystack[i+j]==needle[j]){
                    same = 1;
                }else{
                    same = 0;
                    j = nlen;
                }
            }
            if(same==1){
                return start;
            }
        }
    }
    return -1;
}

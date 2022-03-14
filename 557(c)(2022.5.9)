char * reverseWords(char * s){
    char temp;
    int pos=0;
    for(int i=0;s[i]!='\0';i++){
        if(s[i+1]==' '||s[i+1]=='\0'){
            for(int j=pos;j-pos<=(i-pos)/2;j++){
                temp=s[j];
                s[j]=s[i-j+pos];
                s[i-j+pos]=temp;
            }
            pos=i+2;
        }
    }
    return s;

}


int minDeletionSize(char ** A, int ASize){
    int ans=0;
    int word=(int)'a';
    int len = strlen(A[0]);
    for(int i=0;i<len;i++){
        word=A[0][i];
        for(int j=1;j<ASize;j++){
            if(A[j][i]<word){
                ans++;
                j=ASize;
            }else{
                word=A[j][i];
            }
        }
    }
        
    return ans;

}

char * interpret(char * command){
    int pos = 0;
    int N=strlen(command);
    for(int i=0;i<N;i++){
        if(command[i]=='G'){
            command[pos++]='G';
        } else if(command[i+1]==')'){
            command[pos++]='o';
            i++;
        } else if(command[i+1]=='a'){
            command[pos++]='a';
            command[pos++]='l';
            i=i+2;
        }
    }
    command[pos]='\0';
    return command;

}

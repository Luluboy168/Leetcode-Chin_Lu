bool isVowel(char c){
    return 
        c == 'a' || c == 'A' ||
        c == 'e' || c == 'E' ||
        c == 'i' || c == 'I' ||
        c == 'o' || c == 'O' ||
        c == 'u' || c == 'U';
}

char * reverseVowels(char * s){

	//Two pointers
    int front = 0;
    int back = strlen(s) - 1;
	
    while(front < back){
        if (isVowel(s[front])){
            if (isVowel(s[back])){
                char tmp = s[back];
                s[back] = s[front];
                s[front] = tmp;
                front++;
            }
            back--;
        }
        else front++;
    }
    return s;

}

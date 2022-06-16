bool isIsomorphic(char * s, char * t){
    //using two map
    int *map1 = calloc(255, sizeof(int)), *map2 = calloc(255, sizeof(int)); 
    //(calloc會設置記憶體分配為0)
    for(int i = 0; s[i] != '\0';i++){
        if (*(map1 + (int)s[i]) == 0){
            *(map1 + (int)s[i]) = t[i];
        } else{
            if(*(map1 + (int)s[i]) != t[i]){
                return 0;
            }
        }
    }
    for(int j = 0; t[j] != '\0'; j++){
        if (*(map2 + (int)t[j]) == 0){
            *(map2 + (int)t[j]) = s[j];
        } else{
            if (*(map2 + (int)t[j]) != s[j]){
                return 0;
            }
        }
    }
    return 1;

}

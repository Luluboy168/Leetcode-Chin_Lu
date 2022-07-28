bool isAnagram(char * s, char * t){
    int size_s = strlen(s);
    int size_t = strlen(t);
    if (size_s != size_t) return false;
    int map[26] = {0};
    for (int i=0; i < size_s; i++){
        map[s[i] - 'a']++;
        map[t[i] - 'a']--;
    }
    for (int i=0; i < 26; i++){
        if (map[i] != 0) return false;
    }
    return true;
}

int countMatches(char *** items, int itemsSize, int* itemsColSize, char * ruleKey, char * ruleValue){
    int key;
    if (ruleKey[0] == 't') {
        key=0;
    }else if(ruleKey[0] == 'c'){
        key=1;
    }else if(ruleKey[0] == 'n'){
        key=2;
    }
    int count=0;
    for (int i=0;i<itemsSize;i++){
        if(strcmp(items[i][key],ruleValue)==0) count++;
    }
    return count;
}
/**Runtime: 101 ms, faster than 14.65% of C online submissions for Count Items Matching a Rule.

Memory Usage: 13.6 MB, less than 77.59% of C online submissions for Count Items Matching a Rule.
10/2

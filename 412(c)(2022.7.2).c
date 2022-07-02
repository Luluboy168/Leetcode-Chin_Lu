/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char ** fizzBuzz(int n, int* returnSize){
    
    *returnSize = n;
    char** ans = (char**)malloc(n * sizeof(char*));
    char s[9];
    for(int i=1; i<=n; i++){
        if (i % 15 == 0) sprintf(s, "%s", "FizzBuzz");
        else if (i % 3 == 0) sprintf(s, "%s", "Fizz");
        else if (i % 5 == 0) sprintf(s, "%s", "Buzz");
        else sprintf(s, "%d", i);
        ans[i-1] = malloc(sizeof(s));
        memcpy(ans[i-1], s, strlen(s) + 1);
        memset(s, "", 9);
    }
    return ans;
}

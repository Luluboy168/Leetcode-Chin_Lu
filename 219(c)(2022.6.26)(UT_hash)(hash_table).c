//UT hash solution
//#include "uthash.h"

//define a hash structure
struct hash_struct{
    int id;           //the value of numbers
    int value;        //the position of numbers
    UT_hash_handle hh; //make this structure hashable
};

bool containsNearbyDuplicate(int* nums, int numsSize, int k){
    struct hash_struct *map = NULL; //initialize to NULL
    for (int i=0; i < numsSize; i++){
        struct hash_struct * tmp;
        HASH_FIND_INT(map, &nums[i], tmp);
        if (tmp == NULL){
            tmp = (struct hash_struct *)malloc(sizeof(struct hash_struct));
            tmp->id = nums[i];
            tmp->value = i;
            HASH_ADD_INT(map, id, tmp);
        } else {
            if ((i - tmp->value) <= k){
                return true;
            } else {
                tmp->value = i;
            }
        }
    }
    return false;
}

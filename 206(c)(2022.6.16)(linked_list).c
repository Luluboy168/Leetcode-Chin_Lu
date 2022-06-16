/** 
 * Definition for singly-linked list. 
 * struct ListNode { 
 *     int val; 
 *     struct ListNode *next; 
 * }; 
 */ 
struct ListNode* reverseList(struct ListNode* head){ 
    if (head == NULL || head->next == NULL){ 
        return head; 
    } 
    struct ListNode* prev = (struct ListNode*)malloc(sizeof(struct ListNode*)); 
    struct ListNode* iterator = (struct ListNode*)malloc(sizeof(struct ListNode*)); 
    prev = NULL; 
    iterator = head; 
    while(iterator != NULL){ 
        struct ListNode* curr = iterator; 
        iterator = iterator->next; 
        curr->next = prev; 
        prev = curr; 
    } 
    return prev; 
     
}

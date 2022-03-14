# DDefinition  for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        c = 0
        while temp:            #計算linked list長度
            c += 1
            temp = temp.next
        a = c - n + 1
        temp2 = head
        prev = None
        i = 1
        while i < a:
            i += 1
            prev = temp2
            temp2 = temp2.next  #指出要刪除元素
        if temp2 == head:        #要刪除的質為第一個
            return head.next
        prev.next = temp2.next  #將結點連結
        return head

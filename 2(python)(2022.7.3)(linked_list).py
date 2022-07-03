# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ret = ListNode((l1.val+l2.val) % 10)
        quo = (l1.val+l2.val) // 10
        tmp = ret
        
        while(l1.next and l2.next):
            c = l1.next.val + l2.next.val + quo
            tmp.next = ListNode(c % 10)
            quo = c // 10
            l1 = l1.next
            l2 = l2.next
            tmp = tmp.next
            
        while(l1.next):
            c = l1.next.val + quo
            tmp.next = ListNode(c % 10)
            quo = c // 10
            tmp = tmp.next
            l1 = l1.next
            
        while(l2.next):
            c = l2.next.val + quo
            tmp.next = ListNode(c % 10)
            quo = c // 10
            tmp = tmp.next
            l2 = l2.next
        
        if(quo):
            tmp.next = ListNode(quo)
            
        return ret

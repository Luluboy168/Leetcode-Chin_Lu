# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head      #一倍速度
        fast = head      #兩倍速度
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow

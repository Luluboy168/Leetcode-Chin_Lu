# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        #traverse first LL, flip the value to negtive 
        #traverse second LL until hit a negtive value --> store the value
        #traverse fiRST LL, flip the value back to positive 
        nodeA = headA
        while nodeA:
            nodeA.val *= -1
            nodeA = nodeA.next
            
        nodeB = headB
        nodeI = None
        while nodeB:
            if nodeB.val < 0:
                nodeI = nodeB
                break
            nodeB = nodeB.next
            
        nodeA = headA
        while nodeA:
            nodeA.val *= -1
            nodeA = nodeA.next
            
        return nodeI

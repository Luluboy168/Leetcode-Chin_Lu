#solution 1

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        #solution 1
        ls = []
        while head != None:
            ls.append(head.val)
            head = head.next
        if ls == ls[::-1]:
            return True
        else: 
            return False
          
          
#solution 2 (reverse linked list, slow fast pointer)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        #solution 2
        
        #reverse function
        def reverse(prev, head):
            if not head:
                return prev
            tmp = head.next
            head.next = prev
            return reverse(head, tmp)
        
        #use slow and fast pointer to get the mid of list
        sp = head
        fp = sp
        while(fp and fp.next):
            sp = sp.next
            fp = fp.next.next
            
        mid = reverse(None, sp)
        
        # if (not mid.next):
        #     return True
        # else:
        #     return False
        
        #check for palindrome
        def check(mid, head):
            if(not mid):
                return True
            elif(mid.val == head.val):
                return check(mid.next, head.next)
            else:
                return False
            
        return check(mid, head)
      
      
#solution 3 (recursive)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
      
        #recursive
        global front
        front = head

        def helper(back) -> bool:
            global front
            if not back:
                return True

            #let back pointer travel to the back of the list through recursion
            equal_so_far = helper(back.next)

            #check if front and back have the same value
            value_equal = (front.val == back.val)

            #when the function return, back is gradually moved toward head of the list
            #move front accordingly to compare their value
            front = front.next
            return equal_so_far and value_equal
        
        return helper(head)

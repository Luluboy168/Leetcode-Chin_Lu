"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None
        
        queue = []
        queue.append(root)
        
        while queue:
            temp = []
            while queue:
                cur = queue.pop(0)
                if cur.left:
                    temp.append(cur.left)
                if cur.right:
                    temp.append(cur.right)
                    
            for i in range(len(temp)-1):
                temp[i].next = temp[i + 1]
            queue.extend(temp)
            
        return root

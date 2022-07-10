class Solution:
    def reverseVowels(self, s: str) -> str:
        
        #Two pointers
        
        #because 'str' object does not support item assignmen
        #we need to change type of s into list
        s = list(s)
        
        front = 0
        back = len(s) - 1
        while(front < back):
            if s[front].lower() in ['a', 'e', 'i', 'o', 'u']:
                if s[back].lower() in ['a', 'e', 'i', 'o', 'u']:
                    s[front], s[back] = s[back], s[front]
                    front += 1
                back -= 1
            else:
                front += 1
        return ''.join(s) #convert the answer back to str

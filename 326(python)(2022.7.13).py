class Solution: 
    def isPowerOfThree(self, n: int) -> bool: 
         
        #loop solution 
        x = 1 
        while x <= n: 
            if x != n: 
                x = x * 3 
            else: 
                return True 
        return False

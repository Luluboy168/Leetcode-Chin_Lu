class Solution:
    def reverseBits(self, n: int) -> int:
        
        #Bit shifting 
        res = 0
        
        for i in range(32):
            res = res << 1   #left shift res
            res += n & 1     #get the last bit of n
            n = n >> 1       #right shift n
        
        return res

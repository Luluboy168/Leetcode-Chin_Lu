class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        #recursive
        if columnNumber <= 26:   #base case
            return chr(ord('A') + columnNumber - 1)
        else:
            return self.convertToTitle((columnNumber-1)//26) + self.convertToTitle((columnNumber-1)%26+1)

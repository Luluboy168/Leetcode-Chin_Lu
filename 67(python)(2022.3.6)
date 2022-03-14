class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        #10-->2
        a10 = int(a, 2)
        b10 = int(b, 2)
        sum = a10 + b10
        
        # return format(sum, "b")     #整型轉換為二進位制
        
        result = ""
        while sum != 0:
            remain = sum % 2
            result = str(remain) + result
            sum = sum // 2
        if result != "":
            return result
        else:
            return "0"

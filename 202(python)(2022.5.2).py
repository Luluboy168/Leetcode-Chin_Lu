class Solution:
    def isHappy(self, n: int) -> bool:
         
            temp = []
            
            while n != 1:
                n = sum(int(i)**2 for i in str(n))
                if n in temp:
                    return 0
                else:
                    temp += [n]
            return 1

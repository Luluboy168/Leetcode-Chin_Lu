class Solution:
    def climbStairs(self, n: int) -> int:
        k = [None] * (n + 1)
        k[0], k[1] = 1, 1
        
        for i in range(2, n + 1):
            k[i] = k[i-2] + k[i-1]
        
        return k[n]

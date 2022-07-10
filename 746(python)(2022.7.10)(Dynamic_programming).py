class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        #dynamic programming
        n = len(cost)
        
        if n == 2:
            return min(cost)
        
        pay = [0] * n
        pay[0], pay[1] = cost[0], cost[1] #initializing
        
        for i in range(2, n):
            pay[i] = min(pay[i-1], pay[i-2]) + cost[i]  #minimum cost to reach index i
        
        return min(pay[-1], pay[-2])

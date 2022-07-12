class Solution: 
    def makesquare(self, matchsticks: List[int]) -> bool: 
         
        #DFS solution 
         
        value = sum(matchsticks) 
        if value < 4 or value % 4 != 0: 
            return False 
        edge = value // 4 
        #sort the list in a decending order 
        matchsticks.sort(reverse=True)  
         
        @cache 
        def dfs(l1, l2, l3, l4, i): 
            nonlocal edge 
            if i == len(matchsticks): 
                return l1 == l2 == l3 == l4 
            if l1 > edge or l2 > edge or l3 > edge or l4 > edge: 
                return False 
            return dfs(l1+matchsticks[i], l2, l3, l4, i+1) or dfs(l1, l2+matchsticks[i], l3, l4, i+1) or dfs(l1, l2, l3+matchsticks[i], l4, i+1) or dfs(l1, l2, l3, l4+matchsticks[i], i+1)  
         
        return dfs(0, 0, 0, 0, 0)

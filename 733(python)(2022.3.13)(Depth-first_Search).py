class Solution: 
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]: 
         
        curColor = image[sr][sc] 
        row = len(image) 
        column = len(image[0]) 
         
        #Depth first search 
        def dfs(x, y): 
             
            if (0 <= x < row) and (0 <= y < column) and (image[x][y] == curColor) and (image[x][y] != newColor): 
                image[x][y] = newColor 
                 
                dfs(x - 1, y)   #up 
                dfs(x + 1, y)   #down 
                dfs(x, y - 1)   #left 
                dfs(x, y + 1)   #right 
         
        dfs(sr, sc) 
         
        return image 

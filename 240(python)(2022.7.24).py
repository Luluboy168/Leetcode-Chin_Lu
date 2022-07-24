class Solution: 
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool: 
         
        # start from the bottom-left coner 
        row, col = len(matrix) - 1, 0 
         
        while row >= 0 and col <= len(matrix[0]) - 1: 
            cell = matrix[row][col] 
            if cell > target: 
                row -= 1 
            elif cell < target: 
                col += 1 
            else: 
                return True 
         
        return False
      
#       # solution 2
#       for i in matrix: 
#             if target in i: return True 
#         return False
      
#       #solution 3
#       for i in range(len(matrix)): 
#             if matrix[i][0] == target: 
#                 return True 
#             if matrix[i][0] > target: 
#                 break 
                 
#         for j in range(len(matrix[0])): 
#             if matrix[0][j] == target: 
#                 return True 
#             elif matrix[0][j] > target: 
#                 break 
         
#         for x in range(1, i + 1): 
#             for y in range(1, j + 1): 
#                 if matrix[x][y] == target: 
#                     return True 
                 
#         return False

#Pascal's triangle
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        output = [[0 for i in range(rowIndex + 1)] for j in range(rowIndex + 1)]
        
        for i in range(rowIndex + 1):
            for j in range(rowIndex + 1):
                if i == j:
                    output[i][j] = 1
                else:
                    output[i][j] = output[i - 1][j - 1] + output[i - 1][j]
                
        return output[rowIndex][:rowIndex + 1]

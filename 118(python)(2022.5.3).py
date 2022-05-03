#Pascal's triangle
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = [[0 for i in range(numRows)] for j in range(numRows)]
        for i in range(numRows):
            for j in range(i + 1):
                if (i==0) or (j==0) or (j==i):
                    output[i][j] = 1
                else:
                    output[i][j] = output[i - 1][j - 1] + output[i - 1][j]
                    
            for x, k in enumerate(range(i + 1, numRows)):
                if output[i][numRows - x - 1] == 0:
                    del(output[i][numRows - x - 1])
        
        return output
            
#[[1,0,0,0,0],[1,1,0,0,0],[1,2,1,0,0],[1,3,3,1,0],[1,4,6,4,1]]

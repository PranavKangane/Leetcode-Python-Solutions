class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zero.append([i,j])
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                for pairs in zero:
                    if i == pairs[0] or j == pairs[1]:
                         matrix[i][j] = 0 
        
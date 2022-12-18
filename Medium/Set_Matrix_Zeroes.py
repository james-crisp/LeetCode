#James Crisp
#Dec. 17, 2022

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        def makezero(matrix,pos):
            for k in range(len(matrix)):
                matrix[k][pos[1]] = 0
            for k in range(len(matrix[0])):
                matrix[pos[0]][k] = 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    makezero(matrix,[i,j])

        return

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        row, col = len(matrix), len(matrix[0])
        zero_row = any(matrix[0][c] == 0 for c in range(col)) 
        zero_col = any(matrix[r][0] == 0 for r in range(row)) 

        for r in range(1, row):
            for c in range(1, col):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
    
        for r in range(1, row):
            for c in range(1, col):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        
        if zero_row:
            for c in range(col):
                matrix[0][c] = 0
        
        if zero_col:
            for r in range(row):
                matrix[r][0] = 0
        


        
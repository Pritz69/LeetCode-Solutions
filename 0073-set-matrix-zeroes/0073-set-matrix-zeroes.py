class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row,col=len(matrix),len(matrix[0])
        rowZeros=False
        
        for r in range(row):
            for c in range(col):
                if matrix[r][c]==0:
                    matrix[0][c]=0
                    if r>0:
                        matrix[r][0]=0
                    else:
                        rowZeros=True
        for r in range(1,row):
            for c in range(1,col):
                if matrix[0][c]==0 or matrix[r][0]==0:
                    matrix[r][c]=0

        if matrix[0][0]==0:
            for r in range(row):
                matrix[r][0]=0
        if rowZeros:
            for c in range(col):
                matrix[0][c]=0
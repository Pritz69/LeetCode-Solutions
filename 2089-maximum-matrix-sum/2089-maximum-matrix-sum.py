class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        c=0
        s=0
        m=float('inf')
        for i in range(len(matrix)) :
            for j in range(len(matrix[0])) :
                if (matrix[i][j] < 0) :
                    c=c+1
                s=s+abs(matrix[i][j])    
                m=min(m,abs(matrix[i][j]))
        if c%2==1 :
            return s-(m*2)
        else :
            return s
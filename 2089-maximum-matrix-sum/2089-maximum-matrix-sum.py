class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        c=0
        s=0
        m=float('inf')
        for i in range(len(matrix)) :
            for j in range(len(matrix[0])) :
                if (matrix[i][j] < 0) :
                    c=c+1
                e=abs(matrix[i][j])
                s=s+e    
                m=min(m,e)
        if c%2==1 :
            return s-(m*2)
        else :
            return s
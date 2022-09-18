class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        N,M=len(matrix),len(matrix[0])
        r,c=N-1,0
        while r >=0 and c < M :
            if target == matrix[r][c] :
                return True
            elif target < matrix[r][c] :
                r -=1
            else :
                c +=1
        return False

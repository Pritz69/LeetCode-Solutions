class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        n,m=len(rowSum),len(colSum)
        mat=[[0]*(m) for i in range(n)]
        cols=0
        for r in range(n) :
            mat[r][0]=rowSum[r]
        for c in range(m) :
            cols=0
            for r in range(n) :
                cols +=mat[r][c]
            r=0
            while cols > colSum[c] : 
                diff=cols-colSum[c]
                maxshift=min(mat[r][c],diff)
                mat[r][c] -=maxshift
                mat[r][c+1] +=maxshift
                cols -= maxshift
                r +=1
        return mat
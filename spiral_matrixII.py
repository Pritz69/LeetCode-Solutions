class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        output=[[0]*n for _ in range(n)]
        i=0
        sr,sc,er,ec=0,0,n,n
        while sr<er or sc <ec :
            for c in range(sc,ec) :
                i +=1
                output[sr][c]=i
            sr +=1
            for r in range(sr,er) :
                i +=1
                output[r][ec-1]=i
            ec -=1
            for c in range(ec-1,sc-1,-1) :
                i +=1
                output[er-1][c]=i
            er -=1
            for r in range(er-1,sr-1,-1) :
                i +=1
                output[r][sc]=i
            sc +=1
        return output 

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)
        m=len(grid[0])
        rows=[0]*n
        cols=[0]*m
        for i in range(n) :
            for j in range(m) :
                if grid[i][j]==1:
                    rows[i] +=1
                    cols[j] +=1
        ans=[[0]*m for i in range(n)]
        #print(rows,cols)
        for i in range(n) :
            for j in range(m) :
                ans[i][j]=rows[i]+cols[j]-(n-rows[i])-(m-cols[j])
        return ans

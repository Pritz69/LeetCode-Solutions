class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        dr={}
        dc={}
        for i in range(n) :
            for j in range(m) :
                if grid[i][j] :
                    dr[i]=dr.get(i,0)+1
                    dc[j]=dc.get(j,0)+1
        ans=0
        for i in range(n) :
            for j in range(m) :
                if grid[i][j] and (dr[i] > 1 or dc[j]>1) :
                    ans +=1
        return ans
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        rc=[0]*n
        cc=[0]*m
        for i in range(n):
            rc[i]=grid[i].count(1)
        for j in range(m) :
            c=0
            for i in range(n) :
                if grid[i][j] :
                    c +=1
            cc[j]=c
        ans=0
        for i in range(n) :
            for j in range(m) :
                if grid[i][j] and (rc[i] > 1 or cc[j]>1) :
                    ans +=1
        return ans
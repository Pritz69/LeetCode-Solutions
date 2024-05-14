class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        dr=[0,0,1,-1]
        dc=[1,-1,0,0]
        def rec(i,j) :
            if i<0 or i==n  or j <0 or j==m or grid[i][j]==0 :
                return 0
            ans=0
            temp=grid[i][j]
            grid[i][j]=0
            for k in range(4) :
                nr=i+dr[k]
                nc=j+dc[k]
                ans=max(ans,rec(nr,nc))
            grid[i][j]=temp
            return ans+grid[i][j]
        ans=0
        for i in range(n) :
            for j in range(m) :
                if grid[i][j] != 0 :
                    ans=max(ans,rec(i,j))
        return ans

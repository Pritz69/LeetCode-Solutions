class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n=len(grid)
        m=len(grid[0])
        def dfs(i,j) :
            if i >= n or j >= m or i<0 or j<0 or grid[i][j]=='0' :
                return
            grid[i][j]='0'
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
            return
        c=0
        for i in range(n) :
            for j in range(m) :
                if grid[i][j]=='1' :
                    c +=1
                    dfs(i,j)
        return c

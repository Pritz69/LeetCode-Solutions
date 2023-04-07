class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        def dfs(r,c) :
            if (r<0 or c<0 or r==row or c==col or grid[r][c]==0 or (r,c) in visit) :
                return 0
            visit.add((r,c))
            res =1
            res +=dfs(r+1,c)
            res +=dfs(r-1,c)
            res +=dfs(r,c+1)
            res +=dfs(r,c-1)
            return res
        visit=set()
        res=0
        land=0
        for r in range(row) :
            for c in range(col) :
                land +=grid[r][c]
                if (grid[r][c]==1 and (r,c) not in visit and (c in [0,col-1] or r in [0,row-1])):
                    res += dfs(r,c)
        return land-res       

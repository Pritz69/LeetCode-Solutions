class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        def dfs(r,c) :
            if r<0 or c<0 or r==row or c==col :
                return 0
            if grid[r][c]==1 or (r,c) in visit :
                return 1
            visit.add((r,c))
            return min(dfs(r+1,c),dfs(r-1,c),dfs(r,c+1),dfs(r,c-1))
        visit=set()
        res=0
        for r in range(row) :
            for c in range(col) :
                if grid[r][c]==0 and (r,c) not in visit:
                    res += dfs(r,c)
        return res       

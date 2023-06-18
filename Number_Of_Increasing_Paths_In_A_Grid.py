class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        r=len(grid)
        c=len(grid[0])
        @lru_cache(None)
        def dfs(i,j) :
            res=1
            for dx,dy in [[i,j+1],[i+1,j],[i,j-1],[i-1,j]] :
                if 0<=dx<r and 0<=dy<c and grid[dx][dy] > grid[i][j]  :
                    res = res + dfs(dx,dy)
            return res
        cval=[]
        for i in range(r) :
            for j in range(c) :
                cval.append(dfs(i,j))
        s=sum(cval)
        return s%(10**9 +7)

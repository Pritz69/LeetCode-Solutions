class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        N=len(grid)
        q=deque()
        for r in range(N) :
            for c in range(N) :
                if grid[r][c] :
                    q.append([r,c])
        res=-1
        dir=[[0,1],[1,0],[0,-1],[-1,0]]
        while q :
            r,c=q.popleft()
            res=grid[r][c]
            for dr,dc in dir :
                newr,newc= r+dr,c+dc
                if (min(newr,newc) >= 0 and max(newr,newc) < N and grid[newr][newc] ==0 ) :
                    q.append([newr,newc])
                    grid[newr][newc] =grid[r][c] + 1
        return res-1 if res > 1 else -1   

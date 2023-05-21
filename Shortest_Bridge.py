class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n=len(grid)
        direct=[[0,1],[0,-1],[1,0],[-1,0]]
        def invalid (r,c) :
            return r<0 or c<0 or r==n or c==n 
        visit=set()
        def dfs(r,c) :
            if (invalid(r,c) or not grid[r][c]  or (r,c) in visit ) :
                return 
            visit.add((r,c))
            for dr,dc in direct :
                dfs(r+dr,c+dc)
        def bfs() :
            q=deque(visit)
            res=0
            while q :
                for i in range(len(q)) :
                    r,c=q.popleft()
                    for dr,dc in direct :
                        newr=r+dr
                        newc=c+dc
                        if invalid(newr,newc) or (newr,newc) in visit :
                            continue
                        if grid[newr][newc] :
                            return res
                        q.append([newr,newc])
                        visit.add((newr,newc))   
                res +=1
        for r in range(n) :
            for c in range(n) :
                if grid[r][c] :
                    dfs(r,c)
                    return bfs()
                 

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        q=deque()
        dirs=[(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(1,1),(-1,1),(1,-1)]
        if grid[0][0]==0:
            q.append((1,(0,0)))
            grid[0][0]=1
        while q:
            steps,tmp=q.popleft()
            r,c=tmp[0],tmp[1]
            if (r,c)==(m-1,n-1):
                return steps 
            for i,j in dirs:
                nr,nc=r+i,c+j
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc]==0:
                    q.append((steps+1,(nr,nc)))
                    grid[nr][nc]=1
        return -1

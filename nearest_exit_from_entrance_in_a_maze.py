class Solution:
    def nearestExit(self, maze: List[List[str]], e: List[int]) -> int:
        
        m, n = len(maze), len(maze[0])
        x, y = e
        
        # this lambda checks the exit condition 
        is_exit = lambda i, j : i*j==0 or i==m-1 or j==n-1
        
        # this generator yields (!) allowed directions
        def adj(i,j, dirs=[1, 0, -1, 0, 1]):
            for d in range(4):
                ii, jj = i + dirs[d], j + dirs[d+1]
                if 0 <= ii < m and 0 <= jj < n and maze[ii][jj] != "+":
                    yield ii,jj
            
        dq = deque([(x,y,0)])                      # [1] start from the entrance...
        maze[x][y] = '+'                           #     ...and mark it as visited
        while dq:                                  # [2] while there are still places to go...
            i, j, s = dq.popleft()                 #     ...try going there (don't try, do it!)
            for ii,jj in adj(i,j):                 # [3] look around, make a step...
                maze[ii][jj] = "+"                 #     ...and mark it as visited
                if is_exit(ii,jj) : return s+1     # [4] great, it's the exit!
                dq.append((ii,jj,s+1))             # [5] or maybe not, continue searching
                
        return -1                                  # [6] BFS failed, there is no escape

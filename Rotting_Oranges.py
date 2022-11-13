class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0 
        time = 0
        ROWS,COLS = len(grid),len(grid[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        q = collections.deque() 
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r,c))
        
        while q and fresh > 0:
            for _ in range(len(q)):
                r,c = q.popleft()
                for d in directions:
                    row,col = r + d[0],c + d[1]
                    if (row >= 0 and row < ROWS and col >= 0 and col < COLS
                         and grid[row][col] == 1):
                        fresh -= 1
                        grid[row][col] = 2
                        q.append((row,col))
                    
            time += 1
        
        return time if not fresh else -1
                                    
            

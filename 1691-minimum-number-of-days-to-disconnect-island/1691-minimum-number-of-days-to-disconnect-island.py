class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        def dfs(r, c, g):
            if r < 0 or r >= len(g) or c < 0 or c >= len(g[0]) or g[r][c] != 1:
                return
            g[r][c] = 2
            for nr, nc in (r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1):
                dfs(nr, nc, g)
        
        def num_of_islands(g):
            res = 0
            for r in range(len(g)):
                for c in range(len(g[0])):
                    if g[r][c] == 1:
                        dfs(r, c, g)
                        res += 1
            return res
        
        if num_of_islands(copy.deepcopy(grid)) != 1:
            return 0
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]:
                    grid_copy = copy.deepcopy(grid)
                    grid_copy[r][c] = 0
                    if num_of_islands(grid_copy) != 1:
                        return 1
        
        return 2
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, cols = len(grid1), len(grid1[0])
        visit = set()
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in visit or grid2[r][c] == 0:
                return True
            if grid1[r][c] == 0:
                return False
            visit.add((r, c))
            return dfs(r + 1, c) & dfs(r - 1, c) & dfs(r, c + 1) & dfs(r, c - 1)
        
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid2[r][c] == 1 and (r, c) not in visit and dfs(r, c):
                    count += 1
        return count
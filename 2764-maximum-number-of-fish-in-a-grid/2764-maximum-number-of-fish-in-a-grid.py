class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] > 0:
                    ans = max(ans, self.dfs(i, j, grid, n, m))
        return ans

    def dfs(self, i: int, j: int, grid: List[List[int]], n: int, m: int) -> int:
        f = grid[i][j]
        grid[i][j] = 0
        dr = [0, 1, 0, -1, 0]
        for k in range(4):
            nr = i + dr[k]
            nc = j + dr[k + 1]
            if nr >= 0 and nr < n and nc >= 0 and nc < m and grid[nr][nc] > 0:
                f += self.dfs(nr, nc, grid, n, m)
        return f
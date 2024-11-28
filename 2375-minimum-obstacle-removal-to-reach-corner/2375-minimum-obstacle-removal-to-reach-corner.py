class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = map(len, (grid, grid[0]))
        dist = [[inf] * n for _ in range(m)]
        dist[0][0] = grid[0][0]
        hp = [(dist[0][0], 0, 0)]
        while hp:
            o, r, c = heappop(hp)
            if (r, c) == (m - 1, n - 1):
                return o
            for i, j in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                if m > i >= 0 <= j < n and grid[i][j] + o < dist[i][j]:
                    dist[i][j] = grid[i][j] + o
                    heappush(hp, (dist[i][j], i, j))
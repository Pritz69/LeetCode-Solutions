class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = [[float("inf")]*(cols+1) for i in range(rows+1)]
        res[rows-1][cols] = 0

        for x in range(rows-1,-1,-1):
            for y in range(cols-1,-1,-1):
                res[x][y] = grid[x][y] + min(res[x+1][y], res[x][y+1])

        return res[0][0]

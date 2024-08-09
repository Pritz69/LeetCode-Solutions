class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def isMagicSquare(r,c):
            seen = set()
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    if grid[i][j] < 1 or grid[i][j] > 9 or grid[i][j] in seen:
                        return False
                    seen.add(grid[i][j])

            magic_sum = sum(grid[r][c:c+3])
            for i in range(r+1, r+3):
                if sum(grid[i][c:c+3]) != magic_sum:
                    return False
            for j in range(c, c+3):
                if grid[r][j] + grid[r+1][j] + grid[r+2][j] != magic_sum:
                    return False
            if grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != magic_sum:
                return False
            if grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != magic_sum:
                return False
            
            return True

        n = len(grid)
        m = len(grid[0])
        count = 0
        for i in range(n - 2): 
            for j in range(m - 2): 
                if isMagicSquare(i, j):
                    count += 1
        return count
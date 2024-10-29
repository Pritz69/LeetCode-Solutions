class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        memo = [[-1] * cols for _ in range(rows)]
        
        def dfs(row, col):
            if memo[row][col] != -1:
                return memo[row][col]
            
            max_moves = 0
            for new_row, new_col in [(row - 1, col + 1), (row, col + 1), (row + 1, col + 1)]:
                if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] > grid[row][col]:
                    max_moves = max(max_moves, 1 + dfs(new_row, new_col))
            
            memo[row][col] = max_moves
            return memo[row][col]

        max_moves_overall = 0
        for row in range(rows):
            max_moves_overall = max(max_moves_overall, dfs(row, 0))
        
        return max_moves_overall
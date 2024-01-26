class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        mod = 10**9 + 7
        def rec(i, j, moves_left):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 1
            if moves_left == 0:
                return 0
            if (i, j, moves_left) in dp:
                return dp[(i, j, moves_left)]
            c = 0
            for d in range(4):
                ni = i + dx[d]
                nj = j + dy[d]
                c = (c + rec(ni, nj, moves_left - 1)) % mod
            dp[(i, j, moves_left)] = c
            return c
        dp = {}
        return rec(startRow, startColumn, maxMove)

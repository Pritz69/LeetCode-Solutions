class Solution:
    def restoreMatrix(self, rowSum, colSum):
        N = len(rowSum)
        M = len(colSum)

        orig_matrix = [[0] * M for _ in range(N)]
        i, j = 0, 0

        while i < N and j < M:
            orig_matrix[i][j] = min(rowSum[i], colSum[j])

            rowSum[i] -= orig_matrix[i][j]
            colSum[j] -= orig_matrix[i][j]

            if rowSum[i] == 0:
                i += 1
            else:
                j += 1

        return orig_matrix
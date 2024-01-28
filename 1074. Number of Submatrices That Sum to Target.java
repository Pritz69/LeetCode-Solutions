class Solution {
    public int numSubmatrixSumTarget(int[][] matrix, int target) {
        int m = matrix.length, n = matrix[0].length;
        int[][] sum = new int[m + 1][n + 1];
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                sum[i][j] = sum[i - 1][j] + sum[i][j - 1] - sum[i - 1][j - 1] + matrix[i - 1][j - 1];
            }
        }
        int ans = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                for (int u = i + 1; u <= m; u++) {
                    for (int v = j + 1; v <= n; v++) {
                        int _sum = sum[u][v] - sum[i][v] - sum[u][j] + sum[i][j];
                        if (_sum == target) {
                            ans++;
                        }
                    }
                }
            }
        }
        return ans;
    }
}

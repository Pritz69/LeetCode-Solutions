class Solution {
    public int minFallingPathSum(int[][] grid) {
        int n = grid.length;
        int m = grid[0].length;
        if (n == 1) {
            return grid[0][0];
        }
        int[][] memo = new int[n][m];
        for (int i = 0; i < n; i++) 
        {
            for (int j = 0; j < m; j++) 
            {
                memo[i][j] = Integer.MAX_VALUE;
            }
        }
        int min_sum = Integer.MAX_VALUE;
        for (int j = 0; j < m; j++) 
        {
            min_sum = Math.min(min_sum, rec(0, j, grid, memo));
        }
        return min_sum;
    }
    private int rec(int i, int j, int[][] grid, int[][] memo) 
    {
        int n = grid.length;
        int m = grid[0].length;
        if (i == n) {
            return 0;
        }
        if (memo[i][j] != Integer.MAX_VALUE) {
            return memo[i][j];
        }
        int min_path_sum = Integer.MAX_VALUE;
        for (int k = 0; k < m; k++) {
            if (k != j) {
                min_path_sum = Math.min(min_path_sum, grid[i][j] + rec(i + 1, k, grid, memo));
            }
        }
        memo[i][j] = min_path_sum;
        return min_path_sum;
    }
}


class Solution {
    public int minFallingPathSum(int[][] grid) {
        int n = grid.length, m = grid[0].length;
        int res = Integer.MAX_VALUE;
        int[][] dp = new int[n][m];
        for(int row[] : dp) {
            Arrays.fill(row, -1);
        }

        for(int j = 0; j < m; ++j) {
            dp[0][j] = grid[0][j];
        }

        for(int i = 1; i < n; ++i) {
            for(int j = 0; j < m; ++j) {
                int temp = Integer.MAX_VALUE;

                for(int k = 0; k < m; ++k) {
                    if(j != k) {
                        temp = Math.min(temp, grid[i][j] + dp[i - 1][k]);
                    }

                    dp[i][j] = temp;
                }
            }
        }

        for(int j = 0; j < m; ++j) {
            res = Math.min(res, dp[n - 1][j]);
        }

        return res;
    }
}

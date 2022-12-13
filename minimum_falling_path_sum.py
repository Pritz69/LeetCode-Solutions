class Solution {
    private int m=0, n=0;
    public int minFallingPathSum(int[][] matrix) {
        m=matrix.length;
        n=matrix[0].length;
        int[][] dp = new int[m][n];
        for(int[] arr: dp) {
            Arrays.fill(arr, -1);
        }
        int minSum=Integer.MAX_VALUE;
        for(int c=0;c<n;c++) {
            minSum = Math.min(minSum, minFallingPathSumHelp(matrix, 0, c, dp));
        }
        return minSum;
    }

    private int minFallingPathSumHelp(int[][] matrix, int r, int c, int[][] dp) {
        if(r==m-1 && c<n && c>=0) return dp[r][c] = matrix[r][c];
        if(r<0 || c<0 || r>m-1 || c>n-1) return Integer.MAX_VALUE;
        if(dp[r][c]!=-1) return dp[r][c];
        int prev = minFallingPathSumHelp(matrix, r+1, c-1, dp);
        int same = minFallingPathSumHelp(matrix, r+1, c, dp);
        int next = minFallingPathSumHelp(matrix, r+1, c+1, dp);
        return dp[r][c] = matrix[r][c] + Math.min(same, Math.min(prev, next));
    }
}

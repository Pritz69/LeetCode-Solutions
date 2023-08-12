class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
    int m=obstacleGrid.length;
    int n=obstacleGrid[0].length;
    int[][] tab = new int[m][n];
    for(int i=0; i<m; i++)
    {
        for(int j=0; j<n; j++)
        {
            if (obstacleGrid[i][j]==1)
            {
                tab[i][j]=0;
            }
            else if(i==0 && j==0)
            {
                tab[i][j] = 1;
            }
            else
            {
                int up=0;
                int down=0;
                if (i>0)
                {
                    up=tab[i-1][j];
                }
                if (j>0)
                {
                    down=tab[i][j-1];
                }
                tab[i][j] = up + down;
            }
        }
    }
    return tab[m-1][n-1];
    }
}
/* ---TLE FOR LARGE TEST CASES---
class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int m = obstacleGrid.length;
        int n = obstacleGrid[0].length;
        
        return dfs(obstacleGrid, 0, 0, m, n);
    }
    
    private int dfs(int[][] grid, int x, int y, int m, int n) {
        if (x >= m || y >= n || grid[x][y] == 1) {
            return 0;
        }
        
        if (x == m - 1 && y == n - 1) {
            return 1;
        }
        
        int right = dfs(grid, x, y + 1, m, n);
        int down = dfs(grid, x + 1, y, m, n);
        
        return right + down;
    }
}
*/

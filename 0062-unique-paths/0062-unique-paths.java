class Solution {
    public int uniquePaths(int m, int n) {
    int[][] tab = new int[m][n];
    for(int i=0; i<m; i++)
    {
        for(int j=0; j<n; j++)
        {
            if(i==0 && j==0)
            {
                tab[i][j] = 1;
            }
            else
            {
                int right=0;
                int down=0;
                if(i>0)
                {
                    down=tab[i-1][j];
                }
                if(j>0)
                {
                    right=tab[i][j-1];
                }
                tab[i][j] = right + down;
            }
        }
    }
    return tab[m-1][n-1];
    }
}
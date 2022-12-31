class Solution {
    public int uniquePaths(int m, int n) {
    int[][] tab = new int[m][n];
    for(int i=0; i<m; i++){
        for(int j=0; j<n; j++){
            if(i==0 && j==0)
            {
                tab[i][j] = 1;
            }
            else{
                int up=0;
                int down=0;
                if(i>0)
                {
                    up=tab[i-1][j];
                }
                if(j>0)
                {
                    down=tab[i][j-1];
                }
                tab[i][j] = up+down;
            }
        }
    }
    return tab[m-1][n-1];
    }
}

class Solution {
    public int uniquePaths(int m, int n) {
    int[][] tab = new int[m][n];
    
    for(int i=0; i<m; i++){
        for(int j=0; j<n; j++){
            if(i==0 || j==0){
                tab[i][j] = 1;
            }
            else{
                tab[i][j] = tab[i-1][j]+tab[i][j-1];
            }
        }
    }
    
    return tab[m-1][n-1];
}
}

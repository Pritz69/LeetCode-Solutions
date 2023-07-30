class Solution {
    public int solve(int i,int j,char a[],int [][]dp)
    {
        if(i==j)
        {
            return 1;
        }
        if (dp[i][j]!=0)
        {
            return dp[i][j];
        }
        int turns=Integer.MAX_VALUE;
        for (int k=i;k<j;k++)
        {
            turns=Math.min(turns, solve(i,k,a,dp) + solve(k+1,j,a,dp));
        }
        if (a[i]==a[j])
        {
            turns -=1;
        }
        dp[i][j]=turns;
        return turns;
    }
    public int strangePrinter(String s) {
        int n=s.length();
        int dp[][]=new int[n][n];
        char a[]=s.toCharArray();
        return solve(0,n-1,a,dp);
    }
}

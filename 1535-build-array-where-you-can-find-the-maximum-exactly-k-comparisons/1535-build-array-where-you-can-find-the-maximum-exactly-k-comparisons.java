class Solution {
    int n,m,k;
    public int solve(int idx,int Lis,int lar,int dp[][][])
    {
        if(idx==n)
        {
            if(Lis==k)
            {
                return 1;
            }
            return 0;
        }
        if (dp[idx][Lis][lar] !=-1 )
        {
            return dp[idx][Lis][lar] ;
        }
        int ans=0;
        for(int i=1;i<=m;i++)
        {
            if(i>lar)
            {
                ans += solve(idx+1,Lis+1,i,dp);
            }
            else
            {
                ans += solve(idx+1,Lis,lar,dp);
            }
            ans = ans % 1000000007;
        }
        return dp[idx][Lis][lar]=ans;
    }
    public int numOfArrays(int n, int m, int k) {
        this.n=n;
        this.m=m;
        this.k=k;
        int dp[][][]=new int[n+1][n+1][m+1]; // int dp[][][]=new int[51][51][101];  ==> By Constraints
        for(int i=0;i<=n;i++)
        {
            for(int j=0;j<=n;j++)
            {
                Arrays.fill(dp[i][j],-1);
            }
        }
        return solve(0,0,0,dp);
    }
}
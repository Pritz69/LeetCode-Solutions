class Solution {
    public long solve(int n,int goal,int k,long dp[][],int usongs,int ind)
    {
        int mod=(int)Math.pow(10,9) + 7;
        if(ind==goal)
        {
            if (usongs==n)
            {
                return 1;
            }
            return 0;                           // ARYAN MITTAL EXPLANATION
        }
        if (dp[usongs][ind]!=-1)
        {
            return dp[usongs][ind];
        }
        long usedsong=(Math.max(0,usongs-k) * solve(n,goal,k,dp,usongs,ind+1)) % mod;
        long unusedsong=((n-usongs) * solve(n,goal,k,dp,usongs+1,ind+1)) % mod;
        long total=(usedsong+unusedsong) % mod;
        dp[usongs][ind]=total;
        return total;
    }
    public int numMusicPlaylists(int n, int goal, int k) {
        long dp[][]=new long[goal+1][goal+1];
        for (int i = 0; i <= n; i++) 
        {
            Arrays.fill(dp[i], -1);
        }
        return (int)solve(n,goal,k,dp,0,0);
    }
}

class Solution {
    public int maxProfit(int[] prices, int fee) {
        int n=prices.length;
        int dp[][]=new int[n+1][2];
        for(int i=n-1;i>=0;i--)
        {
            for(int b=0;b<=1;b++)
            {
                if (b==1)
                {
                    dp[i][b]=Math.max(-prices[i]+dp[i+1][0], 0+dp[i+1][1]);
                }
                if(b==0)
                {
                    dp[i][b]=Math.max(+prices[i]+dp[i+1][1]-fee, 0+dp[i+1][0]);
                }
            }
        }
        return dp[0][1];
    }
}
